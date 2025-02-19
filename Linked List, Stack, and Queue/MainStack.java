public class MainStack {
    public static void main(String[] args) {
        Stack stack = new Stack();

        System.out.println("Test case 1: Pop saat Stack masih kosong"); 
        stack.pop(); // Stack kosong, tidak dapat pop.
        stack.printStack();

        System.out.println("\nTest case 2: Push beberapa angka");
        stack.push(50);
        stack.push(100);
        stack.push(150);
        stack.push(200);
        stack.printStack();

        System.out.println("\nTest case 3: Pop semua angka yang di-push");
        while (!stack.isEmpty()) {
            stack.printStack();
            stack.pop();
        }
        stack.printStack();

        System.out.println("\nTest case 4: Menukar dua buah angka (swap)");
        stack.push(250);
        stack.push(300);
        stack.push(350);
        stack.push(400);
        stack.printStack();
        System.out.println("Angka di indeks 1 dan 2 telah ditukar.");
        stack.swapElements(1, 2);
        stack.printStack();
    }
}
