from collections import deque


class Stack(object):
    def __init__(self):
        self.stack = deque()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):

        if self.is_empty():
            print("You cannot pop from an empty stack.")

        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
