class Node:
    def __init__(self, value):
        # Constructor for creating a new node
        self.value = value
        self.next = None
        self.prev = None  # Pointer to the previous node in a doubly linked list


class DoublyLinkedList:
    def __init__(self, value):
        # Constructor for creating a new doubly linked list with a single node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        # Method to print all nodes in the doubly linked list
        temp = self.head
        while temp is not None:
            # print(f"Current Node  {temp}, Next Node {temp.next}, Prev Node {temp.prev}")
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # Method to add a new node at the end of the doubly linked list
        new_node = Node(value)

        if self.length == 0:
            # If the doubly linked list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node

        else:
            # Otherwise, adjust pointers to insert the new node at the end
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # Method to remove the last node from the doubly linked list
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            # If there is only one node, set head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, adjust pointers to remove the last node
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    def prepend(self, value):
        # Method to add a node at the beginning of the doubly linked list
        new_node = Node(value)

        if self.length == 0:
            # If the doubly linked list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Adjust pointers to insert the new node at the beginning
            self.head.prev = new_node
            new_node.next = self.head
            self.head = self.head.prev
        self.length += 1
        return new_node

    def pop_first(self):
        # Method to remove the first node from the doubly linked list
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            # If there is only one node, set head and tail to None
            self.head = None
            self.tail = None
        else:
            # Adjust pointers to remove the first node
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp


    # Most of the part work just fine in DLL as LL, but DLL has prev so we can optimise this, if the finding node is in the
    # first half we can use temp head or else temp tail
    def get_value(self, index):
        # Method to get the value of a node at a specified index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            # If the index is in the first half of the list, start from the head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            # If the index is in the second half of the list, start from the tail
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp

    def set_value(self, index, value):
        # Method to set the value of a node at a specified index
        if index < 0 or index >= self.length:
            return None
        temp = self.get_value(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # Method to insert a new node at a specified index
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get_value(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after

        after.prev = new_node
        before.next = new_node

        self.length += 1
        return new_node


    def remove(self, index):
        # Method to remove a node at a specified index
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        node_remove = self.get_value(index)
        before = node_remove.prev
        after = node_remove.next

        node_remove.prev = None
        node_remove.next = None

        before.next = after
        after.prev = before

        # --> OR below is the efficient way as it doesnt use multiple variables
        # temp = self.get_value(index)
        # temp.prev.next = temp.next
        # temp.next.prev = temp.prev
        #
        # temp.prev = None
        # temp.next = None

        self.length -= 1
        return node_remove


my_doubly_ll = DoublyLinkedList(5)
my_doubly_ll.append(7)
my_doubly_ll.append(9)
my_doubly_ll.append(10)

# my_doubly_ll.print_list()

# print(f"Value at {my_doubly_ll.get_value(1).value}")
# print(f"\nValue at {my_doubly_ll.set_value(1, 2)}")

# my_doubly_ll.insert(2, 3)

print(my_doubly_ll.remove(0))
my_doubly_ll.print_list()
