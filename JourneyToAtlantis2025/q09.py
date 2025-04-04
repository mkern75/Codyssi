from collections import defaultdict
from time import time
import re

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q09.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

balance_initial = {}
for line in blocks[0]:
    name, value = line.split(" HAS ")
    balance_initial[name] = int(value)

transactions = []
for line in blocks[1]:
    x = re.match(r"FROM (.*) TO (.*) AMT (\d*)", line)
    transactions += [(x.groups()[0], x.groups()[1], int(x.groups()[2]))]

balance = dict(balance_initial)
for name1, name2, amount in transactions:
    balance[name1] -= amount
    balance[name2] += amount
ans1 = sum(sorted(balance.values(), reverse=True)[:3])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

balance = dict(balance_initial)
for name1, name2, amount in transactions:
    amount = min(amount, balance[name1])
    balance[name1] -= amount
    balance[name2] += amount
ans2 = sum(sorted(balance.values(), reverse=True)[:3])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")


def repay(balance, debt):
    stop = False
    while not stop:
        stop = True
        for name, balance_value in balance.items():
            if balance_value > 0 and debt[name]:
                stop = False
                name_other, debt_value = debt[name][0]
                repayment = min(balance_value, debt_value)
                balance[name] -= repayment
                balance[name_other] += repayment
                debt[name][0][1] -= repayment
                if debt[name][0][1] == 0:
                    del debt[name][0]


balance = dict(balance_initial)
debt = defaultdict(list)
for name1, name2, amount in transactions:
    amount, debt_amount = min(amount, balance[name1]), max(0, amount - balance[name1])
    balance[name1] -= amount
    balance[name2] += amount
    if debt_amount > 0:
        debt[name1] += [[name2, debt_amount]]
    repay(balance, debt)
ans3 = sum(sorted(balance.values(), reverse=True)[:3])
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
