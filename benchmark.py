import time


def benchmark_search(structure, search_function, city_name):
    start = time.perf_counter()

    search_function(city_name)

    end = time.perf_counter()

    print(f"{structure}: {(end - start) * 1000000:.2f} microseconds")