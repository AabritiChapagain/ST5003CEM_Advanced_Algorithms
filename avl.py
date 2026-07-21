from city import City


class AVLNode:
    """
    Represents a node in an AVL Tree.
    """

    def __init__(self, city):
        self.city = city
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    AVL Tree for storing City objects.
    """

    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):

        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        x.height = 1 + max(
            self.get_height(x.left),
            self.get_height(x.right)
        )

        return x

    def left_rotate(self, x):

        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(
            self.get_height(x.left),
            self.get_height(x.right)
        )

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        return y

    def insert(self, city):
        self.root = self._insert_recursive(self.root, city)

    def _insert_recursive(self, node, city):

        if node is None:
            return AVLNode(city)

        if city.name < node.city.name:
            node.left = self._insert_recursive(node.left, city)

        elif city.name > node.city.name:
            node.right = self._insert_recursive(node.right, city)

        else:
            return node

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

        balance = self.get_balance(node)

        # Left Left
        if balance > 1 and city.name < node.left.city.name:
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and city.name > node.right.city.name:
            return self.left_rotate(node)

        # Left Right
        if balance > 1 and city.name > node.left.city.name:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left
        if balance < -1 and city.name < node.right.city.name:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):

        if node is not None:
            self._inorder_recursive(node.left)
            print(node.city)
            self._inorder_recursive(node.right)