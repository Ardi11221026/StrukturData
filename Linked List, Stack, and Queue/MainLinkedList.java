public class MainLinkedList {
    public static void main(String[] args) {
        LinkedList linkedList = new LinkedList();

        linkedList.add(10);
        linkedList.add(20);
        linkedList.add(30);

        System.out.println("Linked List: " + linkedList);

        linkedList.insert(50, 0);
        linkedList.insert(40, 4);

        System.out.println("After Insertions: " + linkedList);

        linkedList.remove(0);
        linkedList.remove(4);

        System.out.println("After Removals: " + linkedList);

        linkedList.swap(0, 2);

        System.out.println("After Swapping: " + linkedList);

        System.out.println("Value at index 1: " + linkedList.get(1));
    }
}