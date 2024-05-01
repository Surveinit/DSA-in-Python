class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if not self.stack_list:
            # print("Stack is empty")
            return None
        return self.stack_list.pop()


def sort_stack(input_stack):
    sorted_stack = Stack()

    while not input_stack.is_empty():
        temp = input_stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            input_stack.push(sorted_stack.pop())
        sorted_stack.push(temp)

    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())

    return input_stack



my_list_stack = Stack()
my_list_stack.push(2)
my_list_stack.push(5)
my_list_stack.push(9)

sort_stack(my_list_stack)  # 2,5,9

my_list_stack.print_stack()

# print("Popped element:", my_list_stack.pop())
