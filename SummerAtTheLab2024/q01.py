from time import time

time_start = time()
INPUT_FILE = "./SummerAtTheLab2024/data/q01.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

prices = [int(line) for line in data]

ans1 = sum(prices)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = sum(sorted(prices)[:-20])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = sum(prices[0::2]) - sum(prices[1::2])
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
