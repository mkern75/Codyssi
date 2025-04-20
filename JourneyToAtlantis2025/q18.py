from time import time

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q18.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

DIM_X, DIM_Y, DIM_Z, DIM_A = 10, 15, 60, 3
MX = DIM_X * DIM_Y * DIM_Z * DIM_A
MAX_SAFE_HITS = 3


def idx(x, y, z, a):
    return x * DIM_Y * DIM_Z * DIM_A + y * DIM_Z * DIM_A + z * DIM_A + a + 1


def idxr(pos):
    x, pos = divmod(pos, DIM_Y * DIM_Z * DIM_A)
    y, pos = divmod(pos, DIM_Z * DIM_A)
    z, pos = divmod(pos, DIM_A)
    a = pos - 1
    return x, y, z, a


debris_initial = []
dvx, dvy, dvz, dva = [], [], [], []
for line in data:
    s = line.split()
    t = s[2].split("+")
    fx, fy, fz, fa = int(t[0][:-1]), int(t[1][:-1]), int(t[2][:-1]), int(t[3][:-1])
    d, r = int(s[4]), int(s[7])
    vx, vy, vz, va = int(s[11][1:-1]), int(s[12][0:-1]), int(s[13][0:-1]), int(s[14][0:-1])
    for pos in range(MX):
        x, y, z, a = idxr(pos)
        if (fx * x + fy * y + fz * z + fa * a) % d == r:
            debris_initial.append(idx(x, y, z, a))
            dvx.append(vx)
            dvy.append(vy)
            dvz.append(vz)
            dva.append(va)

ans1 = len(debris_initial)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def move_debris(debris):
    for i, pos in enumerate(debris):
        x, y, z, a = idxr(pos)
        x = (x + dvx[i]) % DIM_X
        y = (y + dvy[i]) % DIM_Y
        z = (z + dvz[i]) % DIM_Z
        a = (a + dva[i] + 1) % DIM_A - 1
        debris[i] = idx(x, y, z, a)
    return debris


def calc_moves(safe: list[bool]) -> list[bool]:
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
    return safe_new


start = idx(0, 0, 0, 0)
target = idx(DIM_X - 1, DIM_Y - 1, DIM_Z - 1, 0)
debris = debris_initial[:]
safe = [False] * MX
safe[start] = True
t = 0
while not safe[target]:
    t += 1
    safe = calc_moves(safe)
    debris = move_debris(debris)
    for pos in debris:
        safe[pos] = False
    safe[start] = True
ans2 = t
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")


def calc_moves2(hits: list[int]) -> list[int]:
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
    return hits_new


debris = debris_initial[:]
hits = [MAX_SAFE_HITS + 1] * MX
hits[start] = 0
t = 0
while hits[target] > MAX_SAFE_HITS:
    t += 1
    hits = calc_moves2(hits)
    debris = move_debris(debris)
    for pos in debris:
        hits[pos] += 1
    hits[start] = 0
ans3 = t
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
