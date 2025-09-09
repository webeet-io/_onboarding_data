import os
import sys
import requests
import re
import jwt
import time


# Inputs from workflow
repo = os.environ['TARGET_REPO']
pr_number = os.environ['PR_NUMBER']

# GitHub App secrets
app_id = os.environ['DATAGREMLIN_APP_ID']
private_key = os.environ["DATAGREMLIN_APP_KEY"].replace("\\n", "\n").strip()

# Step 1: Generate JWT for GitHub App
now = int(time.time())
payload = {
    "iat": now - 60,
    "exp": now + (10 * 60),
    "iss": app_id
}
jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

# Step 2: Get installation ID for the target repo
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Accept": "application/vnd.github+json"
}
installation_url = f"https://api.github.com/repos/{repo}/installation"

installation_id = None
try:
    installation_response = requests.get(installation_url, headers=headers)
    if installation_response.status_code == 404:
        raise Exception(f"No installation found for repo {repo}")
    installation_response.raise_for_status()
    installation_data = installation_response.json()
    installation_id = installation_data['id']
except requests.exceptions.RequestException as e:
    raise Exception(f"Failed to retrieve installation ID: {e}")

# Step 3: Generate installation token
token_url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
token_resp = requests.post(token_url, headers=headers)
token_resp.raise_for_status()
token = token_resp.json()['token']

auth_headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

# Step 4: Fetch PR info
pr_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
pr_resp = requests.get(pr_url, headers=auth_headers)
pr_resp.raise_for_status()
pr = pr_resp.json()
branch_name = pr['head']['ref']
base_branch = pr['base']['ref']
pr_head_sha = pr['head']['sha']

# Step 5: Check branch name and extract info
branch_match = re.match(r'^([a-z]+-[a-z]+)-day([1-4])$', branch_name)

if not branch_match:
    print("❌ Branch name invalid")
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    comments_resp = requests.get(comments_url, headers=auth_headers)
    comments_resp.raise_for_status()
    comments = comments_resp.json()
    app_info_url = "https://api.github.com/app"
    app_info_resp = requests.get(app_info_url, headers=headers)
    app_info_resp.raise_for_status()
    bot_username = app_info_resp.json()['slug']
    already_commented = any(c['user']['login'] == bot_username for c in comments)
    if not already_commented:
        comment_body = (
            f"❌ You're trying to merge from the wrong branch name: `{branch_name}`.\n"
            f"Branch names must follow: `firstname-lastname-day1..4`"
        )
        requests.post(comments_url, headers=auth_headers, json={"body": comment_body})
    else:
        print("Bot comment already exists, skipping")
    exit(1)

# If we get here, the branch name is correct, so we can safely use branch_match
expected_base = branch_match.group(1)
day_number = int(branch_match.group(2))
print("✅ Branch name is valid")

# Step 6: Validate PR base branch
print(f"PR is trying to merge into: {base_branch}")

if base_branch != expected_base:
    print(f"❌ PR must be targeted to `{expected_base}`, not `{base_branch}`")
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    comment_body = (
        f"❌ Pull request must be targeted to `{expected_base}`, not `{base_branch}`.\n"
        f"Please change the base branch."
    )
    requests.post(comments_url, headers=auth_headers, json={"body": comment_body})
    exit(1)

print("✅ PR base branch is correct")

# Step 7: Fetch PR files and run checks
files_url = pr['url'] + "/files"
files_resp = requests.get(files_url, headers=auth_headers)
files_resp.raise_for_status()
pr_files = files_resp.json()
file_names = [f['filename'] for f in pr_files]
print(f"Files in this PR: {file_names}")

# Step 8: Run day-specific checks
def check_day_files(day_number, file_names):
    errors = []
    
    expected_files_by_day = {
        1: {"daily_tasks/day_1/day1_answers.md"},
        2: {"daily_tasks/day_2/day2_analysis.ipynb"},
        3: {"daily_tasks/day_3/day3_sql_analysis.ipynb"},
        4: {"daily_tasks/day_4/sat_modeling.ipynb", "daily_tasks/day_4/cleaned_sat_results.csv"},
        5: set()  # No files required for day 5
    }

    files_to_check = expected_files_by_day.get(day_number, set())
    
    if day_number == 5:
        print(f"✅ No file checks required for Day {day_number}.")
        return errors
    
    # Check if there are any files for this day in the dictionary
    if not files_to_check:
        errors.append(f"Day {day_number} check logic is not defined or requires no files.")
        return errors

    # Check for extra files in the PR that shouldn't be there
    pr_files_set = set(file_names)
    extra_files = pr_files_set - files_to_check
    if extra_files:
        errors.append(f"Unexpected files found in the PR: {', '.join(sorted(list(extra_files)))}")
        # We don't return here so we can also check for missing files

    # Check for missing required files
    missing_files = files_to_check - pr_files_set
    if missing_files:
        for missing_file in sorted(list(missing_files)):
            errors.append(f"Missing required file: `{missing_file}`.")

    if not errors:
        for expected_file in sorted(list(files_to_check)):
            print(f"✅ Found expected file: {expected_file}")

    return errors



day_errors = check_day_files(day_number, file_names)
if day_errors:
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    comment_body = "❌ Day-specific file checks failed:\n" + "\n".join(day_errors)
    requests.post(comments_url, headers=auth_headers, json={"body": comment_body})
    exit(1)
else:
    print(f"✅ All day {day_number} files are correct")
