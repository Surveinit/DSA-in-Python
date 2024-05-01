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

    def is_palindrome(self):
        if self.length == 0:
            return True

        left = self.head
        right = self.tail

        while left != right:
            if left.value != right.value:
                return False

            left = left.next
            right = right.prev
        return True



my_doubly_ll = DoublyLinkedList(1)
my_doubly_ll.append(2)
my_doubly_ll.append(3)
my_doubly_ll.append(2)
my_doubly_ll.append(1)

print(my_doubly_ll.is_palindrome())


