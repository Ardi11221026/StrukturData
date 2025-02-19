import java.util.Random;

class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    Node head;

    public LinkedList() {
        this.head = null;
    }

    // Metode untuk menyisipkan elemen di akhir linked list
    public void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    // Metode untuk mencetak isi linked list
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    // Metode untuk menghitung panjang linked list
    public int getLength() {
        int count = 0;
        Node current = head;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }

    // Metode untuk mendapatkan node ke-n dalam linked list
    public Node getNth(int n) {
        Node current = head;
        for (int i = 0; i < n && current != null; i++) {
            current = current.next;
        }
        return current;
    }

    public void addNode(int i) {
    }

    public void display() {
    }
}

//Proses algoritma shell sorting //
public class ShellSort {                                     
    public static void shellSort(LinkedList list) {                  
        int n = list.getLength();
        int gap = n / 2;

        while (gap > 0) {
            for (int i = gap; i < n; i++) {
                int temp = list.getNth(i).data;                     
                int j = i;

                while (j >= gap && list.getNth(j - gap).data > temp) {
                    list.getNth(j).data = list.getNth(j - gap).data;
                    j -= gap;
                }

                list.getNth(j).data = temp;
            }
            gap /= 2;
        }
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        Random random = new Random();

        // Menambahkan 10 angka acak antara 1 dan 20 ke dalam linked list
        for (int i = 0; i < 100; i++) {
            int randomNumber = random.nextInt(1000) + 1;
            list.insertAtEnd(randomNumber);
        }

        System.out.println("Linked List sebelum diurutkan:");
        list.printList();

        shellSort(list);

        System.out.println("\nLinked List setelah diurutkan:");
        list.printList();
    }
}