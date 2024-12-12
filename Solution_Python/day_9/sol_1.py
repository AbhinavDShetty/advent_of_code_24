with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_9\\input.txt") as f:
    data = f.read()

files_space = []
for i, num in enumerate(data):
    if i%2:
        files_space.extend(["."]*int(num))
    else:
        proI = str(i//2)
        files_space.extend([proI for _ in range(int(num))])
print(files_space)
        
i = files_space.index(".")
j = len(files_space)-1

while i<j:
    files_space[i], files_space[j] = files_space[j], files_space[i]
    i+=1
    j-=1
    while files_space[i]!=".":
        i+=1
    while not files_space[j].isdigit():
        j-=1

total_sum = 0
for i, block in enumerate(files_space):
    if block==".":
        break
    total_sum+=int(block)*i
    
print(total_sum)