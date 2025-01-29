import numpy as np
from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
def read_input_file():
    machines = []
    with open(file_path, 'r') as f:
        data = f.readlines()
        for i in range(0, len(data), 4):
            deltaX_a, deltaY_a = map(int, data[i].split(':')[1].strip().replace('X+', '').replace('Y+', '').split(', '))
            deltaX_b, deltaY_b = map(int, data[i + 1].split(':')[1].strip().replace('X+', '').replace('Y+', '').split(', '))
            prizeX, prizeY = map(int, data[i + 2].split(':')[1].strip().replace('X=', '').replace('Y=', '').split(', '))
            machines.append((deltaX_a, deltaY_a, deltaX_b, deltaY_b, prizeX, prizeY))
    return machines


def solve_machine(deltaX_a, deltaY_a, deltaX_b, deltaY_b, prizeX, prizeY):
    prize_max = 100
    min_cost = float('inf')
    costA = 3
    costB = 1
    bestA, bestB = None, None
    for i in range(prize_max + 1):
        for j in range(prize_max + 1):
            posX = i * deltaX_a + j * deltaX_b
            posY = i * deltaY_a + j * deltaY_b
            
            if posX == prizeX and posY == prizeY:
                cost = i * costA + j * costB
                if cost < min_cost:
                    min_cost = cost
                    bestA, bestB = i, j
    
    if bestA is not None and bestB is not None:
        return bestA, bestB, min_cost
    else:
        return None, None, None


machines = read_input_file()

total_cost = 0
times_won = 0

for i, (deltaX_a, deltaY_a, deltaX_b, deltaY_b, prizeX, prizeY) in enumerate(machines):
    bestA, bestB, min_cost = solve_machine(deltaX_a, deltaY_a, deltaX_b, deltaY_b, prizeX, prizeY)
    if min_cost is not None:
        print(f'Machine {i+1}: Won prize with Minimum Cost: {min_cost} ( A presses: {bestA}, B presses: {bestB})')
        total_cost += min_cost
        times_won += 1
    else:
        print(f'Machine {i+1}: No winning combination found.')

print(f"Total Times Won: {times_won}")
print(f"Total Minimum Cost: {total_cost}")