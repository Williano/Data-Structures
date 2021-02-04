from linked_list.linked_list import LinkedList


def main():

    linked_list = LinkedList()

    linked_list.insert_at_front(5)
    linked_list.insert_at_front(20)
    linked_list.insert_at_end(50)

    linked_list.traverse_list()

    print()
    print("Inserting list")
    linked_list.insert_list_at_end(["Will", "Bill", "Me"])
    print()
    print("Printing list")
    print()
    linked_list.traverse_list()

    print()
    print("Inserting list")
    linked_list.insert_list_at_front(["Will", "Bill", "Me"])
    print()
    print("Printing list")
    print()
    linked_list.traverse_list()


if __name__ == "__main__":
    main()
