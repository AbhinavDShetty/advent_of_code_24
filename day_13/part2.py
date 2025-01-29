import re
from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
# Read input file and split into lines
with open(file_path,"r") as file:
    input_lines = file.read().splitlines()

# Function to calculate tokens based on machine configuration
def calculate_tokens(machine: dict) -> int:
    prize_x, prize_y = machine["prize"]
    prize_x, prize_y = prize_x + 10000000000000, prize_y + 10000000000000
    button_a_x, button_a_y = machine["button_a"]
    button_b_x, button_b_y = machine["button_b"]

    low, high = 1, min(prize_x, prize_y)

    j1 = ((prize_x + prize_y) - (button_a_x + button_a_y)) / (button_b_x + button_b_y)
    j2 = ((prize_x + prize_y) - 2 * (button_a_x + button_a_y)) / (button_b_x + button_b_y)

    is_increasing = 1 * button_a_x + j1 * button_b_x < 2 * button_a_x + j2 * button_b_x

    if is_increasing:
        while low <= high:
            i = (low + high) // 2
            j = ((prize_x + prize_y) - i * (button_a_x + button_a_y)) / (button_b_x + button_b_y)
            required_prize_x = i * button_a_x + j * button_b_x

            if required_prize_x < prize_x:
                low = i + 1
            elif required_prize_x > prize_x:
                high = i - 1
            else:
                return i * 3 + int(j)
    else:
        while low <= high:
            i = (low + high) // 2
            j = ((prize_x + prize_y) - i * (button_a_x + button_a_y)) / (button_b_x + button_b_y)
            required_prize_x = i * button_a_x + j * button_b_x

            if required_prize_x > prize_x:
                low = i + 1
            elif required_prize_x < prize_x:
                high = i - 1
            else:
                return i * 3 + int(j)

    return 0

# Initialize machine configuration and total token count
machine_config = {}
total_tokens = 0

# Parse input lines and process each machine configuration
for line in input_lines:
    if match := re.fullmatch(r"Button A: X\+(\d+), Y\+(\d+)", line):
        button_a_x, button_a_y = map(int, match.groups())
        machine_config["button_a"] = (button_a_x, button_a_y)
    elif match := re.fullmatch(r"Button B: X\+(\d+), Y\+(\d+)", line):
        button_b_x, button_b_y = map(int, match.groups())
        machine_config["button_b"] = (button_b_x, button_b_y)
    elif match := re.fullmatch(r"Prize: X=(\d+), Y=(\d+)", line):
        prize_x, prize_y = map(int, match.groups())
        machine_config["prize"] = (prize_x, prize_y)
        tokens = calculate_tokens(machine_config)
        total_tokens += tokens
        machine_config = {}

# Print the total tokens calculated
print(total_tokens)
