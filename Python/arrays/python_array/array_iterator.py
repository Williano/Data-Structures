class ArrayIterator(object):
    """
    A class used to represent an Array Iterator

    ...

    Attributes
    ----------
    None

    Methods
    -------
    None
    """

    def __init__(self, array):
        """
        Constructs all the necessary attributes for the array iterator object.

        Parameters
        ----------
        array : Python Objects
         an array of python objects

        """

        self._array_reference = array
        self._current_index = 0


    def __iter__(self):
        """
        Returns an instance of the object.

        Parameters
        ----------
        None

        Returns
        -------
        array_object: Python Object
            returns an instance of the array

        """

        return self


    def __next__(self):
        """
        Returns the next object in the array.

        Parameters
        ----------
        None

        Returns
        -------
        array_object: Python Object
            returns an instance of the array

        Raises
        -------
        EndOfIterationErro:
            if the size of the array is reached, it returns an error.

        """

        if self._current_index < len(self._array_reference):
            element = self._array_reference[self._current_index]
            self._current_index += 1
            return element
        else:
            raise StopIteration