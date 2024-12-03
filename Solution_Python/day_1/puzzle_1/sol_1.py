from itertools import product

with open('C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_1\\input_1.txt', 'r') as f:
    list_raw_1 = f.readlines()

with open('C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_1\\input_2.txt', 'r') as f:
    list_raw_2 = f.readlines()


list_1 = [int(num_raw) for num_raw in list_raw_1]
list_2 = [int(num_raw) for num_raw in list_raw_2]
list_1.sort()
list_2.sort()

sum_diff = 0

list_len = len(list_1)

for i in range(list_len):
    diff = abs(list_1[i] - list_2[i])
    sum_diff += diff

print(sum_diff)