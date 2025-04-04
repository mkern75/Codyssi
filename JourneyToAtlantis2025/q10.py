from time import time

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q10.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
grid = [list(map(int, line.split())) for line in data]
n = len(grid)

INF = 1 << 31

ans1 = INF
for r in range(n):
    ans1 = min(ans1, sum(grid[r][c] for c in range(n)))
for c in range(n):
    ans1 = min(ans1, sum(grid[r][c] for r in range(n)))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

dp = [[INF] * n for _ in range(n)]
dp[0][0] = grid[0][0]
for r in range(n):
    for c in range(n):
        if r > 0:
            dp[r][c] = min(dp[r][c], dp[r - 1][c] + grid[r][c])
        if c > 0:
            dp[r][c] = min(dp[r][c], dp[r][c - 1] + grid[r][c])
ans2 = dp[14][14]
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = dp[-1][-1]
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
