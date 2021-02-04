from .node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_at_begining(self, data):
        node = Node(data=data, next=self.head)
        self.head = node


