

import re

def check_day_files(day_number, file_names):
    errors = []

    if day_number == 1:
        # Step 1: Check that the file exists in the correct folder
        expected_file = "daily_tasks/day_1/day1_answers.md"
        if expected_file not in file_names:
            errors.append(f"Day 1 requires `{expected_file}` in the PR.")

        # Step 2: If file exists, check its content
        else:
            try:
                with open(expected_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check for Google Sheet link
                sheet_link_pattern = r"https?://docs\.google\.com/spreadsheets/.+"
                if not re.search(sheet_link_pattern, content):
                    errors.append("Day 1 file must contain a valid Google Sheet link.")

                # Check answers format
                required_answers = [
                    r"Total rows:\s*6310",
                    r"Unique schools:\s*(1891|1931)",
                    r"Most frequent incident type:\s*NoCrim\s*11772",
                    r"Bronx incident %:\s*(28\.31%|28\.23%)"
                ]

                for pattern in required_answers:
                    if not re.search(pattern, content, re.IGNORECASE):
                        errors.append(f"Day 1 answer missing or incorrect format: `{pattern}`")

            except FileNotFoundError:
                errors.append(f"Day 1 file `{expected_file}` not found in repository.")

    # Placeholder for other days
    elif day_number == 2:
        # Day 2 checks
        pass
    elif day_number == 3:
        # Day 3 checks
        pass
    elif day_number == 4:
        # Day 4 checks
        pass

    return errors
