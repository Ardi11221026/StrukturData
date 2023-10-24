public class Queue {
    private int maxSize;
    private int[] queueArray;
    private int front;
    private int rear;
    private int currentSize;

    public Queue(int size) {
        maxSize = size;
        queueArray = new int[maxSize];
        front = 0;
        rear = -1;
        currentSize = 0;
    }

    public void push(int value) {
        if (currentSize < maxSize) {
            if (rear == maxSize - 1) {
                rear = -1;
            }
            queueArray[++rear] = value;
            currentSize++;
        } else {
            System.out.println("Queue penuh, tidak bisa push" + value);
        }
    }

    public int pop() {
        if (currentSize > 0) {
            int temp = queueArray[front++];
            if (front == maxSize) {
                front = 0;
            }
            currentSize--;
            return temp;
        } else {
            System.out.println("Queue kosong.");
            return -1;
        }
    }

    public boolean isEmpty() {
        return currentSize == 0;
    }

    public boolean isFull() {
        return currentSize == maxSize;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder("[");
        for (int i = 0; i < currentSize; i++) {
            result.append(queueArray[(front + i) % maxSize]);
            if (i < currentSize - 1) {
                result.append(", ");
            }
        }
        result.append("]");
        return result.toString();
    }

    public void swap(int index1, int index2) {
        if (index1 >= 0 && index1 < currentSize && index2 >= 0 && index2 < currentSize) {
            int temp = queueArray[(front + index1) % maxSize];
            queueArray[(front + index1) % maxSize] = queueArray[(front + index2) % maxSize];
            queueArray[(front + index2) % maxSize] = temp;
        } else {
            System.out.println("Indeks tidak valid untuk ditukar.");
        }
    }
}
