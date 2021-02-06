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
            print(current_node.data, end=" ---> ")
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

    def insert_at_index(self, data):
        pass

    def insert_list_at_front(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_front(data)

    def insert_list_at_end(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def remove_at_index(self, index):

        count = 0

        self.check_index_out_of_range(index)

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head

        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
            count += 1

    def check_index_out_of_range(self, index):

        assert index >= 0 and index <= self.size_of_list(), \
            "(Error) Invalid index !!!"
