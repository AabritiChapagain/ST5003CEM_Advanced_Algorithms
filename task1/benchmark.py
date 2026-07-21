import csv
import time
from task1.bst import BinarySearchTree
from task1.avl import AVLTree
from task1.hash_table import HashTable
from task1.min_heap import MinHeap
from city import City


def load_dataset(filename):
    """Load cities from a CSV file."""
    cities = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            city = City(
                row["Name"],
                float(row["X"]),
                float(row["Y"]),
                int(row["Population"]),
                float(row["Distance"])
            )
            cities.append(city)

    return cities


def benchmark_bst(cities):
    bst = BinarySearchTree()

    start = time.perf_counter()
    for city in cities:
        bst.insert(city)
    insert_time = time.perf_counter() - start

    start = time.perf_counter()
    for city in cities:
        bst.search(city.name)
    search_time = time.perf_counter() - start

    start = time.perf_counter()
    for city in cities:
        bst.delete(city.name)
    delete_time = time.perf_counter() - start

    return insert_time, search_time, delete_time


def benchmark_avl(cities):
    avl = AVLTree()

    start = time.perf_counter()
    for city in cities:
        avl.insert(city)
    insert_time = time.perf_counter() - start

    start = time.perf_counter()
    for city in cities:
        avl.search(city.name)
    search_time = time.perf_counter() - start

    start = time.perf_counter()
    for city in cities:
        avl.delete(city.name)
    delete_time = time.perf_counter() - start

    return insert_time, search_time, delete_time


def benchmark_hash(cities):
    table = HashTable(size=len(cities) * 2)

    start = time.perf_counter()
    for city in cities:
        table.insert(city)
    insert_time = time.perf_counter() - start

    start = time.perf_counter()
    for city in cities:
        table.search(city.name)
    search_time = time.perf_counter() - start

    start = time.perf_counter()
    for city in cities:
        table.delete(city.name)
    delete_time = time.perf_counter() - start

    return insert_time, search_time, delete_time


def benchmark_heap(cities):
    heap = MinHeap()

    start = time.perf_counter()
    for city in cities:
        heap.insert(city)
    insert_time = time.perf_counter() - start

    start = time.perf_counter()
    while heap.extract_min() is not None:
        pass
    extract_time = time.perf_counter() - start

    return insert_time, extract_time


def main():

    datasets = [
        ("data/cities_100.csv", 100),
        ("data/cities_1000.csv", 1000),
        ("data/cities_10000.csv", 10000)
    ]

    with open("task1/benchmark_results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Structure",
            "Dataset",
            "Insert(s)",
            "Search(s)",
            "Delete/Extract(s)"
        ])

        for filename, size in datasets:

            cities = load_dataset(filename)

            ins, sea, dele = benchmark_bst(cities)
            writer.writerow(["BST", size, ins, sea, dele])

            ins, sea, dele = benchmark_avl(cities)
            writer.writerow(["AVL", size, ins, sea, dele])

            ins, sea, dele = benchmark_hash(cities)
            writer.writerow(["Hash Table", size, ins, sea, dele])

            ins, ext = benchmark_heap(cities)
            writer.writerow(["Min Heap", size, ins, "-", ext])

    print("Benchmark completed!")
    print("Results saved to benchmark_results.csv")


if __name__ == "__main__":
    main()