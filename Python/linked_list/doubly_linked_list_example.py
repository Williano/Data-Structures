from linked_list.doubly_linked_list.doubly_linked_list import DoublyLinkedList


def main():

    doubly_list = DoublyLinkedList()

    # insert values
    doubly_list.insert_values(["banana", "mango", "grapes", "orange"])

    # Traverse
    doubly_list.reverse_traversal()
    print(" ")
    doubly_list.front_traversal()

    # Insert at end
    print(" ")
    doubly_list.insert_at_end(data="figs")
    doubly_list.front_traversal()
    print(" ")

    # Insert at index
    doubly_list.insert_at_index(0, data="jackfruit")
    doubly_list.front_traversal()
    print(" ")
    print(doubly_list.get_size_of_list())


if __name__ == '__main__':
    main()
