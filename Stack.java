class Node {
    public int data;
    public Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}
class Stack {
    private Node top;

    public Stack() {
        top = null;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public void push(int data) {
        Node newNode = new Node(data);
        newNode.next = top;
        top = newNode;
    }

    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack kosong, tidak dapat pop.");
            return -1; // Mengembalikan nilai default untuk menunjukkan tumpukan kosong
        }else{

            int poppedData = top.data;
            top = top.next;
    
            return poppedData;
        }

    }

    public void printStack() {
        Node current = top;
        System.out.print("Isi stack: [");
        while (current != null) {
            System.out.print(current.data);
            if (current.next != null) {
                System.out.print(", ");
            }
            current = current.next;
        }
        System.out.println("]");
    }

    public void swapElements(int index1, int index2) {
        if (index1 == index2) {
            return; // Tidak perlu menukar jika indeksnya sama
        }

        Node prevNode1 = null, currNode1 = top;
        for (int i = 0; i < index1 && currNode1 != null; i++) {
            prevNode1 = currNode1;
            currNode1 = currNode1.next;
        }

        Node prevNode2 = null, currNode2 = top;
        for (int i = 0; i < index2 && currNode2 != null; i++) {
            prevNode2 = currNode2;
            currNode2 = currNode2.next;
        }

        if (currNode1 == null || currNode2 == null) {
            System.out.println("Indeks tidak valid untuk ditukar.");
            return;
        }

        if (prevNode1 != null) {
            prevNode1.next = currNode2;
        } else {
            top = currNode2;
        }

        if (prevNode2 != null) {
            prevNode2.next = currNode1;
        } else {
            top = currNode1;
        }

        Node temp = currNode1.next;
        currNode1.next = currNode2.next;
        currNode2.next = temp;
    }
}