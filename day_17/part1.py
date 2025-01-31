from pathlib import Path

file_path = Path(__file__).parent / "input2.txt"

def read_file():
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    registers = {}
    instructions = []
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("Register"):
            parts = line.split(":")
            register_name = parts[0].split(" ")[1]
            register_value = int(parts[1].strip())
            registers[register_name] = register_value
        
        elif line.startswith("Program"):
            instructions = list(map(int, line.split(":")[1].strip().split(",")))
    return registers, instructions


def combo_operand(number,registers):
    if 0 <= number <= 3:
        return number
    if number == 4:
        return registers["A"]
    if number == 5:
        return registers["B"]
    if number == 6:
        return registers["C"]
    if number == 7:
        raise Exception("Invalid operand")


def execute_instruction(registers, instructions):
    pointer = 0
    result = ""
    while pointer < len(instructions):
        opcode, operand = instructions[pointer], instructions[pointer+1]
        combo = combo_operand(operand,registers)
        
        if opcode == 0:
            registers["A"] = registers["A"] // (2 ** combo)
            pointer += 2
            continue
        if opcode == 1:
            registers["B"] = registers["B"] ^ operand
            pointer += 2
            continue
        if opcode == 2:
            registers["B"] = combo % 8
            pointer += 2
            continue
        if opcode == 3:
            if registers["A"] == 0:
                pointer += 2
                continue
            pointer = operand
            continue
        if opcode == 4:
            registers["B"] = registers["B"] ^ registers["C"]
            pointer += 2
            continue
        if opcode == 5:
            result += str(combo % 8) + ','
            pointer += 2
            continue
        if opcode == 6:
            registers["B"] = registers["A"] // (2 ** combo)
            pointer += 2
            continue
        if opcode == 7:
            registers["C"] = registers["A"] // (2 ** combo)
            pointer += 2
            continue
    
    return result


def resolve():
    registers, instructions = read_file()
    result = execute_instruction(registers, instructions)
    return result[:-1]


print(resolve())