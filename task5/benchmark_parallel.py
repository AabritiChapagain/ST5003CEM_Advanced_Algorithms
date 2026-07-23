import random
import time
import csv

from parallel_merge_sort import (
    sequential_merge_sort,
    parallel_merge_sort,
    ThreadStats,
)
from parallel_merge_sort_mp import parallel_merge_sort_processes


SIZE = 200_000
REPEATS = 3  # average over repeats to reduce timing noise


def timed_run(fn, *args, **kwargs):
    best = None
    for _ in range(REPEATS):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        if best is None or elapsed < best:
            best = elapsed
    return result, best


def main():
    numbers = [random.randint(1, 1_000_000) for _ in range(SIZE)]

    # --- Baseline: sequential ---
    seq_result, seq_time = timed_run(sequential_merge_sort, numbers.copy())
    assert seq_result == sorted(numbers), "Sequential sort is incorrect!"
    print(f"Sequential:        {seq_time:.4f}s")

    results = [["Implementation", "Workers", "Time(s)", "Speedup", "PeakConcurrency"]]
    results.append(["Sequential", 1, seq_time, 1.0, 1])

    # --- Threaded version (bounded thread pool) ---
    print("\n--- Threaded (bounded pool, GIL-limited for CPU work) ---")
    for workers in [1, 2, 4, 8]:
        stats = ThreadStats()
        result, elapsed = timed_run(
            parallel_merge_sort, numbers.copy(), max_threads=workers, stats=stats
        )
        assert result == sorted(numbers), f"Threaded sort incorrect at {workers} threads!"
        speedup = seq_time / elapsed
        print(
            f"Threads: {workers} | Time: {elapsed:.4f}s | "
            f"Speedup: {speedup:.2f}x | Peak concurrent threads: {stats.peak_concurrent}"
        )
        results.append(["Threaded", workers, elapsed, speedup, stats.peak_concurrent])

    # --- Multiprocessing version (bypasses the GIL) ---
    print("\n--- Multiprocessing (bypasses the GIL) ---")
    for workers in [1, 2, 4, 8]:
        result, elapsed = timed_run(
            parallel_merge_sort_processes, numbers.copy(), num_processes=workers
        )
        assert result == sorted(numbers), f"Multiprocessing sort incorrect at {workers} procs!"
        speedup = seq_time / elapsed
        print(
            f"Processes: {workers} | Time: {elapsed:.4f}s | Speedup: {speedup:.2f}x"
        )
        results.append(["Multiprocessing", workers, elapsed, speedup, workers])

    import os
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thread_benchmark.csv")
    with open(out_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(results)

    print(f"\nBenchmark complete! Results saved to {out_path}")


if __name__ == "__main__":
    main()
