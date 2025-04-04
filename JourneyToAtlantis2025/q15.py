from time import time
from collections import Counter

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q15.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

artifacts, codes = [], {}
for line in blocks[0]:
    code, value = line.split(" | ")
    value = int(value)
    artifacts += [value]
    codes[value] = code

root = []
level_sum = Counter()
for value in artifacts:
    node = root
    level = 1
    while node:
        node = node[1] if value < node[0] else node[2]
        level += 1
    node += [value, [], []]
    level_sum[level] += value
ans1 = max(level_sum.values()) * len(level_sum)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

new_value = 500_000
node, path = root, []
while node:
    path += [node[0]]
    node = node[1] if new_value < node[0] else node[2]
ans2 = "-".join([codes[v] for v in path])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

value1 = int(blocks[1][0].split(" | ")[1])
value2 = int(blocks[1][1].split(" | ")[1])
node = root
while True:
    if max(value1, value2) < node[0]:
        node = node[1]
    elif min(value1, value2) > node[0]:
        node = node[2]
    else:
        ans3 = codes[node[0]]
        break
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
