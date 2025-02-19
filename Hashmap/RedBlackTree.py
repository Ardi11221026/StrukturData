class Node:
    def __init__(self, key, value, color, left=None, right=None):
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, "BLACK")
        self.root = self.NIL

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.root.color = "BLACK"

    def _insert(self, root, key, value):
        if root == self.NIL:
            return Node(key, value, "RED", self.NIL, self.NIL)

        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            root.value = value

        if self._is_red(root.right) and not self._is_red(root.left):
            root = self._rotate_left(root)
        if self._is_red(root.left) and self._is_red(root.left.left):
            root = self._rotate_right(root)
        if self._is_red(root.left) and self._is_red(root.right):
            self._flip_colors(root)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        while root != self.NIL:
            if key < root.key:
                root = root.left
            elif key > root.key:
                root = root.right
            else:
                return root.value
        return None

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root != self.NIL:
            self._inorder_traversal(root.left, result)
            result.append((root.key, root.value))
            self._inorder_traversal(root.right, result)

    def _is_red(self, node):
        return node.color == "RED"

    def _rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = "RED"
        return x

    def _rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = "RED"
        return x

    def _flip_colors(self, h):
        h.color = "RED"
        h.left.color = "BLACK"
        h.right.color = "BLACK"
