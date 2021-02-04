from .node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def traverse_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def add_at_begining(self, data):
        node = Node(data=data, next=self.head)
        self.head = node