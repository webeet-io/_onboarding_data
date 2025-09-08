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
# The JWT is a temporary token for authenticating as the app itself.
# It grants permission to request an installation token.
now = int(time.time())
payload = {
    "iat": now - 60,                # issued 1 min earlier to allow for clock drift
    "exp": now + (10 * 60),          # expires in 10 minutes
    "iss": app_id
}
jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

# Step 2: Get installation ID for the target repo
# This is the correct method to find the installation ID for a specific repository.
# It uses the JWT to authenticate to a dedicated app endpoint.
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

    installation_response.raise_for_status() # Raises an exception for other HTTP errors (e.g., 401, 500)

    installation_data = installation_response.json()
    installation_id = installation_data['id']

except requests.exceptions.RequestException as e:
    raise Exception(f"Failed to retrieve installation ID: {e}")

# Step 3: Generate installation token
# The installation token is now used to make API calls on behalf of the app
# within the context of the specific repository.
token_url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
token_resp = requests.post(token_url, headers=headers)
token_resp.raise_for_status() # Ensure the token request was successful
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

print(f"Checking PR branch: {branch_name}")

# Step 5: Regex check for firstname-lastname-day[1-4]
if not re.match(r'^[a-z]+-[a-z]+-day[1-4]$', branch_name):
    print("❌ Branch name invalid")

    # Check if bot already commented
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    comments_resp = requests.get(comments_url, headers=auth_headers)
    comments_resp.raise_for_status()
    comments = comments_resp.json()

    # Get the app's username using the JWT token
    # The '/app' endpoint requires JWT authentication.
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

    exit(1)  # FAIL the workflow

print("✅ Branch name is valid")
