"""
Optional comparison implementation using PROCESSES instead of threads.

Python's threading module is subject to the Global Interpreter Lock (GIL):
only one thread executes Python bytecode at a time, even on a multi-core
machine. For CPU-bound work like sorting, this means threading.Thread
gives concurrency (interleaving) but not true parallelism -- which is
exactly what parallel_merge_sort.py's benchmark shows (speedup < 1x).

multiprocessing sidesteps the GIL entirely by running each worker in its
own OS process with its own Python interpreter and memory space. This
file is not required by the brief (which asks for a threading library),
but it is useful evidence for the "Analyse scalability... identify and
explain overheads" discussion: it isolates whether the lack of speedup
is a flaw in the merge-sort logic or a fundamental property of
CPU-bound threading in Python.
"""

from multiprocessing import Pool


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sequential_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = sequential_merge_sort(arr[:mid])
    right = sequential_merge_sort(arr[mid:])
    return merge(left, right)


def _sort_chunk(chunk):
    """Top-level function (required for pickling by multiprocessing)."""
    return sequential_merge_sort(chunk)


def parallel_merge_sort_processes(arr, num_processes=4):
    """
    Splits arr into num_processes chunks, sorts each chunk in a SEPARATE
    OS PROCESS in parallel (via a process Pool), then merges the sorted
    chunks sequentially. This is coarser-grained than the threaded
    divide-and-conquer version, but avoids the GIL entirely for the
    sorting work itself.
    """
    if num_processes <= 1 or len(arr) <= 1:
        return sequential_merge_sort(arr)

    chunk_size = max(1, len(arr) // num_processes)
    chunks = [
        arr[i:i + chunk_size]
        for i in range(0, len(arr), chunk_size)
    ]

    with Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(_sort_chunk, chunks)

    # Merge the sorted chunks together (k-way merge via repeated pairwise merge)
    result = sorted_chunks[0]
    for chunk in sorted_chunks[1:]:
        result = merge(result, chunk)

    return result


if __name__ == "__main__":
    numbers = [8, 3, 6, 2, 9, 1, 5, 7, 4]
    print("Sequential:", sequential_merge_sort(numbers))
    print("Multiprocessing:", parallel_merge_sort_processes(numbers, num_processes=4))
