import numpy as np

with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_10\\input.txt") as f:
    grid = []
    for line in f.read().splitlines():
        grid.append([int(char) for char in line.strip() if char.isdigit()])

# print(grid)

grid = np.array(grid)
rows, cols = grid.shape
directions = [(-1,0), (1,0), (0,-1), (0,1)]

visited = set()
trailtails = []

def bfs(start):
    queue = [start]
    seen = set(queue)
    all_nines = set()
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen:
                # print(f"The new coordinates are {nx}, {ny} with a height {grid[nx,ny]}. For {grid[x,y]} in {x}, {y}.")
                if grid[nx, ny] == grid[x, y] + 1:
                    seen.add((nx, ny))
                    queue.append((nx, ny))
                    if grid[nx, ny] == 9:
                        all_nines.add((nx, ny))
    
    return all_nines

for i in range(rows):
    for j in range(cols):
        if grid[i, j] == 0 and (i,j) not in visited:
            trailtails.append((i, j))
            reachable = bfs((i,j))
            visited.update(reachable)
            
scores = [len(bfs(trailtail)) for trailtail in trailtails]

total_score = sum(scores)
print(total_score)