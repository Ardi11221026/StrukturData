public class RedBlackTreeDemo {
    public static void main(String[] args) {
        Tree redBlackTree = new Tree();

        // Masukkan 10 deret key secara acak
        char[] keys = {'F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H', 'J'};

        // Masukkan semua key ke dalam tree
        for (char key : keys) {
            redBlackTree.add(key);
        }

        // Tampilkan ke layar dengan algoritma pre-order, in-order, dan post-order
        redBlackTree.displayTree();
    }
}