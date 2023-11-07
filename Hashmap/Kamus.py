import random

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = "RED"  # Node baru selalu berwarna merah

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, None)
        self.root = self.NIL_LEAF

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        if self.root == self.NIL_LEAF:
            self.root = new_node
            self.root.color = "BLACK"
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.key < current.key:
            if current.left == self.NIL_LEAF:
                current.left = new_node
                new_node.parent = current
                self._fix_insert(new_node)
            else:
                self._insert(current.left, new_node)
        elif new_node.key > current.key:
            if current.right == self.NIL_LEAF:
                current.right = new_node
                new_node.parent = current
                self._fix_insert(new_node)
            else:
                self._insert(current.right, new_node)
        else:
            current.value = new_node.value  # Jika kunci sudah ada, update nilai

    def _fix_insert(self, new_node):
        while new_node.color == "RED" and new_node.parent.color == "RED":
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right

                if uncle.color == "RED":
                    new_node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    new_node.parent.parent.color = "RED"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self._left_rotate(new_node)

                    new_node.parent.color = "BLACK"
                    new_node.parent.parent.color = "RED"
                    self._right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left

                if uncle.color == "RED":
                    new_node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    new_node.parent.parent.color = "RED"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self._right_rotate(new_node)

                    new_node.parent.color = "BLACK"
                    new_node.parent.parent.color = "RED"
                    self._left_rotate(new_node.parent.parent)

            if new_node == self.root:
                break

        self.root.color = "BLACK"

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current == self.NIL_LEAF:
            return None
        if key == current.key:
            return current.value
        if key < current.key:
            return self._search(current.left, key)
        return self._search(current.right, key)

    def gimmick(self):
        for i in range(10):
            print(random.randint(range1, range2))

# Contoh penggunaan kamus
rb_tree = RedBlackTree()
rb_tree.insert("acak", "random")
rb_tree.insert("hari", "day")
rb_tree.insert("mobil", "car")

while True:
    user_input = input("Masukkan kata yang ingin diterjemahkan (q untuk keluar): ")
    
    if user_input == "q":
        break

    result = rb_tree.search(user_input)
    if result is not None:
        print(f"key: {user_input}\nvalue: {result}")
        print("Gimmick:")
        rb_tree.gimmick()
    else:
        print(f"'{user_input}' tidak ditemukan dalam kamus.")
