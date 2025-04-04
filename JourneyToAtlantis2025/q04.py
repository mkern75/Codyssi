from time import time


def calc_memory_units(s):
    res = 0
    for c in s:
        if "A" <= c <= "Z":
            res += ord(c) - 64
        elif "0" <= c <= "9":
            res += ord(c) - 48
    return res


time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q04.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
for line in data:
    ans1 += calc_memory_units(line)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
for line in data:
    n = len(line)
    k = n // 10
    line_compressed = line[:k] + str(n - 2 * k) + line[-k:]
    ans2 += calc_memory_units(line_compressed)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = 0
for line in data:
    tmp = []
    for c in line:
        if not tmp or tmp[-1] != c:
            tmp += [1, c]
        else:
            tmp[-2] += 1
    line_compressed = "".join(map(str, tmp))
    ans3 += calc_memory_units(line_compressed)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
