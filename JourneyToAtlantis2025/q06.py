from time import time


def is_normal(c):
    return c.isalpha()


def value(c):
    if "a" <= c <= "z":
        return ord(c) - ord("a") + 1
    if "A" <= c <= "Z":
        return ord(c) - ord("A") + 27
    return 0


time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q06.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
data_log = data[0]

normal = [c for c in data_log if is_normal(c)]
ans1 = len(normal)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = sum(value(c) for c in normal)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

values = []
for c in data_log:
    if is_normal(c):
        values += [value(c)]
    else:
        values += [(values[-1] * 2 - 5 - 1) % 52 + 1]
ans3 = sum(values)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
