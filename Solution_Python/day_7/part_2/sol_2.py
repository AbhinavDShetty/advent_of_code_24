import itertools

with open('C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_7\\input.txt', 'r') as f:
    data = f.readlines()

equations = []
for line in data:
    target, numbers = line.split(":")
    equations.append((int(target.strip()), list(map(int, numbers.strip().split()))))

def calculate_possibility(numbers, target):
    
    possible = False
    operation = ['+','*','||']
    
    for operators in itertools.product(operation, repeat = len(numbers) - 1):
        result = numbers[0]
        for i, operator in enumerate(operators):
            if operator == '+':
                result += numbers[i+1]
            elif operator == '*':
                result *= numbers[i+1]
            elif operator == '||':
                result = int(str(result)+str(numbers[i+1]))
        if result == target:
            possible = True
            break
    
    return possible

total_sum = sum(target for target, numbers in equations if calculate_possibility(numbers, target))
print(total_sum)