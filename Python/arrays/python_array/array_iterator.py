class ArrayIterator(object):

    def __init__(self, array):
        self._array_reference = array
        self._current_index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self._current_index < len(self._array_reference):
            element = self._array_reference[self._current_index]
            self._current_index += 1
            return element
        else:
            raise StopIteration