from collections import deque
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

    def pre_order_traversal(self) -> List:

        """
        Prints elements in the tree in an order from root,
        then left sub-tree and right sub-tree.
        """
        elements = []

        # Add root to list first
        elements.append(self.data)

        # Add left sub-tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Add right sub-tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_travesal(self) -> List:
        """
        Prints elements in the tree in an order from left sub-tree,
        then right sub-tree and root.
        """
        elements: List = []

        # Add left sub-tree
        if self.left:
            elements += self.left.post_order_travesal()

        # Add right sub-tree
        if self.right:
            elements += self.right.post_order_travesal()

        # Add root
        elements.append(self.data)

        return elements

    def level_order_travesal(self, root) -> List:
        """[summary]

        Returns:
            List: [description]
        """

        if root is None:
            return

        queue = deque()
        queue.append(root)

        data: List = []

        while queue:

            level: List = []

            for _ in range(len(queue)):

                current_node = queue.popleft()

                if current_node:
                    level.append(current_node.data)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            if level:
                data.append(level)

        return data

    def level_order_travesal_v2(self, root) -> List:
        """[summary]

        Returns:
            List: traversed list
        """

        if root is None:
            return

        queue = deque()
        queue.append(root)

        data: List = []

        while queue:
            current_node = queue.popleft()

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

            if current_node:
                data.append(current_node.data)

        return data

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

    def find_max(self):
        """
        Finds the maximum value in the tree
        """

        if self.right is None:
            return self.data

        return self.right.find_max()

    def find_min(self):
        """
        Finds the maximum value in the tree
        """

        if self.left is None:
            return self.data

        return self.left.find_min()

    def calculate_sum(self):
        """
        Calculates the sum of the tree
        """
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

        return self.data + left_sum + right_sum

    def height(self) -> int:
        """
        Calculates the height of the tree

        Returns:
            int: height of the tree
        """

        if self.data is None:
            return 0

        left_depth = self.left.height() if self.left else 0
        right_depth = self.right.height() if self.right else 0

        return max(left_depth, right_depth) + 1

    def delete(self, value):
        """[summary]

        Args:
            value (Any): [description]
        """
        pass

    def is_balanced(self) -> bool:
        """Checks whether the tree is balanced or not

        Returns:
            bool: returns True if tree is balanced and False if it is not
        """

        if self.data is None:
            return [True, 0]

        left_sub_tree: List = self.left.is_balanced() if self.left else [True, 0]

        right_sub_tree: List = self.right.is_balanced() if self.right else [True, 0]

        is_balanced: bool = (
            left_sub_tree[0]
            and right_sub_tree[0]
            and abs(left_sub_tree[1] - right_sub_tree[1]) <= 1
        )

        # return [is_balanced, self.height()]

        return [is_balanced, 1 + max(left_sub_tree[1], right_sub_tree[1])]

    def balanced(self) -> bool:
        """Checks whether the tree is balanced or not

        Returns:
            bool: returns True if tree is balanced and False if it is not
        """

        if self.data is None:
            return self.data

        # Calucate the height of the left and right sub trees
        left_sub_tree = self.left.height() if self.left else 0
        right_sub_tree = self.right.height() if self.right else 0

        if abs(left_sub_tree - right_sub_tree) <= 1:
            return True

        # Check if the left and right sub trees are balanced
        is_left_balanced = self.left.balanced() if self.left else False
        is_right_balanced = self.right.balanced() if self.right else False

        return is_left_balanced and is_right_balanced
