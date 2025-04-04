from time import time
from collections import defaultdict

time_start = time()
INPUT_FILE = "./SummerAtTheLab2024/data/q04.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

adj = defaultdict(list)
for line in data:
    x, y = line.split(" <-> ")
    adj[x] += [y]
    adj[y] += [x]

ans1 = len(adj)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

distance = {"STT": 0}
queue = ["STT"]
for x in queue:
    for y in adj[x]:
        if y not in distance:
            distance[y] = distance[x] + 1
            queue += [y]
ans2 = sum(1 for dist in distance.values() if dist <= 3)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = sum(distance.values())
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
