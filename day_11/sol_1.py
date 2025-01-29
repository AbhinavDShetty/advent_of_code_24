from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
with open(file_path) as f:
    numbers = [int(num) for num in f.read().split()]

for iteration in range(25):
    i = 0
    print(numbers)
    while i < len(numbers):
        num_str = str(numbers[i])
        num = numbers[i]
        if num == 0:
            numbers[i] = 1
        elif len(num_str) % 2 == 0:
            mid = len(num_str) // 2
            first_half = int(num_str[:mid])
            second_half = int(num_str[mid:])
            numbers[i:i+1] = [first_half, second_half]
            i += 1
        else:
            numbers[i] *= 2024
        i += 1

print(len(numbers))