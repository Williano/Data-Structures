from .arrays import Array

class Array2D:


    def __init__(self, num_of_rows, num_of_cols):

        self._row_references = Array(num_of_rows)

        for row_reference in range(num_of_cols):
            self._row_references[row_reference] = Array(num_of_cols)


    def get_num_of_rows(self):
        return len(self._row_references)


    def get_num_of_columns(self):
        return len(self._row_references[0])


    def initialize_array(self, value):
        for row in range(self.get_num_of_rows()):
            row.initialize_array(value)


    def __getitem__(self, row_colum_index_tuple):

        self.check_row_and_column_index(row_colum_index_tuple)

        row = row_colum_index_tuple[0]
        column = row_colum_index_tuple[1]

        self.check_array_subscript_range(row, column)

        one_d_array = self._row_references[row]

        return one_d_array[column]


    def __setitem__(self, row_colum_index_tuple, value):

        self.check_row_and_column_index(row_colum_index_tuple)

        row = row_colum_index_tuple[0]
        column = row_colum_index_tuple[1]

        self.check_array_subscript_range(row, column)

        one_d_array = self._row_references[row]

        one_d_array[column] = value


    def check_array_subscript_range(self, row_index, column_index):

        assert row_index >= 0 and row_index < self.get_num_of_rows() and \
            column_index > 0 and column_index < self.get_num_of_columns(), "Array subscript out of range"


    def check_row_and_column_index(self, row_column_index):

        assert len(row_column_index) == 2, "Invalid number of array subscripts"
