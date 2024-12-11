from collections import Counter

def transform(stones, blinks):
    stone_counts = Counter(stones)
    for _ in range(blinks):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                left = int(str(stone)[:half])
                right = int(str(stone)[half:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        stone_counts = new_counts

    return sum(stone_counts.values())


with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_11\\input.txt") as f:
    numbers = [int(num) for num in f.read().split()]
    
blinks = 75
result = transform(numbers, blinks)
print(result)