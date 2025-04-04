from time import time

time_start = time()
# INPUT_FILE = "./SummerAtTheLab2024/data/q02_test.txt"
INPUT_FILE = "./SummerAtTheLab2024/data/q02.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = sum(i for i, x in enumerate(data, start=1) if x == "TRUE")
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
for i in range(0, len(data), 4):
    if data[i] == "TRUE" and data[i + 1] == "TRUE":
        ans2 += 1
for i in range(2, len(data), 4):
    if data[i] == "TRUE" or data[i + 1] == "TRUE":
        ans2 += 1
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

ans3 = data.count("TRUE")
while len(data) > 1:
    data_new = []
    for i in range(0, len(data), 2):
        if i % 4 == 0:
            if data[i] == "TRUE" and data[i + 1] == "TRUE":
                data_new.append("TRUE")
            else:
                data_new.append("FALSE")
        else:
            if data[i] == "TRUE" or data[i + 1] == "TRUE":
                data_new.append("TRUE")
            else:
                data_new.append("FALSE")
    data = data_new
    ans3 += data.count("TRUE")
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
