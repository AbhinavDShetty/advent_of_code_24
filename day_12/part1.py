from collections import deque

with open('C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\day_12\\input.txt', 'r') as f:
    farm_map = [list(line.strip()) for line in f]

rows = len(farm_map)
cols = len(farm_map[0])
visited = [[False for _ in range(cols)] for _ in range(rows)]

def get_neighbors(r, c):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def flood_fill(startX, startY):
    queue = deque([(startX, startY)])
    plant_type = farm_map[startX][startY]
    visited[startX][startY] = True
    area = 0
    while queue:
        x, y = queue.popleft()
        area += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if farm_map[nx][ny] == plant_type:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    perimeter += 1
            else:
                perimeter += 1
    return area, perimeter

total_price = 0
for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            area, perimeter = flood_fill(i, j)
            total_price += area * perimeter

print(f"The total price is: {total_price}")