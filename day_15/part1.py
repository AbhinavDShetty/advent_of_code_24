from pathlib import Path

file_path = Path(__file__).parent / "input.txt"

with open(file_path, 'r') as f:
    data1, data2 = f.read().split('\n\n')
    move_directions = data2.replace('\n', '')
    warehouse = [list(line) for line in data1.splitlines()]

robot_pos = None
for i, row in enumerate(warehouse):
    for j, cell in enumerate(row):
        if cell == '@':
            robot_pos = (i, j)
            print("Robot Default position: ",robot_pos)
        if robot_pos:
            break

directions = {
        '^': (-1,0),
        'v': (1,0),
        '<': (0,-1),
        '>': (0,1)
    }

def simulate_move(warehouse, move_directions, robot_pos, directions):
    rows, cols = len(warehouse), len(warehouse[0])
    
    for move in move_directions:
        dx, dy = directions[move]
        nx, ny = robot_pos[0] + dx, robot_pos[1] + dy
        
        if 0 <= nx < rows and 0 <= ny < cols and warehouse[nx][ny] == '#':
            continue
        
        if warehouse[nx][ny] == 'O':
            box_positions = [(nx,ny)]
            current_x, current_y = nx, ny
            
            while 0 <= current_x < rows and 0 <= current_y < cols and warehouse[current_x][current_y] == 'O':
                box_positions.append((current_x, current_y))
                current_x += dx
                current_y += dy
            
            if 0 <= current_x < rows and 0 <= current_y < cols and warehouse[current_x][current_y] == '.':
                for bx, by in reversed(box_positions):
                    warehouse[bx + dx][by + dy] = 'O'
                    warehouse[bx][by] = '.'
                    # print_map(warehouse, move)
                
                warehouse[nx][ny] = '@'
                warehouse[robot_pos[0]][robot_pos[1]] = '.'
                robot_pos = (nx, ny)
                # print_map(warehouse, move)
                
        elif warehouse[nx][ny] == '.':
            warehouse[nx][ny] = '@'
            warehouse[robot_pos[0]][robot_pos[1]] = '.'
            robot_pos = (nx, ny)
            # print_map(warehouse, move)
    
    return warehouse


def calculate_gps(warehouse):
    gps_sum = 0
    for i, row in enumerate(warehouse):
        for j, cell in enumerate(row):
            if cell == 'O':
                gps_sum += 100 * i + j
    return gps_sum

# def print_map(warehouse, move):
#     print("Move:", move)
#     print("Warehouse map:")
#     for row in warehouse:
#         print("".join(row))
#     print("\n")

final_warehouse_map = simulate_move(warehouse, move_directions, robot_pos, directions)
gps_sum = calculate_gps(final_warehouse_map)


# print("Final warehouse map:")
# for row in warehouse:
#     print("".join(row))
# print("\n")
print("Sum of GPS: ", gps_sum)