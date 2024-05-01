class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            # print(f"Current Node  {temp}, Next Node {temp.next}, Prev Node {temp.prev}")
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def swap_first_last(self):
        if self.length == 0:
            return False
        if self.head and self.tail is None:
            return False
        self.head.value, self.tail.value = self.tail.value, self.head.value
        return True




my_doubly_ll = DoublyLinkedList(1)
my_doubly_ll.append(2)
my_doubly_ll.append(3)
my_doubly_ll.append(4)

print("Before")
my_doubly_ll.print_list()

print("\nAfter")
my_doubly_ll.swap_first_last()

my_doubly_ll.print_list()