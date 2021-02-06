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
