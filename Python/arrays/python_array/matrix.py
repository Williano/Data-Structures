from .two_d_array import Array2D


class Matrix:

    def __init__(self, num_of_rows, num_of_cols):
        self._matrix_grid = Array2D(num_of_rows, num_of_cols)
        self._matrix_grid.initialize_array(0)


