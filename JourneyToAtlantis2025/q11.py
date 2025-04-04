from time import time

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q11.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ABC = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^"


def from_base(number: str, base: int) -> int:
    res = 0
    for c in number:
        res = res * base + ABC.index(c)
    return res


def to_base(number: int, base: int) -> str:
    res = []
    while number:
        res += [ABC[number % base]]
        number //= base
    return "".join(reversed(res))


numbers = []
for line in data:
    number, base = line.split()
    base = int(base)
    numbers += [from_base(number, base)]
sum_numbers = sum(numbers)

ans1 = max(numbers)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = to_base(sum_numbers, 68)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = 2
while ans3 ** 4 <= sum_numbers:
    ans3 += 1
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
