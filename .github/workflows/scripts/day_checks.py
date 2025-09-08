import re
import requests

def check_day_files(day_number, auth_headers, pr_files):
    errors = []
    
    if day_number == 1:
        expected_file_path = "daily_tasks/day_1/day1_answers.md"
        
        target_file = next((f for f in pr_files if f['filename'] == expected_file_path), None)
        
        if not target_file:
            errors.append(f"Day 1 requires `{expected_file_path}` in the PR.")
            return errors
        
        raw_url = target_file['raw_url']
        print("Raw url: `{raw_url}`")
        try:
            content_resp = requests.get(raw_url, headers=auth_headers)
            content_resp.raise_for_status()
            file_content = content_resp.text
        except requests.exceptions.RequestException as e:
            errors.append(raw_url)
            errors.append(f"Could not fetch content for `{expected_file_path}`: {e}")
            return errors
        
        print("✅ File content fetched successfully.")

        sheet_link_pattern = r"https?://docs\.google\.com/spreadsheets/.+"
        if not re.search(sheet_link_pattern, file_content):
            errors.append("Day 1 file must contain a valid Google Sheet link.")
            print("❌ Google Sheet link check failed.")
        else:
            print("✅ Google Sheet link check passed.")

        required_answers = [
            r"Total rows:\s*6310",
            r"Unique schools:\s*(1891|1931)",
            r"Most frequent incident type:\s*NoCrim\s*11772",
            r"Bronx incident %:\s*(28\.31%|28\.23%)"
        ]

        for pattern in required_answers:
            if not re.search(pattern, file_content, re.IGNORECASE):
                errors.append(f"Day 1 answer missing or incorrect format: `{pattern}`")
                print(f"❌ Regex check failed for pattern: `{pattern}`")
            else:
                print(f"✅ Regex check passed for pattern: `{pattern}`")
    
    return errors
