# In day_checks.py
import re
import requests

def check_day_files(day_number, auth_headers, pr_files, repo, pr_head_sha):
    errors = []
    
    if day_number == 1:
        expected_file_path = "daily_tasks/day_1/day1_answers.md"
        
        # Find the specific file object in the list of changed files
        target_file = next((f for f in pr_files if f['filename'] == expected_file_path), None)
        
        if not target_file:
            errors.append(f"Day 1 requires `{expected_file_path}` in the PR.")
            return errors
        
        # Construct a reliable URL using the head commit SHA
        raw_url = f"https://raw.githubusercontent.com/{repo}/{pr_head_sha}/{target_file['filename']}"
        print(f"Attempting to fetch file content from URL: {raw_url}")
        
        try:
            # The API call to fetch the raw content
            content_resp = requests.get(raw_url, headers=auth_headers)
            content_resp.raise_for_status()
            file_content = content_resp.text
        except requests.exceptions.RequestException as e:
            # If the request fails for any reason, report the error.
            errors.append(f"Could not fetch content for `{expected_file_path}`: {e}")
            return errors
        
        # Perform content checks on the fetched file_content
        sheet_link_pattern = r"https?://docs\.google\.com/spreadsheets/.+"
        if not re.search(sheet_link_pattern, file_content):
            errors.append("Day 1 file must contain a valid Google Sheet link.")

        required_answers = [
            r"Total rows:\s*6310",
            r"Unique schools:\s*(1891|1931)",
            r"Most frequent incident type:\s*NoCrim\s*11772",
            r"Bronx incident %:\s*(28\.31%|28\.23%)"
        ]

        for pattern in required_answers:
            if not re.search(pattern, file_content, re.IGNORECASE):
                errors.append(f"Day 1 answer missing or incorrect format: `{pattern}`")
    
    return errors
