import ctypes

class Array(object):

    def __init__(self, size):
        assert size > 0, "ERROR!!! Array size must be greater than zero."

        self.array_size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)


    def __len__(self):
        return self.array_size


    def __get_item__(self, index):
        assert index >= 0 and index < len(self), "ERROR!!! Array subscript out of range."
        return self._elements[index]


    def __set_item__(self, index, value):
        assert index >= 0 and index < len(self), "ERROR!!! Array subscript out of range."
        self._elements[index] = value


    def clear(self, value):
        for index in range(len(self)):
            self._elements[index] = value


    def __iter__(self):
        return __ArrayIterator(self._elements)
