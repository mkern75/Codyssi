from time import time

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q18.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

DIM_X, DIM_Y, DIM_Z, DIM_A = 10, 15, 60, 3
MX = DIM_X * DIM_Y * DIM_Z * DIM_A


def idx(x, y, z, a):
    return x * DIM_Y * DIM_Z * DIM_A + y * DIM_Z * DIM_A + z * DIM_A + a + 1



def idxr(pos):
    x, pos = divmod(pos, DIM_Y * DIM_Z * DIM_A)
    y, pos = divmod(pos, DIM_Z * DIM_A)
    z, pos = divmod(pos, DIM_A)
    a = pos - 1
    return x, y, z, a


rules = []
for line in data:
    s = line.split()
    t = s[2].split("+")
    fx, fy, fz, fa = int(t[0][:-1]), int(t[1][:-1]), int(t[2][:-1]), int(t[3][:-1])
    d, r = int(s[4]), int(s[7])
    vx, vy, vz, va = int(s[11][1:-1]), int(s[12][0:-1]), int(s[13][0:-1]), int(s[14][0:-1])
    rules += [(fx, fy, fz, fa, d, r, vx, vy, vz, va)]

dxi, dyi, dzi, dai, dvx, dvy, dvz, dva = [], [], [], [], [], [], [], []
for fx, fy, fz, fa, d, r, vx, vy, vz, va in rules:
    for a in range(-1, -1 + DIM_A):
        for x in range(0, DIM_X):
            for y in range(0, DIM_Y):
                for z in range(0, DIM_Z):
                    if (fx * x + fy * y + fz * z + fa * a) % d == r:
                        dxi.append(x)
                        dyi.append(y)
                        dzi.append(z)
                        dai.append(a)
                        dvx.append(vx)
                        dvy.append(vy)
                        dvz.append(vz)
                        dva.append(va)
n_debris = len(dxi)
ans1 = n_debris
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def move_debris(dx, dy, dz, da):
    for i in range(n_debris):
        dx[i] = (dx[i] + dvx[i]) % DIM_X
        dy[i] = (dy[i] + dvy[i]) % DIM_Y
        dz[i] = (dz[i] + dvz[i]) % DIM_Z
        da[i] = (da[i] + dva[i] + 1) % DIM_A - 1


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
dx, dy, dz, da = dxi[:], dyi[:], dzi[:], dai[:]
safe = [False] * MX
safe[start] = True
t = 0
while not safe[target]:
    t += 1
    safe = calc_moves(safe)
    move_debris(dx, dy, dz, da)
    for i in range(n_debris):
        safe[idx(dx[i], dy[i], dz[i], da[i])] = False
    safe[start] = True
ans2 = t
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")


def calc_moves2(safe: list[int]) -> list[int]:
    safe_new = safe[:]
    for val, hits in enumerate(safe):
        if hits >= 4:
            continue
        x, y, z, a = idxr(val)
        if x > 0:
            pos = idx(x - 1, y, z, a)
            safe_new[pos] = min(safe_new[pos], hits)
        if x < DIM_X - 1:
            pos = idx(x + 1, y, z, a)
            safe_new[pos] = min(safe_new[pos], hits)
        if y > 0:
            pos = idx(x, y - 1, z, a)
            safe_new[pos] = min(safe_new[pos], hits)
        if y < DIM_Y - 1:
            pos = idx(x, y + 1, z, a)
            safe_new[pos] = min(safe_new[pos], hits)
        if z > 0:
            pos = idx(x, y, z - 1, a)
            safe_new[pos] = min(safe_new[pos], hits)
        if z < DIM_Z - 1:
            pos = idx(x, y, z + 1, a)
            safe_new[pos] = min(safe_new[pos], hits)
    return safe_new


dx, dy, dz, da = dxi[:], dyi[:], dzi[:], dai[:]
safe = [4] * MX
safe[start] = 0
t = 0
while safe[target] >= 4:
    t += 1
    safe = calc_moves2(safe)
    move_debris(dx, dy, dz, da)
    for i in range(n_debris):
        safe[idx(dx[i], dy[i], dz[i], da[i])] += 1
    safe[start] = 0
ans3 = t
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
