import requests
import re
import base64

def check_day_files(day_number, auth_headers, pr_files, repo, pr_head_sha):
    errors = []

    if day_number == 1:
        expected_file_path = "daily_tasks/day_1/day1_answers.md"

        # Find the file in the PR files
        target_file = next((f for f in pr_files if f['filename'] == expected_file_path), None)
        if not target_file:
            errors.append(f"Day 1 requires `{expected_file_path}` in the PR.")
            return errors

        print(f"[DEBUG] Found target file: {target_file['filename']}")

        # Build the GitHub Contents API URL
        api_url = f"https://api.github.com/repos/{repo}/contents/{target_file['filename']}?ref={pr_head_sha}"
        print(f"[DEBUG] Fetching file content from API URL: {api_url}")

        try:
            content_resp = requests.get(api_url, headers=auth_headers)
            content_resp.raise_for_status()
            file_data = content_resp.json()
            # Decode Base64 content
            file_content = base64.b64decode(file_data['content']).decode('utf-8')
            print(f"✅ Successfully fetched file via Contents API: {expected_file_path}")
        except requests.exceptions.RequestException as e:
            errors.append(f"Could not fetch content for `{expected_file_path}` via Contents API: {e}")
            return errors

        # --- Content validation ---
        # Check Google Sheet link
        sheet_link_pattern = r"https?://docs\.google\.com/spreadsheets/\S+"
        if not re.search(sheet_link_pattern, file_content):
            errors.append("Day 1 file must contain a valid Google Sheet link.")

        # Check required answers
        required_patterns = {
            "Total rows": r"Total rows:\s*6310",
            "Unique schools": r"Unique schools:\s*(1891|1931)",
            "Most frequent incident type": r"Most frequent incident type:\s*NoCrim\s*11772",
            "Bronx incident %": r"Bronx incident %:\s*(28\.31%|28\.23%)"
        }

        for label, pattern in required_patterns.items():
            if not re.search(pattern, file_content, re.IGNORECASE):
                errors.append(f"Day 1 answer missing or incorrect format for: {label}")

    # Placeholder for other days
    elif day_number in [2, 3, 4]:
        print(f"[DEBUG] Day {day_number} checks not implemented yet.")

    return errors
