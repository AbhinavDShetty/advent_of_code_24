from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

robots = []

for line in data.strip().split('\n'):
    part_p, part_v = line.split(" v=")
    px, py = map(int,part_p[2:].split(','))
    vx, vy = map(int,part_v.split(','))
    robots.append((px,py,vx,vy))


width = 101
height = 103
seconds = 100


def move_robots(robots, seconds, width, height):
    positions = []
    for px, py, vx, vy in robots:
        new_px = (px + seconds * vx) % width
        new_py = (py + seconds * vy) % height
        positions.append((new_px, new_py))
    return positions

def quadrants(positions, width, height):
    q1 = q2 = q3 = q4 = 0
    for x, y in positions:
        if x > width//2 and y > height//2:
            q1 += 1
        elif x > width//2 and y < height//2:
            q2 += 1
        elif x < width//2 and y > height//2:
            q3 += 1
        elif x < width//2 and y < height//2:
            q4 += 1
    return q1, q2, q3, q4


positions_after_100 = move_robots(robots, seconds, width, height)

q1, q2, q3, q4 = quadrants(positions_after_100, width, height)

safety_factor = q1 * q2 * q3 * q4

print(f"Quadrant count: {q1}, {q2}, {q3}, {q4}")
print(f"Safety factor: {safety_factor}")
