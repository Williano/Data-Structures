from linked_list.linked_list import LinkedList


def main():

    linked_list = LinkedList()

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


if __name__ == "__main__":
    main()
