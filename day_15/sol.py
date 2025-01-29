from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
COMMANDS = {
    "<": (0,-1),
    ">": (0,1),
    "^": (-1,0),
    "v": (1,0)
}


def read_file():
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    matrix_lines = []
    command_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            matrix_lines.append(line)
        elif line:
            command_lines.append(line)
    
    first_matrix = [list(row) for row in matrix_lines]
    second_matrix = []
    current_row = 0
    for i in range(len(first_matrix)):
        second_matrix.append([])
        for j in range(len(first_matrix[0])):
            if first_matrix[i][j] in ["#","."]:
                second_matrix[current_row] += [first_matrix[i][j],first_matrix[i][j]]
            if first_matrix[i][j] == "O":
                second_matrix[current_row] += ["[","]"]
            if first_matrix[i][j] == "@":
                second_matrix[current_row] += ["@","."]
        current_row += 1
    
    commands = list("".join(command_lines))
    
    return second_matrix, commands


def get_robot_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "@":
                return i,j


def move_object(current, direction, matrix, symbol):
    new_x, new_y = current[0] + direction[0], current[1] + direction[1]
    matrix[new_x][new_y] = symbol
    matrix[current[0]][current[1]] = "."


def update_with_direction(cod, direction):
    return cod[0] + direction[0], cod[1] + direction[1]


def find_boxes(current, direction, matrix):
    current_x, current_y = current[0], current[1]
    if matrix[current_x + direction[0]][current_y] == "[":
        return (current_x + direction[0], current_y),( current_x + direction[0], current_y + 1)
    return (current_x + direction[0], current_y - 1),( current_x + direction[0], current_y)


def interact_boxes(current, matrix, direction):
    if direction[0] == 0:
        new_x, new_y = current[0] + direction[0], current[1] + direction[1]
        
        while matrix[new_x][new_y] in ["[","]"]:
            new_x, new_y = new_x + direction[0], new_y + direction[1]
        
        if matrix[new_x][new_y] == '#':
            return current
        
        while (new_x,new_y) != current:
            new_x, new_y = new_x - direction[0], new_y - direction[1]
            move_object((new_x,new_y), direction, matrix, matrix[new_x][new_y])
        
        return update_with_direction(current, direction)
    
    connected_boxes = [find_boxes(current, direction, matrix)]
    
    i = 0
    while i < len(connected_boxes):
        box = connected_boxes[i]
        left_bracket, right_bracket = box[0], box[1]
        new_x_left_bracket, new_y_left_bracket = update_with_direction(left_bracket, direction)
        new_x_right_bracket, new_y_right_bracket = update_with_direction(right_bracket, direction)
        
        if (matrix[new_x_left_bracket][new_y_left_bracket]) == "#" or (matrix[new_x_right_bracket][new_y_right_bracket]) == "#":
            return current
        if matrix[new_x_left_bracket][new_y_left_bracket] in ['[', ']']:
            connected_boxes.append(find_boxes(left_bracket, direction, matrix))
        if matrix[new_x_right_bracket][new_y_right_bracket] in ['[', ']']:
            connected_boxes.append(find_boxes(right_bracket, direction, matrix))
        i += 1
    
    i-=1
    while i >= 0:
        box = connected_boxes[i]
        left_bracket, right_bracket = box[0], box[1]
        move_object(left_bracket, direction, matrix, symbol='[')
        move_object(right_bracket, direction, matrix, symbol=']')
        i -= 1
    move_object(current, direction, matrix, '@')
    
    return update_with_direction(current, direction)


def final_map(matrix, commands, start_position):
    current = start_position
    for command in commands:
        direction = COMMANDS[command]
        new_x, new_y = current[0] + direction[0], current[1] + direction[1]
        if matrix[new_x][new_y] == "#":
            continue
        if matrix[new_x][new_y] == ".": 
            move_object(current, direction, matrix, "@")
            current = update_with_direction(current, direction)
        if matrix[new_x][new_y] in ["[","]"]:
            current = interact_boxes(current, matrix, direction)
        # print_matrix(matrix)


def result_solution(matrix):
    result = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == "[":
                result += 100 * i + j
    return result


def resolve():
    matrix, commands = read_file()
    start_position = get_robot_pos(matrix)
    final_map(matrix, commands, start_position)
    return result_solution(matrix)


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


print(resolve())