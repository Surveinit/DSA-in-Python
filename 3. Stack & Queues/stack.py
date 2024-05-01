class Node:
    def __init__(self, value):
        # Constructor for creating a new node
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        # Constructor for creating a new stack with a single node
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        # Method to print all elements in the stack
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
            # print(f"Height = {self.height}")

    def push(self, value):
        # Method to add an element to the top of the stack
        new_node = Node(value)
        if self.height == 0:
            # If the stack is empty, set top to the new node
            self.top = new_node
        else:
            # Otherwise, adjust pointers to insert the new node at the top
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        # Method to remove and return the top element from the stack
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
        return temp


my_stack = Stack(1)

# PUSH #
print("PUSH")
my_stack.push(2)
my_stack.push(3)
my_stack.print_stack()

# POP #
print("\nPOP")
my_stack.pop()
my_stack.print_stack()
