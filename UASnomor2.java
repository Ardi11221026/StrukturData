class BinarySearchTree {
    Node root;

    BinarySearchTree() {
        root = null;
    }

    void insert(int key) {
        root = insertRec(root, key);
    }

    Node insertRec(Node root, int key) {
        if (root == null) {
            root = new Node(key);
            return root;
        }

        if (key < root.key)
            root.left = insertRec(root.left, key);
        else if (key > root.key)
            root.right = insertRec(root.right, key);

        return root;
    }

    String search(int key) {
        return searchRec(root, key);
    }

    String searchRec(Node root, int key) {
        if (root == null) {
            return key + " tidak ditemukan di dalam tree";
        }

        if (key == root.key) {
            return key + " ditemukan di dalam tree";
        }

        if (key < root.key) {
            return searchRec(root.left, key);
        } else {
            return searchRec(root.right, key);
        }
    }
}

public class UASnomor2 {
    public static void main(String[] args) {
        int[] input = {73, 29, 51, 92, 14, 63, 37, 81, 46, 55, 64, 34, 102, 124, 98, 18, 8};

        BinarySearchTree tree = new BinarySearchTree();

        for (int key : input) {
            tree.insert(key);
        }
        System.out.println("Searching:");
        System.out.println(tree.search(37)); 
        System.out.println(tree.search(100)); 
    }
}