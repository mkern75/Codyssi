from time import time

time_start = time()
INPUT_FILE = "./SummerAtTheLab2024/data/q03.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ABC = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#"

readings = []
for line in data:
    reading, base = line.split()
    readings += [(reading, int(base))]

ans1 = sum(x[1] for x in readings)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
for reading, base in readings:
    ans2 += int(reading, base)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

val, digits = ans2, []
while val:
    digits += [ABC[val % 65]]
    val //= 65
ans3 = "".join(reversed(digits))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
