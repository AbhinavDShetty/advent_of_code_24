with open('C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_1\\input_1.txt', 'r') as f:
    list_raw_1 = f.readlines()
    
with open('C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_1\\input_2.txt', 'r') as f:
    list_raw_2 = f.readlines()
    
list_1 = [int(num_raw) for num_raw in list_raw_1]
list_2 = [int(num_raw) for num_raw in list_raw_2]

total_sum = 0

for num1 in list_1:
    num_count = sum(1 for num2 in list_2 if num1 == num2)
    total_sum += num_count * num1
    
print(total_sum)