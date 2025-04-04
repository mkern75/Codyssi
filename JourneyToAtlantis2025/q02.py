from time import time
import re

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q02.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def apply(func, x):
    res = re.findall(r"Function [ABC]: RAISE TO THE POWER OF (\d+)", func)
    if res:
        return x ** int(res[0])
    res = re.findall(r"Function [ABC]: MULTIPLY (\d+)", func)
    if res:
        return x * int(res[0])
    res = re.findall(r"Function [ABC]: ADD (\d+)", func)
    if res:
        return x + int(res[0])
    assert False


function_a = data[0]
function_b = data[1]
function_c = data[2]
room_qualities = list(map(int, data[4:]))
n = len(room_qualities)

room_qualities.sort()
ans1 = room_qualities[n // 2]
ans1 = apply(function_c, ans1)
ans1 = apply(function_b, ans1)
ans1 = apply(function_a, ans1)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans1 = sum(x for x in room_qualities if x & 1 == 0)
ans1 = apply(function_c, ans1)
ans1 = apply(function_b, ans1)
ans1 = apply(function_a, ans1)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

max_price = 15000000000000
ans3 = 0
for x in room_qualities:
    y = apply(function_c, x)
    y = apply(function_b, y)
    y = apply(function_a, y)
    if y <= max_price:
        ans3 = x
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
