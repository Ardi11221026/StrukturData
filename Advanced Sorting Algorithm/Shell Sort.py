import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def getLength(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def getNth(self, n):
        current = self.head
        for i in range(n):
            if current is None:
                return None
            current = current.next
        return current

def shellSort(linked_list):
    n = linked_list.getLength()
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = linked_list.getNth(i).data
            j = i

            while j >= gap and linked_list.getNth(j - gap).data > temp:
                linked_list.getNth(j).data = linked_list.getNth(j - gap).data
                j -= gap

            linked_list.getNth(j).data = temp
        gap //= 2

if __name__ == "__main__":
    linked_list = LinkedList()

    # Menambahkan 100 angka acak antara 1 dan 100 ke dalam linked list tanpa angka yang sama
    random_numbers = random.sample(range(1, 101), 100)
    for number in random_numbers:
        linked_list.insertAtEnd(number)

    print("Linked List sebelum diurutkan:")
    linked_list.printList()

    shellSort(linked_list)

    print("\nLinked List setelah diurutkan:")
    linked_list.printList()
