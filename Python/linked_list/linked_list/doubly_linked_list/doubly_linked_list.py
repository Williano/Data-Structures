from .doubly_node import DoublyNode


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def front_traversal(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end=" ---> ")
            current_node = current_node.next

    def reverse_traversal(self):
        current_node = self.tail

        while current_node:
            print(current_node.data, end=" <--- ")
            current_node = current_node.previous
