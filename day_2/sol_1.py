from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
with open(file_path, "r") as f: 
    data_raw = f.read() 

reports = [list(map(int,line.split())) for line in data_raw.strip().split("\n")]

def is_safe(report): 
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]
    increasing = all(0<diff<=3 for diff in differences)
    decreasing = all(-3<=diff<0 for diff in differences)
    return increasing or decreasing 

safe_report = sum(1 for report in reports if is_safe(report)); print(safe_report)