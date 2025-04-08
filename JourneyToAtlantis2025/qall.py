from time import time

overall_start = time()

for day in range(1, 19):
    print(f"Day {day}")
    exec(open(f"./JourneyToAtlantis2025/q{day:02d}.py").read())
    print(f"running time so far: {time() - overall_start:.3f}s")
    print()

print(f"total running time: {time() - overall_start:.3f}s")
