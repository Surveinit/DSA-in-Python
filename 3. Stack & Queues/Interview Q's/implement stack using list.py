# Stack: Implement Stack Using a List
# Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.
class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if not self.stack_list:
            print("Stack is empty")
            return None
        return self.stack_list.pop()



my_list_stack = Stack()
my_list_stack.push(3)
my_list_stack.push(2)
my_list_stack.push(1)

# my_list_stack.print_stack()

# print("Popped element:", my_list_stack.pop())
