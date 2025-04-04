from time import time
import re

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q03.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
for line in data:
    a, b, c, d = map(int, re.findall(r"\d+", line))
    ans1 += (b - a + 1) + (d - c + 1)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
for line in data:
    a, b, c, d = map(int, re.findall(r"\d+", line))
    if b < c or d < a:
        ans2 += (b - a + 1) + (d - c + 1)
    else:
        ans2 += max(b, d) - min(a, c) + 1
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = 0
for i in range(len(data) - 1):
    a1, b1, c1, d1 = map(int, re.findall(r"\d+", data[i]))
    a2, b2, c2, d2 = map(int, re.findall(r"\d+", data[i + 1]))
    seg = [[a1, b1], [c1, d1], [a2, b2], [c2, d2]]
    seg.sort()
    seg2 = [seg[0]]
    for [x, y] in seg[1:]:
        if x <= seg2[-1][1]:
            seg2[-1][1] = max(seg2[-1][1], y)
        else:
            seg2 += [[x, y]]
    res = sum(y - x + 1 for x, y in seg2)
    ans3 = max(ans3, res)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
