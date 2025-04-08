from time import time

overall_start = time()

for day in range(1, 19):
    day_start = time()
    exec(open(f"./JourneyToAtlantis2025/q{day:02d}.py").read())
    print(f"Day {day}: {time() - day_start:.3f}s")
    print()

print(f"total running time: {time() - overall_start:.3f}s")
