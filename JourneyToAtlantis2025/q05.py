from time import time
import re


def manhatten_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def calc_closest(x, y, coord):
    idx_min, dist_min = 0, manhatten_dist(x, y, coord[0][0], coord[0][1])
    for i, (x2, y2) in enumerate(coord):
        dist = manhatten_dist(x, y, x2, y2)
        if (dist < dist_min) or (dist == dist_min and x2 < coord[idx_min][0]) or (
                dist == dist_min and x2 == coord[idx_min][0] and y2 < coord[idx_min][1]):
            idx_min, dist_min = i, dist
    return idx_min, dist_min


time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q05.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
coord = [tuple(map(int, re.findall(r"[-+]?\d+", line))) for line in data]

mn = mx = manhatten_dist(0, 0, *coord[0])
for x, y in coord:
    d = manhatten_dist(0, 0, x, y)
    mn = min(mn, d)
    mx = max(mx, d)
ans1 = mx - mn
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

i_min, _ = calc_closest(0, 0, coord)
coord_remaining = coord[:i_min] + coord[i_min + 1:]
_, ans2 = calc_closest(*coord[i_min], coord_remaining)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = 0
x, y = 0, 0
while coord:
    i_min, dist_min = calc_closest(x, y, coord)
    ans3 += dist_min
    x, y = coord[i_min]
    del coord[i_min]
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
