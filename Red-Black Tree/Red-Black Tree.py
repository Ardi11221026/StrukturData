class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None  
        self.red = False

    def setRight(self, right):
        self.right = right

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def isRed(self):
        return self.red

    def setRed(self, red):
        self.red = red

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

class Tree:
    def __init__(self):
        self.root = None

    def search(self, key):
        found = self._search(self.root, key)
        print(found)
        return found

    def isRed(self, key):
        node = self._isExist(self.root, key)
        red = node.isRed()
        if not red:
            print(f"Node is Black {key}")
        else:
            print(f"Node is Red {key}")
        return red

    def _isExist(self, parent, key):
        if parent is None:
            return parent
        else:
            if parent.getKey() == key:
                return parent
            if parent.getKey() > key:
                return self._isExist(parent.getLeft(), key)
            else:
                return self._isExist(parent.getRight(), key)

    def _search(self, parent, key):
        if parent is None:
            return False
        else:
            if parent.getKey() == key:
                print(f"Node found = {key}")
                return True
            if parent.getKey() > key:
                return self._search(parent.getLeft(), key)
            else:
                return self._search(parent.getRight(), key)

    def add(self, key):
        node = Node(key)
        isThere = self._search(self.root, key)
        if isThere:
            print(f"{key} Didalam node? {isThere}")
            return False
        if self.root is None:
            self.root = node
            return True
        self._insert(self.root, node)
        self._balancingTree(node)
        return True

    def _insert(self, parent, node):
        if parent is None:
            node.setRed(True)
            return node
        if node.getKey() < parent.getKey():
            parent.setLeft(self._insert(parent.getLeft(), node))
            parent.getLeft().setParent(parent)
        else:
            parent.setRight(self._insert(parent.getRight(), node))
            parent.getRight().setParent(parent)
        return parent

    def remove(self, key):
        if self.root is None:
            print("Tree still Empty")
            return False
        if not self._search(self.root, key):
            print(f"Couldnt found {key} Node in Tree")
            return False
        self.root = self._remove(self.root, key)
        self._balancingTree(self.root)
        print(f"Succeded Deleted node {key}")
        return True

    def _remove(self, node, key):
        if node is None:
            return node
        if key < node.getKey():
            node.setLeft(self._remove(node.getLeft(), key))
        elif key > node.getKey():
            node.setRight(self._remove(node.getRight(), key))
        else:
            if node.getLeft() is None:
                return node.getRight()
            elif node.getRight() is None:
                return node.getLeft()
            node.setKey(self._successor(node.getRight()))
            node.setRight(self._remove(node.getRight(), node.getKey()))
        return node

    def _successor(self, node):
        minimum = node.getKey()
        while node.getLeft() is not None:
            minimum = node.getLeft().getKey()
            node = node.getLeft()
        return minimum

    def leftRotate(self, x):
        rightTemp = x.getRight()
        x.setRight(rightTemp.getLeft())
        if rightTemp.getLeft() is not None:
            rightTemp.getLeft().setParent(x)
        rightTemp.setParent(x.getParent())
        if x.getParent() is None:
            self.root = rightTemp
        elif x == x.getParent().getLeft():
            x.getParent().setLeft(rightTemp)
        else:
            x.getParent().setRight(rightTemp)
        rightTemp.setLeft(x)
        x.setParent(rightTemp)

    def rightRotate(self, y):
        leftTemp = y.getLeft()
        y.setLeft(leftTemp.getRight())
        if leftTemp.getRight() is not None:
            leftTemp.getRight().setParent(y)
        leftTemp.setParent(y.getParent())
        if y.getParent() is None:
            self.root = leftTemp
        elif y == y.getParent().getLeft():
            y.getParent().setLeft(leftTemp)
        else:
            y.getParent().setRight(leftTemp)
        leftTemp.setRight(y)
        y.setParent(leftTemp)

    def _balancingTree(self, node):
        while self.root != node and node.getParent() is not None and node.getParent().isRed():
            if node.getParent() == node.getParent().getParent().getLeft():
                if node.getParent().getParent().getRight() is not None and node.getParent().getParent().getRight().isRed(): 
                    node.getParent().getParent().getRight().setRed(False)
                    node.getParent().getParent().setRed(True)
                    node.getParent().setRed(False)
                    node = node.getParent().getParent()
                else:
                    if node == node.getParent().getRight():
                        node = node.getParent()
                        self.leftRotate(node)  
                    node.getParent().setRed(False)
                    node.getParent().getParent().setRed(True)
                    self.rightRotate(node.getParent().getParent())
            else:
                if node.getParent() == node.getParent().getParent().getRight():
                    if node.getParent().getParent().getLeft() is not None and node.getParent().getParent().getLeft().isRed(): 
                        node.getParent().getParent().getLeft().setRed(False)
                        node.getParent().getParent().setRed(True)
                        node.getParent().setRed(False)
                        node = node.getParent().getParent()
                    else:
                        if node == node.getParent().getLeft():
                            node = node.getParent()
                            self.rightRotate(node)
                        node.getParent().setRed(False)
                        node.getParent().getParent().setRed(True)
                        self.leftRotate(node.getParent().getParent())
            self.root.setRed(False)

    def inorderTraversal(self, node):
        if node is not None:
            self.inorderTraversal(node.getLeft())
            print(node.getKey(), end=' ')
            self.inorderTraversal(node.getRight())

    def preorderTraversal(self, node):
        if node is None:
            return
        print(node.getKey(), end=' ')
        self.preorderTraversal(node.getLeft())
        self.preorderTraversal(node.getRight())

    def postorderTraversal(self, node):
        if node is None:
            return
        self.postorderTraversal(node.getLeft())
        self.postorderTraversal(node.getRight())
        print(node.getKey(), end=' ')

    def getRoot(self):
        return self.root

    def preorderTraversal(self, node):
        if node is not None:
            print(node.getKey(), end=' ')
            self.preorderTraversal(node.getLeft())
            self.preorderTraversal(node.getRight())

    def inorderTraversal(self, node):
        if node is not None:
            self.inorderTraversal(node.getLeft())
            print(node.getKey(), end=' ')
            self.inorderTraversal(node.getRight())

    def postorderTraversal(self, node):
        if node is not None:
            self.postorderTraversal(node.getLeft())
            self.postorderTraversal(node.getRight())
            print(node.getKey(), end=' ')

    def visualize(self):
        if self.root is not None:
            self._visualize(self.root, "", True)

    def display(self):
        treeStringBuilder = []
        self._display(self.root, "", True, treeStringBuilder)
        for line in treeStringBuilder:
            print(line)

    def _display(self, node, prefix, isRight, treeStringBuilder):
        if node is not None:
            treeStringBuilder.append(prefix + ("|-- " if isRight else "`-- ") + f"{node.getKey()} ({'R' if node.isRed() else 'B'})")
            self._display(node.getRight(), prefix + ("|   " if isRight else "    "), True, treeStringBuilder)
            self._display(node.getLeft(), prefix + ("|   " if isRight else "    "), False, treeStringBuilder)

if __name__ == "__main__":
    tree = Tree()
    tree.add(3)
    tree.add(2)
    tree.add(5)
    tree.add(7)
    tree.add(4)
    tree.add(8)
    tree.add(9)
    tree.add(10)
    tree.add(1)
    tree.add(12)
    tree.add(6)
    tree.add(11)

    tree.remove(12)
    
    print("In-order Traversal:")
    tree.inorderTraversal(tree.getRoot())

    print("\nPre-order Traversal:")
    tree.preorderTraversal(tree.getRoot())

    print("\nPost-order Traversal:")
    tree.postorderTraversal(tree.getRoot())

    print("\nRed-Black Tree Structure:")
    tree.display()