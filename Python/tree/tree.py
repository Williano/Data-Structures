from typing import List


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children: List = []
        self.parent = None

    def add_child(self, child) -> None:
        child.parent = self
        self.children.append(child)

    def print_tree(self) -> None:
        print(self.data)

        for child in self.children:
            print(child.data)
