from time import time
from math import prod

time_start = time()
INPUT_FILE = "./JourneyToAtlantis2025/data/q16.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

N = 80
instrunctions = [tuple(line.split()) for line in blocks[0]]
twists = list(blocks[1][0])


class V3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def twist_l(self):
        self.x, self.z = self.z, -self.x

    def twist_r(self):
        self.x, self.z = -self.z, self.x

    def twist_d(self):
        self.y, self.z = self.z, -self.y

    def twist_u(self):
        self.y, self.z = -self.z, self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Face:
    def __init__(self, point: V3D, direction: V3D, n):
        self.point = point
        self.direction = direction
        self.n = n
        self.grid = [[1] * n for _ in range(n)]
        self.absorption = 0

    def normalise(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.grid[r][c] > 100:
                    self.grid[r][c] -= 100

    def apply_face(self, value):
        self.absorption += value * self.n * self.n
        for r in range(self.n):
            for c in range(self.n):
                self.grid[r][c] += value
        self.normalise()

    def apply_row(self, row, value):
        self.absorption += value * self.n
        if self.direction.y == +1:
            for c in range(self.n):
                self.grid[row][c] += value
        elif self.direction.y == -1:
            for c in range(self.n):
                self.grid[self.n - 1 - row][c] += value
        elif self.direction.x == +1:
            for r in range(self.n):
                self.grid[r][row] += value
        elif self.direction.x == -1:
            for r in range(self.n):
                self.grid[r][self.n - 1 - row] += value
        self.normalise()

    def apply_col(self, col, value):
        self.absorption += value * self.n
        if self.direction.y == +1:
            for r in range(self.n):
                self.grid[r][col] += value
        elif self.direction.y == -1:
            for r in range(self.n):
                self.grid[r][self.n - 1 - col] += value
        elif self.direction.x == +1:
            for c in range(self.n):
                self.grid[self.n - 1 - col][c] += value
        elif self.direction.x == -1:
            for c in range(self.n):
                self.grid[col][c] += value
        self.normalise()

    def exec_twist(self, twist):
        if twist == "L":
            self.point.twist_l()
            self.direction.twist_l()
        elif twist == "R":
            self.point.twist_r()
            self.direction.twist_r()
        elif twist == "U":
            self.point.twist_u()
            self.direction.twist_u()
        elif twist == "D":
            self.point.twist_d()
            self.direction.twist_d()

    def dominant_sum(self):
        res = 0
        for r in range(self.n):
            res = max(res, sum(self.grid[r][c] for c in range(N)))
        for c in range(self.n):
            res = max(res, sum(self.grid[r][c] for r in range(N)))
        return res


class Cube:
    def __init__(self, n):
        self.n = n
        self.faces = []
        self.faces += [Face(V3D(0, 0, +1), V3D(0, +1, 0), n)]  # top
        self.faces += [Face(V3D(0, 0, -1), V3D(0, -1, 0), n)]  # bottom
        self.faces += [Face(V3D(-1, 0, 0), V3D(0, 0, +1), n)]  # left
        self.faces += [Face(V3D(+1, 0, 0), V3D(0, 0, -1), n)]  # right
        self.faces += [Face(V3D(0, -1, 0), V3D(0, 0, +1), n)]  # front
        self.faces += [Face(V3D(0, +1, 0), V3D(0, 0, -1), n)]  # back

    def current_face(self):
        return next(face for face in self.faces if face.point == V3D(0, 0, 1))

    def exec_twist(self, twist):
        for face in self.faces:
            face.exec_twist(twist)

    def exec_instruction(self, instruction):
        if instruction[0] == "FACE":
            value = int(instruction[3])
            self.current_face().apply_face(value)
        elif instruction[0] == "ROW":
            value = int(instruction[4])
            row = int(instruction[1]) - 1
            self.current_face().apply_row(row, value)
        elif instruction[0] == "COL":
            value = int(instruction[4])
            col = int(instruction[1]) - 1
            self.current_face().apply_col(col, value)

    def exec_instruction2(self, instruction):
        if instruction[0] == "FACE":
            value = int(instruction[3])
            self.current_face().apply_face(value)
        elif instruction[0] == "ROW":
            row = int(instruction[1]) - 1
            value = int(instruction[4])
            for _ in range(4):
                self.current_face().apply_row(row, value)
                self.exec_twist("L")
        elif instruction[0] == "COL":
            col = int(instruction[1]) - 1
            value = int(instruction[4])
            for _ in range(4):
                self.current_face().apply_col(col, value)
                self.exec_twist("U")


cube = Cube(N)
for instruction, twist in zip(instrunctions, twists):
    cube.exec_instruction(instruction)
    cube.exec_twist(twist)
cube.exec_instruction(instrunctions[-1])
absorptions = sorted(face.absorption for face in cube.faces)
ans1 = absorptions[-1] * absorptions[-2]
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = prod(face.dominant_sum() for face in cube.faces)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

cube = Cube(N)
for instruction, twist in zip(instrunctions, twists):
    cube.exec_instruction2(instruction)
    cube.exec_twist(twist)
cube.exec_instruction2(instrunctions[-1])
ans3 = prod(face.dominant_sum() for face in cube.faces)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
