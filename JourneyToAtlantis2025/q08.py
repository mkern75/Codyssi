from time import time

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q08.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def reduce_p2(l):
    for i in range(len(l)):
        if l[i].isdigit():
            if i > 0 and (l[i - 1].isalpha() or l[i - 1] == "-"):
                return reduce_p2(l[:i - 1] + l[i + 1:])
            if i + 1 < len(l) and (l[i + 1].isalpha() or l[i + 1] == "-"):
                return reduce_p2(l[:i] + l[i + 2:])
    return l


def reduce_p3(l):
    for i in range(len(l)):
        if l[i].isdigit():
            if i > 0 and l[i - 1].isalpha():
                return reduce_p3(l[:i - 1] + l[i + 1:])
            if i + 1 < len(l) and l[i + 1].isalpha():
                return reduce_p3(l[:i] + l[i + 2:])
    return l


ans1 = sum(int(c.isalpha()) for line in data for c in line)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = sum(len(reduce_p2(line)) for line in data)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = sum(len(reduce_p3(line)) for line in data)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")