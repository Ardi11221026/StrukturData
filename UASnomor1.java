class Node {
    int key;
    Node left, right;

    public Node(int item) {
        key = item;
        left = right = null;
    }
}

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

    void inorderTraversal(Node root) {
        if (root != null) {
            inorderTraversal(root.left);
            System.out.print(root.key + " ");
            inorderTraversal(root.right);
        }
    }

    void preorderTraversal(Node root) {
        if (root != null) {
            System.out.print(root.key + " ");
            preorderTraversal(root.left);
            preorderTraversal(root.right);
        }
    }

    void postorderTraversal(Node root) {
        if (root != null) {
            postorderTraversal(root.left);
            postorderTraversal(root.right);
            System.out.print(root.key + " ");
        }
    }
}

public class UASnomor1 {
    public static void main(String[] args) {
        int[] input = {73, 29, 51, 92, 14, 63, 37, 81, 46, 55, 64, 34, 102, 124, 98, 18, 8};

        BinarySearchTree tree = new BinarySearchTree();

        for (int key : input) {
            tree.insert(key);
        }

        System.out.println("Inorder Traversal:");
        tree.inorderTraversal(tree.root);

        System.out.println("\n\nPreorder Traversal:");
        tree.preorderTraversal(tree.root);

        System.out.println("\n\nPostorder Traversal:");
        tree.postorderTraversal(tree.root);
    }
}