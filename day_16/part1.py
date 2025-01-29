from pathlib import Path
from collections import deque

file_path = Path(__file__).parent / "input1.txt"

def read_file():
    with open(file_path, 'r') as f:
        maze = [list(line.strip()) for line in f if line.strip()]
    return maze


def print_maze(maze):
    for row in maze:
        for column in row:
            print(column, end='')
        print()


directions = [(1, 0), (0, -1), (-1, 0), (0, 1)] # Down Left Up Right


def turn_right(current_direction):
    return directions[(directions.index(current_direction) + 1) % 4]


def turn_left(current_direction):
    return directions[(directions.index(current_direction) - 1) % 4]
maze = read_file()
print(maze[len(maze) - 2][1])
def bfs(maze):
    queue = deque()
    start = (len(maze) - 2, 1, (0, 1), 0)
    queue.append(start)
    
    while queue: