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