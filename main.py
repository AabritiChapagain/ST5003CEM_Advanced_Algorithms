from city import City
from bst import BinarySearchTree
from avl import AVLTree


def main():

    bst = BinarySearchTree()
    avl = AVLTree()      # <-- Create the AVL tree here

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


if __name__ == "__main__":
    main()