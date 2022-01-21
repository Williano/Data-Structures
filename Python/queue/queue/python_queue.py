from collections import deque


class Queue(object):
    def __init__(self):
        self._queue = deque()

    def size(self):
        return len(self._queue)

    def is_empty(self):
        return len(self._queue) == 0

    def enqueue(self, value):
        self._queue.append(value)

    def deque(self):
        try:
            self.is_empty()
        except Exception:
            print("Index out of bounds")

        return self._queue.popleft()
