from time import time
from collections import namedtuple

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q14.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

Item = namedtuple("ITEM", "quality cost materials")
items = []
for line in data:
    x = line.replace(",", "").split()
    items += [Item(int(x[5]), int(x[8]), int(x[12]))]


def solve(COST_MAX):
    dp = [(0, 0) for _ in range(COST_MAX + 1)]  # dp[cost]: highest (quality, -materials) that can be achieved
    for item in items:
        for cost in range(COST_MAX, -1, -1):
            cost_new = cost + item.cost
            if cost_new <= COST_MAX:
                dp[cost_new] = max(dp[cost_new], (dp[cost][0] + item.quality, dp[cost][1] - item.materials))
    res = max(dp)
    return res[0] * - res[1]


items.sort(key=lambda item: (-item.quality, -item.cost))
ans1 = sum(item.materials for item in items[:5])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = solve(30)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = solve(300)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
