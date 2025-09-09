def check_day_files(day_number, file_names):
    errors = []

    # A dictionary to store the expected files for each day
    # Day 4 requires two files, so its value is a list
    expected_files_by_day = {
        1: ["daily_tasks/day_1/day1_answers.md"],
        2: ["daily_tasks/day_2/day2_analysis.ipynb"],
        3: ["daily_tasks/day_3/day3_sql_analysis.ipynb"],
        4: ["daily_tasks/day_4/sat_modeling.ipynb", "daily_tasks/day_4/cleaned_sat_results.csv"],
        5: []  # No files required for day 5
    }

    # Get the list of files to check for the current day
    files_to_check = expected_files_by_day.get(day_number, [])

    if day_number == 5:
        print(f"✅ No file checks required for Day {day_number}.")
        return errors
    
    if not files_to_check:
        errors.append(f"Day {day_number} check logic is not defined.")
        return errors

    # Check if each expected file exists in the PR files
    for expected_file in files_to_check:
        if expected_file not in file_names:
            errors.append(f"Day {day_number} requires `{expected_file}` in the PR.")

    return errors
