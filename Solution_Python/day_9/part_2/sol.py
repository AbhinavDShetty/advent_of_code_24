with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_9\\input.txt") as f:
    data = f.read()

    
files_spaces = []
for i, d in enumerate(data):
    if i%2:
        files_spaces.extend(["."]*int(d))
    else:
        proI = str(i//2)
        files_spaces.append((proI, )*int(d))
# print(files_spaces)
j = len(files_spaces) - 1
# while not isinstance(files_spaces[j], tuple):
#     j-=1

while j>=0:
    idx1 = 0
    length = 0
    total_length = len(files_spaces[j])
    for i in range(j):
        if files_spaces[i] == ".":
            if length == 0:
                idx1 = i
                length = 1
            else:
                length+=1
            if length>=total_length:
                tup = files_spaces[j]
                files_spaces.pop(j)
                for _ in range(length):
                    files_spaces.insert(j, ".")
                for _ in range(length):
                    files_spaces.pop(idx1)
                files_spaces.insert(idx1, tup)
                length = 0
                break
        else:
            length = 0
    j-=1
    # while j>=0 and not isinstance(files_spaces[j], tuple):
    #     j-=1
    
final_files_spaces = []
for elements in files_spaces:
    if isinstance(elements, tuple):
        final_files_spaces.extend(elements)
    else:
        final_files_spaces.append(elements)

total_sum = 0
for en, num in enumerate(final_files_spaces):
    if num.isdigit(): total_sum+=int(num)*en
    
print(total_sum)


# i = files_space.index(".")
# j = len(files_space)-1

# while i<j:
#     files_space[i], files_space[j] = files_space[j], files_space[i]
#     i+=1
#     j-=1
#     while files_space[i]!=".":
#         i+=1
#     while not files_space[j].isdigit():
#         j-=1


# total_sum = sum(int(block) * i for i, block in enumerate(files_space) if block.isdigit())
    
# print(total_sum)