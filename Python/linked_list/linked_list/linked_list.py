from .node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def size_of_list(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def traverse_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def insert_at_front(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data, next=None)
            return
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(data=data, next=None)

    def insert_list_at_front(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_front(data)

    def insert_list_at_end(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

