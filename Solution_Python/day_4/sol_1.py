with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_4\\input.txt", "r") as f:
    data_raw = f.read().split("\n")
data = [list(row) for row in data_raw]

def find_XMAS(data):
    word = "XMAS"
    rows, cols = len(data), len(data[0])
    word_len = len(word)
    
    directions = [
        [0,1],
        [0,-1],
        [1,0],
        [-1,0],
        [1,1],
        [1,-1],
        [-1,1],
        [-1,-1]
    ]
    
    def search(X, Y, direction):
        dirX , dirY = direction
        for i in range(word_len):
            newX, newY = X + (i * dirX), Y + (i * dirY)
            if newX < 0 or newX >= rows or newY < 0 or newY >= cols or data[newX][newY] != word[i]:
                return False
        return True
    
    count = 0
    for row in range(rows):
        for col in range(cols):
            for direction in directions:
                if search(row, col, direction):
                    count += 1
    return count

print(find_XMAS(data))