import re

with open("C:\\Users\\abhin\\OneDrive\\文档\\GitHub\\advent_of_code_24\\Solution_Python\\day_3\\input.txt", "r") as f:
    data_raw = f.read()
print(data_raw)
mul_match = re.findall(r'\bmul\((\d+),(\d+)\)', data_raw)

count = 0
for i in mul_match:
    count += 1

sum_value = sum(int(x)*int(y) for x,y in mul_match)
print(count)
print(sum_value)