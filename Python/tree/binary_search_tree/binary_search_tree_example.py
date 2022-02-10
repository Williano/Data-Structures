from binary_search_tree import BinarySearchTreeNode


def build_tree(elements):

    root = BinarySearchTreeNode(elements[0])

    for element_index in range(1, len(elements)):

        root.add_child(elements[element_index])

    return root


def main():

    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 40, 18, 4]

    numbers_tree = build_tree(numbers)

    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_travesal())
    print(numbers_tree.level_order_travesal(root=numbers_tree))
    print(numbers_tree.level_order_travesal_v2(root=numbers_tree))
    print(numbers_tree.search(value=2))
    print(f"Max of tree is: {numbers_tree.find_max()}")
    print(f"Min of tree is: {numbers_tree.find_min()}")
    print(f"Sum of tree is: {numbers_tree.calculate_sum()}")
    print(f"Height of tree is: {numbers_tree.height()}")
    print(f"Tree Balance: {numbers_tree.is_balanced()[0]}")
    print(f"Tree Balanced: {numbers_tree.balanced()}")


if __name__ == "__main__":
    main()
