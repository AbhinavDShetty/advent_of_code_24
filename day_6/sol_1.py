from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
with open(file_path, 'r') as f:
    map_raw = f.readlines()

lab_map = [string.strip() for string in map_raw]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
dir_index = {'^': 0, '>': 1, 'v': 2, '<': 3}

guard_direction = None
X = None
Y = None

# Locate the guard's initial position and direction
for row_id, row in enumerate(lab_map):
    for col_id, col in enumerate(row):
        if col in dir_index:
            X, Y = row_id, col_id
            guard_direction = col
            break
    if X is not None and Y is not None:
        break
    
direction_index = dir_index[guard_direction]  # Initial direction index

visited = {(X, Y)}
rows, cols = len(lab_map), len(lab_map[0])

while True:
    dirX, dirY = directions[direction_index]
    newX, newY = X + dirX, Y + dirY
    if 0 <= newX < rows and 0 <= newY < cols and lab_map[newX][newY] != '#':
        X, Y = newX, newY
        visited.add((X, Y))
    else:
        direction_index = (direction_index + 1) % 4
    if not (0 <= newX < rows and 0 <= newY < cols):
        break

print("Visited positions:", len(visited))
