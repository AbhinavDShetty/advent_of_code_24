import re

with open("C:\\Users\\abhin\\OneDrive\\文档\\GitHub\\advent_of_code_24\\Solution_Python\\day_3\\input.txt", "r") as f:
    data_raw = f.read()


mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
command_pattern = re.compile(r"(do\(\)|don't\(\))")

mul_enabled = True
total_sum = 0

words = re.split(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", data_raw)

for word in words:
    word = word.strip()
    mul_match = mul_pattern.match(word)
    command_match = command_pattern.match(word)

    if mul_match :
        if mul_enabled:
            x, y = map(int, mul_match.groups())
            total_sum += x * y

    elif command_match :
        mul_enabled = (command_match.group() == "do()")
        print(command_match.group())

print(total_sum)