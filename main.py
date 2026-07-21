from city import City
from bst import BinarySearchTree
from avl import AVLTree
from hash_table import HashTable
from min_heap import MinHeap
from benchmark import benchmark_search

def main():

    bst = BinarySearchTree()
    avl = AVLTree()
    hash_table = HashTable()
    heap = MinHeap()

    cities = [
        City("Kathmandu", 27.7172, 85.3240, 1500000, 0),
        City("Pokhara", 28.2096, 83.9856, 518000, 200),
        City("Biratnagar", 26.4525, 87.2718, 242000, 390),
        City("Lalitpur", 27.6644, 85.3188, 299000, 5)
    ]

    # BST
    for city in cities:
        bst.insert(city)

    print("=== BST Search ===")
    result = bst.search("Pokhara")

    if result:
        print(result)

    print("\nBST Inorder:")
    bst.inorder_traversal()

    # AVL
    print("\n==========================")
    print("Testing AVL Tree")
    print("==========================")

    for city in cities:
        avl.insert(city)

    avl.inorder_traversal()

    print("\nSearching in AVL Tree...")

    result = avl.search("Pokhara")

    if result:
        print("City Found:")
        print(result)
    else:
        print("City not found.")

    # Hash Table
    print("\n==========================")
    print("Testing Hash Table")
    print("==========================")

    for city in cities:
        hash_table.insert(city)

    result = hash_table.search("Pokhara")

    if result:
        print("City Found:")
        print(result)
    else:
        print("City not found.")

    print("\nDeleting Pokhara...\n")

    hash_table.delete("Pokhara")

    print("Hash Table after deletion:")

    hash_table.display()
    
    print("\n==========================")
    print("Testing Min Heap")
    print("==========================")

    heap.display()
    for city in cities:
        heap.insert(city)
    print("\nNearest city:")

    nearest = heap.extract_min()

    if nearest:
        print(nearest)
    print("\n==========================")
    print("Benchmark Results")
    print("==========================")

    benchmark_search(
        "Binary Search Tree",
        bst.search,
        "Pokhara"
    )

    benchmark_search(
        "AVL Tree",
        avl.search,
        "Pokhara"
    )

    benchmark_search(
        "Hash Table",
        hash_table.search,
        "Pokhara"
    )
if __name__ == "__main__":
    main()