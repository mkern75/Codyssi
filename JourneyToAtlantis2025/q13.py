from time import time
from collections import defaultdict
from math import prod

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q13.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

idx = defaultdict(lambda: len(idx))
adj = defaultdict(list)
for line in data:
    locs, dist = line.split(" | ")
    start, end = locs.split(" -> ")
    adj[idx[start]] += [(idx[end], int(dist))]
n = len(idx)
start_node = idx["STT"]


class Dijkstra:
    def __init__(self, n):
        assert 2 <= n
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.dist = [float("inf")] * n
        self.prev = [-1] * n

    def add_edge(self, frm, to, weight):
        assert 0 <= frm < self.n and 0 <= to < self.n and 0 <= weight
        self.adj[frm] += [(to, weight)]

    def solve(self, start):
        import heapq
        assert 0 <= start < self.n
        self.dist[start] = 0
        queue = []
        heapq.heappush(queue, (0, start))
        while queue:
            d, v = heapq.heappop(queue)
            if d == self.dist[v]:
                for u, w in self.adj[v]:
                    if d + w < self.dist[u]:
                        self.dist[u] = d + w
                        self.prev[u] = v
                        heapq.heappush(queue, (d + w, u))


dijkstra = Dijkstra(n)
for node, neighbour_nodes in adj.items():
    for neighbour_node, _ in neighbour_nodes:
        dijkstra.add_edge(node, neighbour_node, 1)
dijkstra.solve(idx["STT"])
ans1 = prod(sorted(dijkstra.dist[:])[-3:])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

dijkstra = Dijkstra(n)
for node, neighbour_nodes in adj.items():
    for neighbour_node, path_length in neighbour_nodes:
        dijkstra.add_edge(node, neighbour_node, path_length)
dijkstra.solve(idx["STT"])
ans2 = prod(sorted(dijkstra.dist[:])[-3:])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")


def longest_cycle(cycle_start_node, current_node, visited, length_so_far):
    res = 0
    for next_node, path_length in adj[current_node]:
        if next_node == cycle_start_node:
            res = max(res, length_so_far + path_length)
        elif next_node == start_node or next_node in visited:
            continue
        else:
            res = max(res,
                      longest_cycle(cycle_start_node, next_node, visited | {next_node}, length_so_far + path_length))
    return res


ans3 = 0
for node in range(n):
    ans3 = max(ans3, longest_cycle(node, node, {node}, 0))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
