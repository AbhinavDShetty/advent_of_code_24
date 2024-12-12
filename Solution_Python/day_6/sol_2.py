import itertools

with open('C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_6\\input.txt', 'r') as f:
    map_raw = f.readlines()

lab_map = [string.strip() for string in map_raw]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_index = {'^': 0, '>': 1, 'v': 2, '<': 3}

guard_direction = None
X = None
Y = None

for row_id, row in enumerate(lab_map):
    for col_id, col in enumerate(row):
        if col in dir_index:
            X, Y = row_id, col_id
            guard_direction = col
            break
    if X is not None and Y is not None:
        break

start_direction = dir_index[guard_direction]
rows, cols = len(lab_map), len(lab_map[0])

def simulate_loop(lab_map, startX, startY, start_direction):
    direction_index = start_direction
    X, Y = startX, startY
    visited = {((X, Y), direction_index)}

    while True:
        dirX, dirY = directions[direction_index]
        newX, newY = X + dirX, Y + dirY

        if 0 <= newX < rows and 0 <= newY < cols:
            if lab_map[newX][newY] not in ['#', 'O']:
                X, Y = newX, newY
                if ((X, Y), direction_index) in visited:
                    return True
                visited.add(((X, Y), direction_index))
            else:
                direction_index = (direction_index + 1) % 4
        else:
            break

    return False

possible_positions = set()

for x, y in itertools.product(range(rows), range(cols)):
    if lab_map[x][y] != '#' and (x, y) != (X, Y):
        original_char = lab_map[x][y]
        lab_map[x] = f'{lab_map[x][:y]}O{lab_map[x][y + 1:]}'

        if simulate_loop(lab_map, X, Y, start_direction):
            possible_positions.add((x, y))

        lab_map[x] = f'{lab_map[x][:y]}{original_char}{lab_map[x][y + 1:]}'

print(f'Possible Positions: {possible_positions}')
print(f'Total Possible Positions: {len(possible_positions)}')
