def is_safe(report):
    # Check if the levels are either all increasing or all decreasing
    increasing = True
    decreasing = True
    
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:  # Check if the difference is within the valid range
            return False
        
        if report[i] >= report[i + 1]:
            increasing = False  # Not strictly increasing
        if report[i] <= report[i + 1]:
            decreasing = False  # Not strictly decreasing
    
    return increasing or decreasing  # The report must be strictly increasing or decreasing

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
    return safe_count

# Read the file and store each line as a list of numbers
numbers = []

# Assuming the file is in the same folder as your script
with open("Day 2/puzzle_input.txt", "r") as f:
    for line in f:
        # Convert the line into a list of integers (strip any leading/trailing whitespace)
        num_list = list(map(int, line.strip().split()))
        numbers.append(num_list)

# Count how many reports are safe
safe_reports_count = count_safe_reports(numbers)
print(f"Number of safe reports: {safe_reports_count}")
