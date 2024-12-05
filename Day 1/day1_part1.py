numbers = []

with open("Day 1/puzzle_input.txt", "r") as f:
    for line in f:
        num1, num2 = map(int, line.split())
        numbers.append((num1, num2))
# print(numbers)

#Creating 2 lists and sorting them.

left_numbers = [num1 for num1, num2 in numbers]
right_numbers = [num2 for num1, num2 in numbers]

left_numbers.sort()
right_numbers.sort()

# Rejoin the 2 lists

sorted_nums  =list(zip(left_numbers, right_numbers))

total_distance = 0
for num1, num2 in sorted_nums:
    distance = 0
    if num1 > num2:
        distance = num1 - num2
        total_distance += distance
    elif num2 > num1:
        distance = num2 - num1
        total_distance += distance
    else:
        distance = 0

print(total_distance)
        