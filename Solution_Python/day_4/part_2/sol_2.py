import itertools
with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_4\\input.txt", "r") as f:
    data_raw = f.read().split("\n")
data = [list(row) for row in data_raw]
rows, cols = len(data), len(data[0])

def find_X_MAS(data, x, y):
    
    if data[x][y] != 'A':
        return False
    
    if x > 0 and x < rows - 1 and y > 0 and y < cols - 1:
        topLeft = data[x - 1][y - 1]
        topRight = data[x - 1][y + 1]
        bottomLeft = data[x + 1][y - 1]
        bottomRight = data[x + 1][y + 1]
        
        if ((topLeft == 'M' and bottomRight == 'S') or (topLeft == 'S' and bottomRight == 'M')) and \
           ((topRight == 'M' and bottomLeft == 'S') or (topRight == 'S' and bottomLeft == 'M')):
            return True
    return False

def count(data):
    return sum(
        1
        for row, col in itertools.product(range(rows), range(cols))
        if find_X_MAS(data, row, col)
    )

print(count(data))