from time import time

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q07.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

freq = [int(x) for x in blocks[0]]
swaps = [tuple(map(lambda x: int(x) - 1, line.split("-"))) for line in blocks[1]]
test_index = int(blocks[2][0]) - 1
n = len(freq)
m = len(swaps)

fa = freq[:]
for x, y in swaps:
    fa[x], fa[y] = fa[y], fa[x]
ans1 = fa[test_index]
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

fb = freq[:]
for i in range(m):
    x, y, z = swaps[i][0], swaps[i][1], swaps[(i + 1) % m][0]
    fb[x], fb[y], fb[z] = fb[z], fb[x], fb[y]
ans2 = fb[test_index]
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

fc = freq[:]
for i in range(m):
    x, y = min(swaps[i]), max(swaps[i])
    d = min(y - x, n - y)
    for j in range(d):
        xx, yy = x + j, y + j
        fc[xx], fc[yy] = fc[yy], fc[xx]
ans3 = fc[test_index]
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
