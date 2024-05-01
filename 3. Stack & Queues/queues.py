class Node:
    def __init__(self, value):
        # Constructor for creating a new node
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        # Constructor for creating a new queue with a single node
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        # Method to print all elements in the queue
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        # Method to add an element to the end of the queue
        new_node = Node(value)

        if self.length == 0:
            # If the queue is empty, set both first and last to the new node
            self.first = new_node
            self.last = new_node
        else:
            # Otherwise, adjust pointers to insert the new node at the end
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return new_node

    def dequeue(self):
        # Method to remove and return the first element from the queue
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            # If there is only one element, set both first and last to None
            self.first = None
            self.last = None
        else:
            # Otherwise, adjust pointers to remove the first element
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

my_queue.dequeue()
my_queue.dequeue()

my_queue.print_queue()
