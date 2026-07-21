import random
import time
import csv

from parallel_merge_sort import (
    sequential_merge_sort,
    parallel_merge_sort
)


SIZE = 100000

numbers = [random.randint(1, 1000000) for _ in range(SIZE)]


# Sequential benchmark
start = time.perf_counter()
sequential_merge_sort(numbers.copy())
sequential_time = time.perf_counter() - start

results = []

for threads in [1, 2, 4, 8]:

    start = time.perf_counter()

    if threads == 1:
        sequential_merge_sort(numbers.copy())
    else:
        parallel_merge_sort(numbers.copy(), threads)

    elapsed = time.perf_counter() - start

    speedup = sequential_time / elapsed

    results.append([threads, elapsed, speedup])

    print(
        f"Threads: {threads} | "
        f"Time: {elapsed:.4f}s | "
        f"Speedup: {speedup:.2f}x"
    )


with open("task5/thread_benchmark.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Threads",
        "Time",
        "Speedup"
    ])

    writer.writerows(results)

print("\nBenchmark complete!")
print("Results saved to task5/thread_benchmark.csv")
