# Standard Library imports
import ctypes

# Local imports
from array_iterator import ArrayIterator


class Array(object):

    def __init__(self, size):
        """
            Implements the array data structure in Python
        """
        assert size > 0, "ERROR!!! Array size must be greater than zero."

        self.array_size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize array.
        self.initialize_array(None)


    def __len__(self):
        """
            Returns the lenght of the array
        """
        return self.array_size


    def __get_item__(self, index):
        """
            Returns an element from a specific location
        """
        assert index >= 0 and index < len(self), "ERROR!!! Array subscript out of range."
        return self._elements[index]


    def __set_item__(self, index, value):
        """
            Sets an element to a specific position
        """
        assert index >= 0 and index < len(self), "ERROR!!! Array subscript out of range."
        self._elements[index] = value


    def initialize_array(self, value):
        """
            Initializes the array with specified value
        """
        for index in range(len(self)):
            self._elements[index] = value


    def __iter__(self):
        """
            Iterates through the array and returns all elements
        """
        return _ArrayIterator(self._elements)
