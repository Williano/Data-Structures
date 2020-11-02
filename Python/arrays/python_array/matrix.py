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

    def scale_matrix(self, scalar):
        for row in range(self.get_number_of_rows()):
            for column in range(self.get_number_of_columns()):
                self[row, column] *= scalar

    def transpose_matrix(self, scalar):
        pass

    def __add__(self, right_handside_matrix):
        assert right_handside_matrix.get_num_of_rows() == \
            self.get_number_of_rows() and \
            right_handside_matrix.get_num_of_columns() == \
            self.get_number_of_columns(), "Matrix sizes not compatible\
            for the add operation."

        new_matrix = Matrix(self.get_number_of_rows,
                            self.get_number_of_columns)

        for row in range(self.get_number_of_rows()):
            for column in range(self.get_number_of_columns()):
                new_matrix[row, column] = self[row, column] + \
                    right_handside_matrix[row, column]
        return new_matrix

    def __sub__(self, right_handside_matrix):
        pass

    def __mul__(self, right_handside_matrix):
        pass
