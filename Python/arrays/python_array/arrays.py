# Standard Library imports
import ctypes

# Local imports
from .array_iterator import ArrayIterator

class Array(object):
    """
    A class used to represent an Array

    ...

    Attributes
    ----------
    size : int
        an integer to set the size of the array

    Methods
    -------
    initialize_array(value)
        Initializes the array with specified value
    """

    def __init__(self, size):
        """
        Constructs all the necessary attributes for the array object.

        Parameters
        ----------
        size : int
         an integer to set the size of the array

        Raises
        ------
        LowArraySizeError
            If the array size is less than zero.
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
        Returns the size of the array

        Parameters
        ----------
        None

        Returns
        -------
        array_size: int
            Returns the array size
        """

        return self.array_size


    def __getitem__(self, index):
        """
        Returns an element from a specific location

        Parameters
        ----------
        index : int
            the index of the item or element

        Returns
        -------
        element: Python Object
            returns an element from a specific location

        Raises
        ------
        ArraySizeOutOfBoundsError
            If the array size is less than zero and greater than the size of the array.
        """

        assert index >= 0 and index < len(self), "ERROR!!! Array subscript out of range."
        return self._elements[index]


    def __setitem__(self, index, value):
        """
        Sets an element to a specific position

        Parameters
        ----------
        index : int
            the index to insert the item at.

        value : Python Object
            the value or element to add to the array

        Returns
        -------
        element: Python Object
            returns an element from a specific location

        Raises
        ------
        ArraySizeOutOfBoundsError
            If the array size is less than zero and greater than the size of the array.
        """

        assert index >= 0 and index < len(self), "ERROR!!! Array subscript out of range."
        self._elements[index] = value


    def initialize_array(self, value):
        """
        Initializes the array with specified value

        Parameters
        ----------
        value : Python Object
            the value to initialize the array with

        Returns
        -------
        None
        """

        for index in range(len(self)):
            self._elements[index] = value


    def __iter__(self):
        """
        Iterates through the array and returns all elements

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        return ArrayIterator(self._elements)
