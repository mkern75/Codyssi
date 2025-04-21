from time import time
from math import lcm

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q18.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

DIM_X, DIM_Y, DIM_Z, DIM_A = 10, 15, 60, 3
DIM_YZA = DIM_Y * DIM_Z * DIM_A
DIM_ZA = DIM_Z * DIM_A
MX = DIM_X * DIM_Y * DIM_Z * DIM_A
MAX_SAFE_HITS = 3
DEBRIS_CYCLE = lcm(DIM_X, DIM_Y, DIM_Z, DIM_A)  # cycle is rather small


def idx(x, y, z, a):
    return x * DIM_YZA + y * DIM_ZA + z * DIM_A + a + 1


def idxr(pos):
    x, pos = divmod(pos, DIM_YZA)
    y, pos = divmod(pos, DIM_ZA)
    z, pos = divmod(pos, DIM_A)
    a = pos - 1
    return x, y, z, a


debris = [[0] * MX for _ in range(DEBRIS_CYCLE)]
for line in data:
    s = line.split()
    ss = s[2].split("+")
    fx, fy, fz, fa = int(ss[0][:-1]), int(ss[1][:-1]), int(ss[2][:-1]), int(ss[3][:-1])
    d, r = int(s[4]), int(s[7])
    vx, vy, vz, va = int(s[11][1:-1]), int(s[12][0:-1]), int(s[13][0:-1]), int(s[14][0:-1])
    for pos in range(MX):
        x, y, z, a = idxr(pos)
        if (fx * x + fy * y + fz * z + fa * a) % d == r:
            debris[0][idx(x, y, z, a)] += 1
            for t in range(1, DEBRIS_CYCLE):
                x = (x + vx) % DIM_X
                y = (y + vy) % DIM_Y
                z = (z + vz) % DIM_Z
                a = (a + va + 1) % DIM_A - 1
                debris[t][idx(x, y, z, a)] += 1

ans1 = sum(debris[0])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

start = idx(0, 0, 0, 0)
target = idx(DIM_X - 1, DIM_Y - 1, DIM_Z - 1, 0)
safe = [False] * MX
safe[start] = True
t = 0
while not safe[target]:
    t += 1

    safe_new = safe[:]
    for pos, ok in enumerate(safe):
        if not ok:
            continue
        x, y, z, a = idxr(pos)
        if x > 0:
            safe_new[idx(x - 1, y, z, a)] = True
        if x < DIM_X - 1:
            safe_new[idx(x + 1, y, z, a)] = True
        if y > 0:
            safe_new[idx(x, y - 1, z, a)] = True
        if y < DIM_Y - 1:
            safe_new[idx(x, y + 1, z, a)] = True
        if z > 0:
            safe_new[idx(x, y, z - 1, a)] = True
        if z < DIM_Z - 1:
            safe_new[idx(x, y, z + 1, a)] = True
    safe = safe_new

    for pos, debris_cnt in enumerate(debris[t % DEBRIS_CYCLE]):
        if debris_cnt:
            safe[pos] = False
    safe[start] = True

ans2 = t
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

hits = [MAX_SAFE_HITS + 1] * MX
hits[start] = 0
t = 0
while hits[target] > MAX_SAFE_HITS:
    t += 1

    hits_new = hits[:]
    for pos, hit_count in enumerate(hits):
        if hit_count > MAX_SAFE_HITS:
            continue
        x, y, z, a = idxr(pos)
        if x > 0:
            pos = idx(x - 1, y, z, a)
            hits_new[pos] = min(hits_new[pos], hit_count)
        if x < DIM_X - 1:
            pos = idx(x + 1, y, z, a)
            hits_new[pos] = min(hits_new[pos], hit_count)
        if y > 0:
            pos = idx(x, y - 1, z, a)
            hits_new[pos] = min(hits_new[pos], hit_count)
        if y < DIM_Y - 1:
            pos = idx(x, y + 1, z, a)
            hits_new[pos] = min(hits_new[pos], hit_count)
        if z > 0:
            pos = idx(x, y, z - 1, a)
            hits_new[pos] = min(hits_new[pos], hit_count)
        if z < DIM_Z - 1:
            pos = idx(x, y, z + 1, a)
            hits_new[pos] = min(hits_new[pos], hit_count)
    hits = hits_new

    for pos, debris_cnt in enumerate(debris[t % DEBRIS_CYCLE]):
        hits[pos] += debris_cnt
    hits[start] = 0

ans3 = t
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
