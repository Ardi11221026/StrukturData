class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getKey(self):
        return self.key

class Tree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if not self.root:
            self.root = Node(key)
            return True
        return self._add_recursive(self.root, key)

    def _add_recursive(self, current_node, key):
        if key == current_node.getKey():
            return False
        elif key < current_node.getKey():
            if current_node.getLeft() is None:
                current_node.setLeft(Node(key))
            else:
                return self._add_recursive(current_node.getLeft(), key)
        else:
            if current_node.getRight() is None:
                current_node.setRight(Node(key))
            else:
                return self._add_recursive(current_node.getRight(), key)
        return True

    def remove(self, key):
        if not self.root:
            return False
        return self._remove_recursive(None, self.root, key)

    def _remove_recursive(self, parent, current_node, key):
        if current_node is None:
            return False
        if key == current_node.getKey():
            if current_node.getLeft() is None and current_node.getRight() is None:
                if parent:
                    if parent.getLeft() == current_node:
                        parent.setLeft(None)
                    else:
                        parent.setRight(None)
                else:
                    self.root = None
            elif current_node.getLeft() is None:
                if parent:
                    if parent.getLeft() == current_node:
                        parent.setLeft(current_node.getRight())
                    else:
                        parent.setRight(current_node.getRight())
                else:
                    self.root = current_node.getRight()
            elif current_node.getRight() is None:
                if parent:
                    if parent.getLeft() == current_node:
                        parent.setLeft(current_node.getLeft())
                    else:
                        parent.setRight(current_node.getLeft())
                else:
                    self.root = current_node.getLeft()
            else:
                successor_parent = current_node
                successor = current_node.getRight()
                while successor.getLeft() is not None:
                    successor_parent = successor
                    successor = successor.getLeft()
                current_node.key = successor.getKey()
                if successor_parent.getLeft() == successor:
                    successor_parent.setLeft(successor.getRight())
                else:
                    successor_parent.setRight(successor.getRight())
        elif key < current_node.getKey():
            return self._remove_recursive(current_node, current_node.getLeft(), key)
        else:
            return self._remove_recursive(current_node, current_node.getRight(), key)

    def pre_order_traversal(self, node):
        if node:
            print(node.getKey(), end=' ')
            self.pre_order_traversal(node.getLeft())
            self.pre_order_traversal(node.getRight())

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.getLeft())
            print(node.getKey(), end=' ')
            self.in_order_traversal(node.getRight())

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.getLeft())
            self.post_order_traversal(node.getRight())
            print(node.getKey(), end=' ')

# Membuat objek BST
bst = Tree()

# Menambahkan 10 angka manual
keys = (3,2,5,7,4,8,9,10,1,6)
for key in keys:
    bst.add(key)

# Menampilkan BST dengan pre-order traversal
print("Pre-order Traversal:")
bst.pre_order_traversal(bst.root)
print()

# Menampilkan BST dengan in-order traversal
print("In-order Traversal:")
bst.in_order_traversal(bst.root)
print()

# Menampilkan BST dengan post-order traversal
print("Post-order Traversal:")
bst.post_order_traversal(bst.root)
print()