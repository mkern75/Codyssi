from time import time
from copy import deepcopy
from collections import deque
import operator

time_start = time()

MOD = 1073741824
OPS = {"ADD": operator.add, "SUB": operator.sub, "MULTIPLY": operator.mul}

INPUT_FILE = "./JourneyToAtlantis2025/data/q12.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]
grid_initial = [list(map(int, line.split())) for line in blocks[0]]
instructions_initial = [tuple(line.split()) for line in blocks[1]]
actions_initial = blocks[2]


def shift_update(instr, grid):
    n = len(grid)
    amount, applies_to = int(instr[4]), str(instr[1])
    if applies_to == "ROW":
        row = int(instr[2]) - 1
        tmp = [grid[row][(col - amount) % n] for col in range(n)]
        for col in range(n):
            grid[row][col] = tmp[col]
    elif applies_to == "COL":
        col = int(instr[2]) - 1
        tmp = [grid[(row - amount) % n][col] for row in range(n)]
        for row in range(n):
            grid[row][col] = tmp[row]


def change_update(instr, grid):
    n = len(grid)
    op, amount, applies_to = str(instr[0]), int(instr[1]), str(instr[2])
    if applies_to == "ALL":
        for row in range(n):
            for col in range(n):
                grid[row][col] = OPS[op](grid[row][col], amount) % MOD
    elif applies_to == "ROW":
        row = int(instr[3]) - 1
        for col in range(n):
            grid[row][col] = OPS[op](grid[row][col], amount) % MOD
    elif applies_to == "COL":
        col = int(instr[3]) - 1
        for row in range(n):
            grid[row][col] = OPS[op](grid[row][col], amount) % MOD


def update(instr, grid):
    op = str(instr[0])
    if op == "SHIFT":
        shift_update(instr, grid)
    elif op in ["ADD", "SUB", "MULTIPLY"]:
        change_update(instr, grid)


def max_sum_row_col(grid):
    res = 0
    n = len(grid)
    for row in range(n):
        res = max(res, sum(grid[row][col] for col in range(n)))
    for col in range(n):
        res = max(res, sum(grid[row][col] for row in range(n)))
    return res


grid = deepcopy(grid_initial)
instructions = deepcopy(instructions_initial)
for instr in instructions:
    update(instr, grid)
ans1 = max_sum_row_col(grid)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

grid = deepcopy(grid_initial)
instructions = deque(deepcopy(instructions_initial))
actions = deepcopy(actions_initial)
instr = None
for action in actions:
    if action == "TAKE":
        instr = instructions.popleft()
    elif action == "CYCLE":
        instructions.append(instr)
    else:
        update(instr, grid)
ans2 = max_sum_row_col(grid)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

grid = deepcopy(grid_initial)
instructions = deque(deepcopy(instructions_initial))
actions = deepcopy(actions_initial)
instr = None
done = False
while not done:
    for action in actions:
        if action == "TAKE":
            instr = instructions.popleft()
        elif action == "CYCLE":
            instructions.append(instr)
        else:
            update(instr, grid)
            if not instructions:
                done = True
                break
ans3 = max_sum_row_col(grid)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
