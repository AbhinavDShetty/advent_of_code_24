import itertools
from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
with open(file_path, 'r') as f:
    data = f.readlines()


equations = []
for line in data:
    target, numbers = line.split(":")
    target = int(target.strip())
    numbers = list(map(int, numbers.strip().split()))
    equations.append((target, numbers))

def calculate_possibility(numbers, target):
    
    possible = False
    operation = ['+','*']
    
    for operators in itertools.product(operation, repeat = len(numbers) - 1):
        result = numbers[0]
        for i, operator in enumerate(operators):
            if operator == '+':
                result += numbers[i+1]
            elif operator == '*':
                result *= numbers[i+1]
        if result == target:
            possible = True
            break
    
    return possible

total_sum = sum(target for target, numbers in equations if calculate_possibility(numbers, target))
print(total_sum)