class Node {
    int value;
    Node next, prev;
    Node(int value) { this.value = value; }
}

class LinkedList {
    Node first, last;

    void add(int value) {
        Node newNode = new Node(value);
        if (last == null) first = last = newNode;
        else {
            last.next = newNode;
            newNode.prev = last;
            last = newNode;
        }
    }

    void insert(int value, int index) {
        Node newNode = new Node(value);
        if (index == 0) {
            newNode.next = first;
            if (first != null) first.prev = newNode;
            first = newNode;
        } else {
            Node current = first;
            for (int i = 0; i < index - 1 && current != null; i++)
                current = current.next;
            if (current == null) return;
            newNode.next = current.next;
            if (current.next != null) current.next.prev = newNode;
            newNode.prev = current;
            current.next = newNode;
        }
    }

    void remove(int index) {
        if (index == 0) {
            if (first != null) {
                first = first.next;
                if (first != null) first.prev = null;
            }
        } else {
            Node current = first;
            for (int i = 0; i < index - 1 && current != null; i++)
                current = current.next;
            if (current == null || current.next == null) return;
            current.next = current.next.next;
            if (current.next != null) current.next.prev = current;
        }
    }

    void swap(int index1, int index2) {
        if (index1 == index2) return;

        Node prev1 = null, current1 = first;
        for (int i = 0; i < index1 && current1 != null; i++) {
            prev1 = current1;
            current1 = current1.next;
        }

        Node prev2 = null, current2 = first;
        for (int i = 0; i < index2 && current2 != null; i++) {
            prev2 = current2;
            current2 = current2.next;
        }

        if (current1 == null || current2 == null) return;

        if (prev1 != null) prev1.next = current2;
        else first = current2;

        if (prev2 != null) prev2.next = current1;
        else first = current1;

        Node temp = current1.next;
        current1.next = current2.next;
        current2.next = temp;

        if (current1.next != null) current1.next.prev = current1;
        if (current2.next != null) current2.next.prev = current2;

        Node tempPrev = current1.prev;
        current1.prev = current2.prev;
        current2.prev = tempPrev;

        if (current1.prev == null) first = current1;
        if (current2.prev == null) first = current2;
    }

    int get(int index) {
        Node current = first;
        for (int i = 0; i < index && current != null; i++)
            current = current.next;
        if (current == null) return -1;
        return current.value;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node current = first;
        while (current != null) {
            sb.append(current.value).append(" ");
            current = current.next;
        }
        return sb.toString();
    }
}
