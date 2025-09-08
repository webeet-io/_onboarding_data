import re
import requests

def check_day_files(day_number, auth_headers, pr_files):
    errors = []
    file_names = [f['filename'] for f in pr_files]

    if day_number == 1:
        # Step 1: Check that the file exists in the correct folder
        expected_file_path = "daily_tasks/day_1/day1_answers.md"
        
        file_found = False
        file_content = None
        for f in pr_files:
            if f['filename'] == expected_file_path:
                file_found = True
                try:
                    # Fetch the raw content of the file using the GitHub API
                    content_resp = requests.get(f['raw_url'], headers=auth_headers)
                    content_resp.raise_for_status()
                    file_content = content_resp.text
                except requests.exceptions.RequestException as e:
                    errors.append(f"Could not fetch content for `{expected_file_path}`: {e}")
                break

        if not file_found:
            errors.append(f"Day 1 requires `{expected_file_path}` in the PR.")
        elif file_content:
            # Step 2: If file exists and content is fetched, check its content
            
            # Check for Google Sheet link
            sheet_link_pattern = r"https?://docs\.google\.com/spreadsheets/.+"
            if not re.search(sheet_link_pattern, file_content):
                errors.append("Day 1 file must contain a valid Google Sheet link.")

            # Check answers format
            # Using tuple to make it easier to add new values
            required_answers = [
                r"Total rows:\s*6310",
                r"Unique schools:\s*(1891|1931)",
                r"Most frequent incident type:\s*NoCrim\s*11772",
                r"Bronx incident %:\s*(28\.31%|28\.23%)"
            ]

            for pattern in required_answers:
                if not re.search(pattern, file_content, re.IGNORECASE):
                    errors.append(f"Day 1 answer missing or incorrect format: `{pattern}`")
    
    # Placeholder for other days - you will use the same pattern
    elif day_number == 2:
        # Day 2 checks
        pass
    
    return errors
