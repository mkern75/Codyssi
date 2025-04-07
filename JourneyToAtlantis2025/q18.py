from time import time
from collections import defaultdict

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q18.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

DIM_X, DIM_Y, DIM_Z, DIM_A = 10, 15, 60, 3


def idx(x, y, z, a):
    return x * DIM_Y * DIM_Z * DIM_A + y * DIM_Z * DIM_A + z * DIM_A + a + 1


def idxr(v):
    x, v = divmod(v, DIM_Y * DIM_Z * DIM_A)
    y, v = divmod(v, DIM_Z * DIM_A)
    z, v = divmod(v, DIM_A)
    a = v - 1
    return x, y, z, a


rules = []
for line in data:
    s = line.split()
    t = s[2].split("+")
    fx, fy, fz, fa = int(t[0][:-1]), int(t[1][:-1]), int(t[2][:-1]), int(t[3][:-1])
    d, r = int(s[4]), int(s[7])
    vx, vy, vz, va = int(s[11][1:-1]), int(s[12][0:-1]), int(s[13][0:-1]), int(s[14][0:-1])
    rules += [(fx, fy, fz, fa, d, r, vx, vy, vz, va)]

debris_initial = []
velocity = []
for x in range(0, DIM_X):
    for y in range(0, DIM_Y):
        for z in range(0, DIM_Z):
            for a in range(-1, -1 + DIM_A):
                for fx, fy, fz, fa, d, r, vx, vy, vz, va in rules:
                    sm = fx * x + fy * y + fz * z + fa * a
                    if sm % d == r:
                        debris_initial.append(idx(x, y, z, a))
                        velocity.append((vx, vy, vz, va))

ans1 = len(debris_initial)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def move_debris(debris):
    debris_new = []
    for val1, (vx, vy, vz, va) in zip(debris, velocity):
        x, y, z, a = idxr(val1)
        xn = (x + vx) % DIM_X
        yn = (y + vy) % DIM_Y
        zn = (z + vz) % DIM_Z
        an = (a + va + 1) % DIM_A - 1
        debris_new.append(idx(xn, yn, zn, an))
    return debris_new


def calc_moves(safe):
    safe_new = safe.copy()
    for val in safe:
        x, y, z, a = idxr(val)
        if x > 0:
            safe_new.add(idx(x - 1, y, z, a))
        if x < DIM_X - 1:
            safe_new.add(idx(x + 1, y, z, a))
        if y > 0:
            safe_new.add(idx(x, y - 1, z, a))
        if y < DIM_Y - 1:
            safe_new.add(idx(x, y + 1, z, a))
        if z > 0:
            safe_new.add(idx(x, y, z - 1, a))
        if z < DIM_Z - 1:
            safe_new.add(idx(x, y, z + 1, a))
    return safe_new


start = idx(0, 0, 0, 0)
target = idx(DIM_X - 1, DIM_Y - 1, DIM_Z - 1, 0)
debris = debris_initial
safe = {start}
t = 0
while target not in safe:
    t += 1
    debris = move_debris(debris)
    safe = calc_moves(safe)
    safe.difference_update(debris)
    safe.add(start)
ans2 = t
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")


def calc_moves2(safe):
    safe_new = defaultdict(lambda: 4, safe)
    for val, hits in safe.items():
        x, y, z, a = idxr(val)
        if x > 0:
            safe_new[idx(x - 1, y, z, a)] = min(safe_new[idx(x - 1, y, z, a)], hits)
        if x < DIM_X - 1:
            safe_new[idx(x + 1, y, z, a)] = min(safe_new[idx(x + 1, y, z, a)], hits)
        if y > 0:
            safe_new[idx(x, y - 1, z, a)] = min(safe_new[idx(x, y - 1, z, a)], hits)
        if y < DIM_Y - 1:
            safe_new[idx(x, y + 1, z, a)] = min(safe_new[idx(x, y + 1, z, a)], hits)
        if z > 0:
            safe_new[idx(x, y, z - 1, a)] = min(safe_new[idx(x, y, z - 1, a)], hits)
        if z < DIM_Z - 1:
            safe_new[idx(x, y, z + 1, a)] = min(safe_new[idx(x, y, z + 1, a)], hits)
    return safe_new


debris = debris_initial
safe = defaultdict(lambda: 4)
safe[start] = 0
t = 0
while target not in safe:
    t += 1
    debris = move_debris(debris)
    safe_new = calc_moves2(safe)
    for pos in debris:
        if pos in safe_new:
            safe_new[pos] += 1
    safe_new[start] = 0
    safe = defaultdict(lambda: 4, {k: v for k, v in safe_new.items() if v <= 3})
ans3 = t
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")