from collections import defaultdict, deque
from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
with open(file_path, 'r') as f:
    data = f.read()



rules_raw, updates_raw = data.strip().split('\n\n')
rules = []
for rule in rules_raw.splitlines():
    x, y = map(int, rule.split('|'))
    rules.append((x, y))

updates = [list(map(int, update.split(','))) for update in updates_raw.splitlines()]


# Helper function to validate order
def is_correct_order(update, rules):
    indices = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in indices and y in indices and indices[x] > indices[y]:
            return False
    return True

# Helper function to reorder update based on rules
def reorder_update(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)
    
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sort
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

# Process updates
incorrect_updates_middle_pages = []

for update in updates:
    if not is_correct_order(update, rules):
        corrected_update = reorder_update(update, rules)
        middle_page = corrected_update[len(corrected_update) // 2]
        incorrect_updates_middle_pages.append(middle_page)

# Calculate the sum of middle pages
sum_middle_pages = sum(incorrect_updates_middle_pages)
print(sum_middle_pages)
