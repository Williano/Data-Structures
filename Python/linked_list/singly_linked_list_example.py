from linked_list.singly_linked_list.singly_linked_list import SinglyLinkedList


def main():

    linked_list = SinglyLinkedList()

    # Insert at front
    linked_list.insert_at_front(5)
    linked_list.insert_at_front(20)
    linked_list.insert_at_end(50)
    print(linked_list.size_of_list())

    linked_list.traverse_list()

    print()
    print("Inserting list")

    # Insert list at end
    linked_list.insert_list_at_end(["Will", "Bill", "Me"])
    print(linked_list.size_of_list())
    print()
    print("Printing list")
    print()
    linked_list.traverse_list()

    # Insert list the front
    print()
    print("Inserting list")
    linked_list.insert_list_at_front(["Will", "Bill", "Me"])
    print(linked_list.size_of_list())
    print()
    print("Printing list")
    print()
    linked_list.traverse_list()

    # Remove list a specific index
    print()
    print("Inserting list")
    linked_list.insert_list_at_front(["Test", "Example", "Test"])
    linked_list.remove_at_index(2)
    print(linked_list.size_of_list())
    print()
    print("Printing list")
    print()
    linked_list.traverse_list()

    # Insert at specific index
    print()
    print("Inserting data")
    linked_list.insert_at_index(0, "Quick Text")
    linked_list.traverse_list()
    linked_list.insert_at_index(2, "Testing")
    print(linked_list.size_of_list())
    print()
    print("Printing list")
    print()
    linked_list.traverse_list()

    # Insert after value
    print()
    print("Inserting data")
    linked_list.insert_after_value(data_after="Testing", data_to_insert=5)
    linked_list.traverse_list()
    print(f'Size of list is: {linked_list.size_of_list()}')
    print()
    print("Printing list")
    print()
    linked_list.traverse_list()

    # Remove by value
    print()
    print("Removing data ..................")
    linked_list.remove_by_value(value="Example")
    linked_list.traverse_list()
    print(f'Size of list is: {linked_list.size_of_list()}')
    print()
    print("Printing list")
    print()
    linked_list.traverse_list()


if __name__ == "__main__":
    main()
