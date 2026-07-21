class BSTNode:
    """
    Represents a node in the Binary Search Tree.
    """

    def __init__(self, city):
        self.city = city
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree for storing City objects.
    """

    def __init__(self):
        self.root = None

    def insert(self, city):
        """
        Insert a city into the BST.
        """
        if self.root is None:
            self.root = BSTNode(city)
        else:
            self._insert_recursive(self.root, city)

    def _insert_recursive(self, current_node, city):

        if city.name < current_node.city.name:

            if current_node.left is None:
                current_node.left = BSTNode(city)
            else:
                self._insert_recursive(current_node.left, city)

        elif city.name > current_node.city.name:

            if current_node.right is None:
                current_node.right = BSTNode(city)
            else:
                self._insert_recursive(current_node.right, city)

        # Ignore duplicate city names

    def search(self, city_name):
        """
        Search for a city by name.
        """
        return self._search_recursive(self.root, city_name)

    def _search_recursive(self, current_node, city_name):

        if current_node is None:
            return None

        if city_name == current_node.city.name:
            return current_node.city

        if city_name < current_node.city.name:
            return self._search_recursive(current_node.left, city_name)

        return self._search_recursive(current_node.right, city_name)

    def inorder_traversal(self):
        """
        Display cities in alphabetical order.
        """
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):

        if current_node is not None:
            self._inorder_recursive(current_node.left)
            print(current_node.city)
            self._inorder_recursive(current_node.right)
def delete(self, city_name):
    """Delete a city from the BST."""
    self.root = self._delete_recursive(self.root, city_name)
def _delete_recursive(self, node, city_name):

    if node is None:
        return node

    if city_name < node.city.name:
        node.left = self._delete_recursive(node.left, city_name)

    elif city_name > node.city.name:
        node.right = self._delete_recursive(node.right, city_name)

    else:

        # Case 1 & 2
        if node.left is None:
            return node.right

        if node.right is None:
            return node.left

        # Case 3
        successor = self._find_min(node.right)
        node.city = successor.city
        node.right = self._delete_recursive(
            node.right,
            successor.city.name
        )

    return node
def _find_min(self, node):

    current = node

    while current.left is not None:
        current = current.left

    return current