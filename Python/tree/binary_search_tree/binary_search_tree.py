from typing import List


class BinarySearchTreeNode:
    """
    Binary Search Tree
    """

    def __init__(self, data) -> None:
        """
        Initializes a tree node with a value

        Args:
            data ([type]): the value for the node
        """
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        """
        Adds a child to the binary search tree.

        To avoid duplicates, it checks to see if the data already exists.
        If the data exists, it will return without adding it.
        """

        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data=data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data=data)

    def in_order_traversal(self) -> List:
        """
        Prints elements in the tree in an order from left sub tree,
        then root and right sub tree.

        """

        elements: List = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        """
        Searches for a value in the tree and returns True if the value is found
        or False if the value is not found.

        Args:
            value ([type]): The value to be searched for

        Returns:
            bool: True if value is found or False if not found
        """

        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)

        if value > self.data:
            if self.right:
                return self.right.search(value)

        return False
