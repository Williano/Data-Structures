from typing import List


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children: List = []
        self.parent = None

    def add_child(self, child) -> None:
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self) -> None:

        spaces = " " * self.get_level() * 3

        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)

        if self.children:

            for child in self.children:
                child.print_tree()
