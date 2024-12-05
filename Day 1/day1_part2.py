numbers = []

with open("Day 1/puzzle_input.txt", "r") as f:
    for line in f:
        num1, num2 = map(int, line.split())
        numbers.append((num1, num2))

left_numbers = [num1 for num1, num2 in numbers]
right_numbers = [num2 for num1, num2 in numbers]

total_similarity = 0

for num1 in left_numbers:
    count = 0
    for num2 in right_numbers:
        if num1 == num2:
            count+=1
    similarity = num1 * count
    total_similarity += similarity

print(total_similarity)
