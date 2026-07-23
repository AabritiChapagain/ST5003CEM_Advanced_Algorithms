import threading


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


class ThreadStats:
    """
    Shared counters updated from multiple worker threads.

    This is the CRITICAL SECTION of the program: 'threads_created' and
    'peak_concurrent' are read-modify-written by many threads at once, so
    every access is guarded by 'self.lock' (a mutex). Without the lock,
    concurrent '+= 1' operations on a plain int are not guaranteed atomic
    in general and could lose updates (a classic race condition).
    """

    def __init__(self):
        self.lock = threading.Lock()
        self.threads_created = 0
        self.active = 0
        self.peak_concurrent = 0

    def on_thread_start(self):
        with self.lock:                      # enter critical section
            self.threads_created += 1
            self.active += 1
            self.peak_concurrent = max(self.peak_concurrent, self.active)

    def on_thread_end(self):
        with self.lock:                      # enter critical section
            self.active -= 1


def parallel_merge_sort(arr, max_threads=4, stats=None, _pool=None):
    """
    Divide-and-conquer merge sort parallelised with a BOUNDED thread pool.

    Concurrency control:
        A threading.Semaphore initialised to 'max_threads' bounds how many
        worker threads may be actively running sort work at the same
        time. Each recursive call attempts to acquire the semaphore
        (non-blocking) before spawning a new OS thread for the left half;
        if the pool is already saturated it falls back to doing that half
        on the CURRENT thread instead of spawning an unbounded number of
        threads. This fixes the earlier version, which spawned a new
        thread pair at every recursion level (e.g. 14 threads for a
        'threads=8' request) and therefore measured thread-creation
        overhead rather than real parallel speedup.

    Thread safety:
        'stats' (a ThreadStats instance) is shared, mutable state written
        by every worker thread. All access to it goes through
        'stats.lock' (see ThreadStats above) -- this is the mutex-based
        synchronisation required for correctness.
    """
    if stats is None:
        stats = ThreadStats()
    if _pool is None:
        _pool = threading.Semaphore(max_threads)

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Try to claim a pool slot for a NEW thread without blocking.
    acquired = _pool.acquire(blocking=False)

    if not acquired:
        # Pool saturated: do both halves on the current thread (no new
        # OS thread is created, so no semaphore release is owed either).
        left_result = parallel_merge_sort(left_half, max_threads, stats, _pool)
        right_result = parallel_merge_sort(right_half, max_threads, stats, _pool)
        return merge(left_result, right_result)

    left_result = []

    def sort_left():
        stats.on_thread_start()
        try:
            left_result.extend(
                parallel_merge_sort(left_half, max_threads, stats, _pool)
            )
        finally:
            stats.on_thread_end()
            _pool.release()  # give the slot back to the pool

    worker = threading.Thread(target=sort_left)
    worker.start()

    # Right half is done on the current (already-counted) thread.
    right_result = parallel_merge_sort(right_half, max_threads, stats, _pool)

    worker.join()

    return merge(left_result, right_result)


if __name__ == "__main__":

    numbers = [8, 3, 6, 2, 9, 1, 5, 7, 4]

    print("Original:")
    print(numbers)

    print("\nSequential:")
    print(sequential_merge_sort(numbers))

    stats = ThreadStats()
    print("\nParallel (max_threads=4):")
    print(parallel_merge_sort(numbers, max_threads=4, stats=stats))
    print(f"Worker threads created: {stats.threads_created}")
    print(f"Peak concurrent worker threads: {stats.peak_concurrent}")
