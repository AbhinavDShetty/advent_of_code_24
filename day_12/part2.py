from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
def read_grid():
    grid = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                grid.append(line)
    return grid


def neighbours(pos, grid):
    width, height = len(grid[0]), len(grid)
    x, y = pos
    if x > 0:
        yield (x - 1, y), grid[y][x - 1]
    if (x + 1) < width:
        yield (x + 1, y), grid[y][x + 1]
    if y > 0:
        yield (x, y - 1), grid[y - 1][x]
    if (y + 1) < height:
        yield (x, y + 1), grid[y + 1][x]


def get_num_sides(region):
    up_sides = 0
    down_sides = 0
    left_sides = 0
    right_sides = 0
    for (x, y) in region:
        left = x - 1
        right = x + 1
        above = y - 1
        below = y + 1
        right_not_in_region = (right, y) not in region
        below_not_region = (x, below) not in region

        if (x, above) not in region:
            if right_not_in_region or (right, above) in region:
                up_sides += 1

        if (x, below) not in region:
            if right_not_in_region or (right, below) in region:
                down_sides += 1

        if (left, y) not in region:
            if below_not_region or (left, below) in region:
                left_sides += 1

        if (right, y) not in region:
            if below_not_region or (right, below) in region:
                right_sides += 1

    return up_sides + down_sides + left_sides + right_sides


def flood_region(start_pos, grid):
    start_x, start_y = start_pos
    letter = grid[start_y][start_x]
    region = set()
    to_check = [start_pos]
    area = 0
    perimeter = 0
    while to_check:
        x, y = to_check.pop()
        if (x, y) in region:
            continue

        region.add((x, y))
        area += 1  
        num_sides = 4
        for n_pos, n_letter in neighbours((x, y), grid):
            if n_letter == letter:
                to_check.append(n_pos)
                num_sides -= 1
        perimeter += num_sides
    sides = get_num_sides(region)
    print(f"All Regions: {region}")
    return letter, region, area, perimeter, sides


grid = read_grid()
width, height = len(grid[0]), len(grid)
used = set()

region_info = []
for y in range(height):
    for x in range(width):
        if (x, y) in used:
            continue
        letter, region, area, perimeter, sides = flood_region((x, y), grid)
        region_info.append((letter, area, perimeter, sides))
        used.update(region)
print(f"Region Information: {region_info}")
price1 = sum(area * p for _l, area, p, _sides in region_info)
price2 = sum(area * sides for _l, area, p, sides in region_info)
print(f"Total price part1: {price1}")
print(f"Total price part2: {price2}")
