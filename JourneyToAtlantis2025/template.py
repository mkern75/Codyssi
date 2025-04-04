from time import time

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q1x_test.txt"
# INPUT_FILE = "./JourneyToAtlantis2025/data/q1x.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans1 = 0
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = 0
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
