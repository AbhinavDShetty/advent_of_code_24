from pathlib import Path
from collections import deque

file_path = Path(__file__).parent / "input1.txt"

def read_file():
    with open(file_path, 'r') as f:
        maze = [list(line.strip()) for line in f if line.strip()]
    return maze


def print_maze(maze):
    # for row in maze:
    #     for column in row:
    #         print(column, end='')
    #     print()
    for row in maze:
        print(row)


directions = [(1, 0), (0, -1), (-1, 0), (0, 1)] # Down Left Up Right


def turn_right(current_direction):
    return directions[(directions.index(current_direction) + 1) % 4]


def turn_left(current_direction):
    return directions[(directions.index(current_direction) - 1) % 4]


def bfs(maze):
    queue = deque()
    start = (len(maze) - 2, 1, (0, 1), 0)
    maze[len(maze)-2][1] = 0
    queue.append(start)
    
    while queue:
        current = queue.popleft()
        cur_x, cur_y, cur_dir, cur_score = current[0], current[1], current[2], current[3]
        
        allowed_directions_score = [(cur_dir, cur_score + 1), (turn_left(cur_dir), cur_score + 1001), (turn_right(cur_dir), cur_score + 1001)]
        
        for new_dir, new_score in allowed_directions_score:
            new_x, new_y = cur_x + new_dir[0], cur_y + new_dir[1]
            
            if maze[new_x][new_y] == '#':
                continue
            
            if maze[new_x][new_y] in ['.','E'] or (isinstance(maze[new_x][new_y], int) and maze[new_x][new_y]> new_score):
                maze[new_x][new_y] = new_score
                queue.append((new_x, new_y, new_dir, new_score))
        
    return maze[1][len(maze[1])-2]


def resolve():
    maze = read_file()
    result = bfs(maze)
    print("The Final Maze is:\n")
    print_maze(maze)
    return result

print(resolve())