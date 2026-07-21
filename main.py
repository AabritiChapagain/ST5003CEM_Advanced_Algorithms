from city import City
from bst import BinarySearchTree

def main():

    bst = BinarySearchTree()

    cities = [
        City("Kathmandu", 27.7172, 85.3240, 1500000, 0),
        City("Pokhara", 28.2096, 83.9856, 518000, 200),
        City("Biratnagar", 26.4525, 87.2718, 242000, 390),
        City("Lalitpur", 27.6644, 85.3188, 299000, 5)
    ]
    # Insert cities into the BST
    for city in cities:
      bst.insert(city)

    print("=== BST Search ===")

    result = bst.search("Pokhara")

    if result:
        print("City Found:")
        print(result)
    else:
        print("City not found.")

    print("\n=== Cities in Alphabetical Order ===")
    bst.inorder_traversal()

    print("\nDeleting Pokhara...\n")
    bst.delete("Pokhara")
    print("Cities after deletion:\n")
    bst.inorder_traversal()

if __name__ == "__main__":
    main()