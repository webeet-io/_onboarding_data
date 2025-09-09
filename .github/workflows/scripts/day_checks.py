# day_checks.py
import requests
import re
import base64

def check_day_files(day_number, auth_headers, pr_files, repo, pr_head_sha):
    errors = []

    if day_number == 1:
        expected_file_path = "daily_tasks/day_1/day1_answers.md"

        target_file = next((f for f in pr_files if f['filename'] == expected_file_path), None)
        if not target_file:
            errors.append(f"Day 1 requires `{expected_file_path}` in the PR.")
            return errors
        
        # This is the fix: construct the raw URL using the API response token.
        # This URL is more reliable for direct file access from a PR.
        raw_url = f"https://raw.githubusercontent.com/{repo}/{pr_head_sha}/{target_file['filename']}"
        
        print(f"[DEBUG] Fetching content from URL: {raw_url}")

        try:
            # We're using a different authentication method for the raw domain.
            # This is why the code was failing before.
            raw_headers = {
                "Accept": "application/vnd.github.v3.raw"
            }
            content_resp = requests.get(raw_url, headers=raw_headers, auth=(auth_headers.get('Authorization').split(' ')[1], 'x-oauth-basic'))
            content_resp.raise_for_status()
            file_content = content_resp.text
            
            # The raw content is NOT base64 encoded, so we don't need to decode it.
            print(f"✅ Successfully fetched file content for: {expected_file_path}")

        except requests.exceptions.RequestException as e:
            errors.append(f"Could not fetch content for `{expected_file_path}`: {e}")
            return errors
        
        # --- Content validation ---
        sheet_link_pattern = r"https?://docs\.google\.com/spreadsheets/\S+"
        if not re.search(sheet_link_pattern, file_content):
            errors.append("Day 1 file must contain a valid Google Sheet link.")

        required_patterns = {
            "Total rows": r"Total rows:\s*6310",
            "Unique schools": r"Unique schools:\s*(1891|1931)",
            "Most frequent incident type": r"Most frequent incident type:\s*NoCrim\s*11772",
            "Bronx incident %": r"Bronx incident %:\s*(28\.31%|28\.23%)"
        }

        for label, pattern in required_patterns.items():
            if not re.search(pattern, file_content, re.IGNORECASE):
                errors.append(f"Day 1 answer missing or incorrect format for: {label}")
    
    return errors
