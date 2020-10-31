from .two_d_array import Array2D


class Matrix:

    def __init__(self, num_of_rows, num_of_cols):
        self._matrix_grid = Array2D(num_of_rows, num_of_cols)
        self._matrix_grid.initialize_array(0)

    def get_number_of_rows(self):
        return self._matrix_grid.get_num_of_rows()

    def get_number_of_columns(self):
        return self._matrix_grid.get_num_of_columns()

    def __getitem__(self, row_colum_index_tuple):
        return self._matrix_grid[
            row_colum_index_tuple[0],
            row_colum_index_tuple[1]
            ]

    def __setitem__(self, row_colum_index_tuple, scalar):
        self._matrix_grid[
            row_colum_index_tuple[0],
            row_colum_index_tuple[1]
            ] = scalar
