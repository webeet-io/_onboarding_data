import requests
import re
import base64

def check_day_files(day_number, auth_headers, pr_files, repo, pr_head_sha):
    errors = []

    # Dynamically define the expected file path and validation logic based on the day number
    expected_file_path = f"daily_tasks/day_{day_number}/day{day_number}_answers.md"

    target_file = next((f for f in pr_files if f['filename'] == expected_file_path), None)
    if not target_file:
        errors.append(f"Day {day_number} requires `{expected_file_path}` in the PR.")
        return errors
    
    # Use the GitHub Contents API to get the file's content
    api_url = f"https://api.github.com/repos/{repo}/contents/{target_file['filename']}?ref={pr_head_sha}"
    
    try:
        print(f"[DEBUG] Fetching file content from API URL: {api_url}")
        content_resp = requests.get(api_url, headers=auth_headers)
        content_resp.raise_for_status()
        file_data = content_resp.json()
        
        # The content is Base64 encoded, so it must be decoded
        file_content = base64.b64decode(file_data['content']).decode('utf-8')
        print(f"✅ Successfully fetched file via Contents API: {expected_file_path}")

    except requests.exceptions.RequestException as e:
        errors.append(f"Could not fetch content (looser) for `{expected_file_path}` via Contents API: {e}")
        return errors
    except KeyError:
        errors.append("File content not found in API response. Is the file empty or binary?")
        return errors

    # --- Content validation logic based on day ---
    if day_number == 1:
        # Check for Google Sheet link
        sheet_link_pattern = r"https?://docs\.google\.com/spreadsheets/\S+"
        if not re.search(sheet_link_pattern, file_content):
            errors.append("Day 1 file must contain a valid Google Sheet link.")

        # Check required answers for Day 1
        required_patterns = {
            "Total rows": r"Total rows:\s*6310",
            "Unique schools": r"Unique schools:\s*(1891|1931)",
            "Most frequent incident type": r"Most frequent incident type:\s*NoCrim\s*11772",
            "Bronx incident %": r"Bronx incident %:\s*(28\.31%|28\.23%)"
        }
        for label, pattern in required_patterns.items():
            if not re.search(pattern, file_content, re.IGNORECASE):
                errors.append(f"Day 1 answer missing or incorrect format for: {label}")
    
    elif day_number == 2:
        expected_file_path = f"daily_tasks/day_2/day2_answers.md"
        # Add Day 2 validation logic here
        errors.append("Day 2 validation is not yet implemented.")
        # Example check:
        # if not re.search(r"Another pattern", file_content):
        #     errors.append("Day 2 content check failed.")
    
    # Add other day-specific logic here
    elif day_number == 3:
        # Add Day 3 validation logic here
        errors.append("Day 3 validation is not yet implemented.")

    elif day_number == 4:
        # Add Day 4 validation logic here
        errors.append("Day 4 validation is not yet implemented.")

    return errors
