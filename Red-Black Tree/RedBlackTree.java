class Node {
    private char key;
    private Node right;
    private Node left;
    private Node parent;
    private boolean red;

    public Node(char key) {
        this.key = key;
        this.red = true; // Node baru selalu berwarna merah
    }

    public void setRight(Node right) {
        this.right = right;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public void setParent(Node parent) {
        this.parent = parent;
    }

    public void setRed(boolean red) {
        this.red = red;
    }

    public Node getRight() {
        return right;
    }

    public Node getLeft() {
        return left;
    }

    public Node getParent() {
        return parent;
    }

    public char getKey() {
        return key;
    }

    public boolean isRed() {
        return red;
    }
}

class Tree {
    private Node root;

    public Tree() {
        this.root = null;
    }

    public void add(char key) {
        // Implementasi penambahan node ke dalam Red-Black Tree
        // ...
    }

    public boolean remove(char key) {
        // Implementasi penghapusan node dari Red-Black Tree
        // ...
        return false;
    }

    public boolean isExist(char key) {
        // Implementasi pengecekan keberadaan node dalam Red-Black Tree
        // ...
        return false;
    }

    private void rotateToRight(Node current) {
        // Implementasi rotasi ke kanan pada Red-Black Tree
        // ...
    }

    private void rotateToLeft(Node current) {
        // Implementasi rotasi ke kiri pada Red-Black Tree
        // ...
    }

    // Metode untuk menampilkan Tree dengan algoritma pre-order, in-order, dan post-order
    private void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.getKey() + " ");
            preOrder(node.getLeft());
            preOrder(node.getRight());
        }
    }

    private void inOrder(Node node) {
        if (node != null) {
            inOrder(node.getLeft());
            System.out.print(node.getKey() + " ");
            inOrder(node.getRight());
        }
    }

    private void postOrder(Node node) {
        if (node != null) {
            postOrder(node.getLeft());
            postOrder(node.getRight());
            System.out.print(node.getKey() + " ");
        }
    }

    public void displayTree() {
        System.out.println("Pre-order: ");
        preOrder(root);
        System.out.println("\n\nIn-order: ");
        inOrder(root);
        System.out.println("\n\nPost-order: ");
        postOrder(root);
    }
}
