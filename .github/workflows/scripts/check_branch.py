import os
import requests
import re
import jwt
import time

# Inputs from workflow
repo = os.environ['TARGET_REPO']
pr_number = os.environ['PR_NUMBER']

# GitHub App secrets (must exist in Repo B)
app_id = os.environ['DATAGREMLIN_APP_ID']
private_key = os.environ["DATAGREMLIN_APP_KEY"].replace("\\n", "\n").strip()

# Step 1: Generate JWT for GitHub App
now = int(time.time())
payload = {
    "iat": now - 60,                # issued 1 min earlier to allow clock drift
    "exp": now + (10 * 60),         # expires in 10 minutes
    "iss": app_id
}
jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

# Step 2: Get installation ID for the target repo
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Accept": "application/vnd.github+json"
}
installations_url = "https://api.github.com/app/installations"
installations = requests.get(installations_url, headers=headers).json()

installation_id = None
for inst in installations:
    repos_url = inst.get("repositories_url")
    if repos_url:
        repos = requests.get(repos_url, headers=headers).json().get("repositories", [])
        if any(r["full_name"] == repo for r in repos):
            installation_id = inst["id"]
            break

if not installation_id:
    raise Exception(f"No installation found for repo {repo}")

# Step 3: Generate installation token
token_url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
token_resp = requests.post(token_url, headers=headers)
token = token_resp.json()['token']

auth_headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

# Step 4: Fetch PR info
pr_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
pr = requests.get(pr_url, headers=auth_headers).json()
branch_name = pr['head']['ref']

print(f"Checking PR branch: {branch_name}")

# Step 5: Regex check for firstname-lastname-day[1-4]
if not re.match(r'^[a-z]+-[a-z]+-day[1-4]$', branch_name):
    print("❌ Branch name invalid")

    # Check if bot already commented
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    comments = requests.get(comments_url, headers=auth_headers).json()

    bot_username = requests.get("https://api.github.com/user", headers=auth_headers).json()['login']

    already_commented = any(c['user']['login'] == bot_username for c in comments)

    if not already_commented:
        comment_body = f"❌ You're trying to merge from the wrong branch name: `{branch_name}`.\n" \
                       f"Branch names must follow: firstname-lastname-day1..4"
        requests.post(comments_url, headers=auth_headers, json={"body": comment_body})
    else:
        print("Bot comment already exists, skipping")

    exit(1)  # FAIL the workflow

print("✅ Branch name is valid")


