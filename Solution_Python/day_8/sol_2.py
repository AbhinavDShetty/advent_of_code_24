from collections import defaultdict

with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_8\\input.txt") as f:
    data = f.read().splitlines()

lines = list(map(list, data))

rows, cols = len(data), len(data[0])
antenna_positions = defaultdict(list[tuple[int,int]])


def coordinateExists(x, y):
    return 0 <= x < rows and 0 <= y < cols


for i in range(rows):
    for j in range(cols):
        if data[i][j] != '.' and data[i][j] != '#':
            antenna_positions[data[i][j]].append((i, j))

for freq, positions in antenna_positions.items():
    for pos in positions:
        lines[pos[0]][pos[1]] = '#'
    for i in range(len(positions)):
        position = positions[i]
        oddPositions = positions[:i] + positions[i+1:]
        for pos in oddPositions:
            nextPosition = (pos[0]+(pos[0]-position[0]),pos[1] + (pos[1] - position[1]))
            while coordinateExists(*nextPosition):
                lines[nextPosition[0]][nextPosition[1]] = '#'
                nextPosition = (nextPosition[0]+(pos[0]-position[0]),nextPosition[1] + (pos[1] - position[1]))

aNodes = sum(map(lambda x:x.count("#"), lines))


print(aNodes)
