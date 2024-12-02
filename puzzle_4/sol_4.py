with open("C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\puzzle_4\\input.txt", "r") as f: 
    data_raw = f.read() 

reports = [list(map(int,line.split())) for line in data_raw.strip().split("\n")]

def is_safe(report): 
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]
    increasing = all(0<diff<=3 for diff in differences)
    decreasing = all(-3<=diff<0 for diff in differences)
    return increasing or decreasing 

def damper(report):
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    
    return False

safe_report = sum(1 for report in reports if damper(report))
print(safe_report)