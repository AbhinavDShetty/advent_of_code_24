with open('C:\\Users\\deepa\\OneDrive\\Documents\\GitHub\\advent_of_code_24\\Solution_Python\\day_5\\input.txt', 'r') as f:
    data = f.read()


def input(data):
    rules_raw, updates_raw = data.strip().split('\n\n')
    rules = []
    for rule in rules_raw.splitlines():
        x, y = map(int, rule.split('|'))
        rules.append((x, y))

    updates = [list(map(int, update.split(','))) for update in updates_raw.splitlines()]
    return rules, updates


def correct_updates(rules, update):
    dic = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in dic and y in dic:
            if dic[y] < dic[x]:
                return False
    return True


rules, updates = input(data)
mid_sum = 0
for update in updates:
    if correct_updates(rules, update):
        mid_sum += update[len(update) // 2]

print(mid_sum)