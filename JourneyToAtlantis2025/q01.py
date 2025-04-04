from time import time

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q01.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

offsets = [int(data[i]) for i in range(len(data) - 1)]
n = len(offsets)
signs = data[-1]

ans1 = offsets[0]
for i in range(n - 1):
    ans1 += +offsets[i + 1] if signs[i] == "+" else -offsets[i + 1]
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = offsets[0]
for i in range(n - 1):
    ans2 += +offsets[i + 1] if signs[-(i + 1)] == "+" else -offsets[i + 1]
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

offsets = []
for i in range(0, len(data) - 1, 2):
    offsets += [int(data[i]) * 10 + int(data[i + 1])]
n = len(offsets)
signs = data[-1]

ans3 = offsets[0]
for i in range(n - 1):
    ans3 += +offsets[i + 1] if signs[-(i + 1)] == "+" else -offsets[i + 1]
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
