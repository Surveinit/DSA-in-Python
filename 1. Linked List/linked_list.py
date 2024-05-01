class Node:
    def __init__(self, value):
        # Constructor for creating a new node
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # Constructor for creating a new linked list with a single node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        # Method to print all nodes in the linked list
        temp = self.head  # Start from the head of the list
        while temp is not None:
            print(f"Node: {temp} Node_value: {temp.value}")
            temp = temp.next

    def append(self, value):
        # Method to add a new node at the end of the linked list
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Set the next pointer of the current tail node
            self.tail = new_node  # Update the tail pointer
        self.length += 1
        return True

    def pop(self):
        # Method to remove the last node from the linked list
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        # Method to add a Node at the Beginning of the linked list
        new_node = Node(value)
        if self.length == 0:
            # If the linked list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, adjust pointers to insert the new node at the beginning
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # Method to remove the first node from the linked list
        if self.length == 0:  # Check if the linked list is empty
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:  # If there was only one node, update the tail
            self.tail = None
        return temp

    def get_value(self, index):
        # Method to get the value of a node at a specified index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        # Method to set the value of a node at a specified index
        if index < 0 or index >= self.length:
            return None
        temp = self.get_value(index)
        if temp is not None:
            temp.value = value
            return temp
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
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        # Method to remove a node at a specified index
        if index < 0 or index >= self.length:
            return None
        if index <= 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get_value(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # Method to reverse the linked list
        # Swap head & tail pointers
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True


# Creating and manipulating a linked list
my_LinkedList = LinkedList(4)
my_LinkedList.append(7)
my_LinkedList.append(11)

# print('Head:', my_LinkedList.head.value)
# print('Tail:', my_LinkedList.tail.value)
# print('Length:', my_LinkedList.length)

# print("BEFORE")
# my_LinkedList.print_list()
#
# # PREPEND #
# my_LinkedList.prepend(19)
# print("AFTER")
# my_LinkedList.print_list()

# POP NODE #
# my_LinkedList.pop()
# my_LinkedList.pop()
#
# print("\nAfter Pop")
# my_LinkedList.print_list()

# POP FIRST #
# print(f"\nAfter POPPING ({my_LinkedList.pop_first().value})")
# my_LinkedList.print_list()
#
# my_LinkedList.pop_first()
# print(f"\nAfter POPPING ({my_LinkedList.pop_first().value})")
# my_LinkedList.print_list()

# # GET #
# my_LinkedList.print_list()
# print(f"\nGetting value from index 1 = ({my_LinkedList.get_value(3)})")

# SET #
# my_LinkedList.print_list()
# print(f"\nSetting value of index 1 = ({my_LinkedList.set_value(1,9)})")
# print(f"\nGetting value from index 1 = ({my_LinkedList.get_value(1).value})")

# INSERT #
# print("BEFORE INSERTING")
# my_LinkedList.print_list()
# my_LinkedList.insert(2,5)
# print("\nAFTER INSERTING")
# my_LinkedList.print_list()

# REMOVE #
# print("BEFORE REMOVING")
# my_LinkedList.print_list()
# my_LinkedList.remove(2)
# print("\nAFTER REMOVING")
# my_LinkedList.print_list()

# REVERSE #
print("BEFORE REVERSING")
my_LinkedList.print_list()
print("\nAFTER REVERSING")
my_LinkedList.reverse()
my_LinkedList.print_list()
