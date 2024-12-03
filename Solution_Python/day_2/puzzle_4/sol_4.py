with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_2\\input.txt", "r") as f:
    data_raw = f.read().strip().split("\n")

reports = [list(map(int, line.split())) for line in data_raw]

def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]
    return all(0 < diff <= 3 for diff in differences) or all(-3 <= diff < 0 for diff in differences)

def damper(report):
    n = len(report)
    differences = [report[i+1] - report[i] for i in range(n-1)]

    if all(0 < diff <= 3 for diff in differences) or all(-3 <= diff < 0 for diff in differences):
        return True

    for i in range(n):
        if i == 0:
            new_diff = differences[1:]
        elif i == n-1:
            new_diff = differences[:-1]
        else:
            new_diff = differences[:i-1] + [report[i+1] - report[i-1]] + differences[i+1:]
        
        if all(0 < diff <= 3 for diff in new_diff) or all(-3 <= diff < 0 for diff in new_diff):
            return True
    
    return False

safe_report = sum(1 for report in reports if damper(report))
print(safe_report)