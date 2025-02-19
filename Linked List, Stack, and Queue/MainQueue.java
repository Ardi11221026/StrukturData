public class MainQueue {
    public static void main(String[] args) {
        Queue queue = new Queue(5);

        // Test-case 1: pop saat queue masih kosong
        System.out.println("Test-case 1: Pop saat queue masih kosong");
        System.out.println("Isi Queue: " + queue);

        // Test-case 2: push beberapa angka
        System.out.println("\nTest-case 2: Push beberapa angka");
        queue.push(10);
        queue.push(20);
        queue.push(30);
        queue.push(40);
        System.out.println("Isi Queue: " + queue); 

        // Test-case 3: pop semua angka yang sudah di push
        System.out.println("\nTest-case 3: Pop semua angka yang sudah di-push");
        while (!queue.isEmpty()) {
            System.out.println("Popped: " + queue.pop());
            System.out.println("Isi Queue: " + queue);
        }
        // Queue is empty.

        // Test-case 4: menukar dua buah angka (swap)
        System.out.println("\nTest-case 4: Menukar dua buah angka");
        queue.push(100);
        queue.push(200);
        queue.push(300);
        queue.push(400);
        System.out.println("Isi Queue Sebelum ditukar: " + queue); 
        queue.swap(1, 2);
        System.out.println("Isi Queue Sesudah ditukar: " + queue);
    }
}
