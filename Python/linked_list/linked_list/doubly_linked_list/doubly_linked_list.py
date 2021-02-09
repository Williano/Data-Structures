from .doubly_node import DoublyNode


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def front_traversal(self):

        self.check_if_list_is_empty()

        current_node = self.head

        while current_node:
            print(current_node.data, end=" ---> ")
            current_node = current_node.next

    def reverse_traversal(self):


        current_node = self.tail

        while current_node:
            print(current_node.data, end=" <--- ")
            current_node = current_node.previous

    def search_by_value(self, value):

        recent_search_result_pointer = None

        if self.head is None:
            print("List is empty! You can search through an empty list.")
            return False
        elif recent_search_result_pointer is None:
            recent_search_result_pointer = self.head

        # If the the value comes before the recent result pointer,
        # we traverse backward otherwise traverse forward.
        if value < recent_search_result_pointer.data:
            while recent_search_result_pointer and value <= \
                    recent_search_result_pointer.data:
                if value == recent_search_result_pointer.data:
                    return True
                else:
                    recent_search_result_pointer = \
                        recent_search_result_pointer.previous
        else:
            while recent_search_result_pointer and value >= \
                    recent_search_result_pointer.data:
                if value == recent_search_result_pointer.data:
                    return True
                else:
                    recent_search_result_pointer = \
                        recent_search_result_pointer.next

        # If the target is not found in the list, return False
        return False

    def insert_value_into_ordered_linked_list(self, value):

        new_node = DoublyNode(data=value)

        if self.head is None:  # empty list
            self.head = new_node
            self.tail = self.head

        elif value < self.head.data:  # insert before head
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        elif value > self.head.data:  # insert after tail
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        else:  # insert in the middle
            node = self.head
            while node is not None and node.data < value:
                node = node.next

            new_node.next = node
            new_node.previous = node.previous
            node.previous.next = new_node
            node.previous = new_node

    def check_if_list_is_empty(self):
        if self.head is None:
            print("Linked list is empty")
            return