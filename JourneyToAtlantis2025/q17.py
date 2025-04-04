from time import time
from collections import defaultdict
import re

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q17.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

# read staircases, build set of states and map of directed, single steps
states = set()
steps = defaultdict(list)
start, end = (-1, -1), (-1, -1)
for line in blocks[0]:
    s = line.split()
    id, level_start, level_end, sid_from, sid_to = int(s[0][1:]), int(s[2]), int(s[4]), s[7], s[9]
    for level in range(level_start, level_end + 1):
        states.add((id, level))
        if level < level_end:
            steps[(id, level)] += [(id, level + 1)]
    if id == 1:
        start, end = (id, level_start), (id, level_end)
    else:
        id_from, id_to = int(sid_from[1:]), int(sid_to[1:])
        steps[(id_from, level_start)] += [(id, level_start)]
        steps[(id, level_end)] += [(id_to, level_end)]

# read moves
moves = set(map(int, re.findall(r"[-+]?\d+", blocks[1][0])))
max_move = max(moves)

# build map of all states that are reachable from a state in a full move
reachable_states = defaultdict(set)
for state in states:
    states_tmp = {state}
    for k in range(1, max_move + 1):
        states_tmp_new = set()
        for s in states_tmp:
            states_tmp_new.update(steps[s])
        states_tmp = states_tmp_new
        if k in moves:
            reachable_states[state].update(states_tmp)

# topological sort of states
n_states = len(states)
in_degree = defaultdict(int)
for lst in steps.values():
    for v in lst:
        in_degree[v] += 1
sorted_states = []
stack = [s for s in states if in_degree[s] == 0]
while stack:
    v = stack.pop()
    sorted_states += [v]
    for u in steps[v]:
        in_degree[u] -= 1
        if in_degree[u] == 0:
            stack += [u]
assert len(sorted_states) == n_states

dp = defaultdict(int)
dp[start] = 1
for i in range(0, end[1] + 1):
    state = (1, i)
    for reachable_state in reachable_states[state]:
        if reachable_state[0] == 1:
            dp[reachable_state] += dp[state]
ans1 = dp[end]
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

dp = defaultdict(int)
dp[end] = 1
for state in reversed(sorted_states):
    for reachable_state in reachable_states[state]:
        dp[state] += dp[reachable_state]
ans2 = dp[start]
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

target = 100000000000000000000000000000
path = [start]
while path[-1] != end:
    state = path[-1]
    reachable_states_sorted = sorted(reachable_states[state])
    path += [reachable_states_sorted[0]]
    for state_next in reachable_states_sorted:
        path[-1] = state_next
        if target - dp[state_next] <= 0:
            break
        target -= dp[state_next]
ans3 = "-".join(f"S{state[0]}_{state[1]}" for state in path)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
