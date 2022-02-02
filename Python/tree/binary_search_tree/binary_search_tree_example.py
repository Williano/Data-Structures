from binary_search_tree import BinarySearchTreeNode


def build_tree(elements):

    root = BinarySearchTreeNode(elements[0])

    for element_index in range(1, len(elements)):

        root.add_child(elements[element_index])

    return root


def main():

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    numbers_tree = build_tree(numbers)

    print(numbers_tree.in_order_traversal())


if __name__ == "__main__":
    main()
