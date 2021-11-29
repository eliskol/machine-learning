class DataFrame:

    def __init__(self, data_dict, column_order):

        self.data_dict = data_dict
        self.column_order = column_order

        # there's probably an easier way to do this, but i can't think of it rn

        array_by_cols = []

        for col in self.column_order:
            array_by_cols.append(self.data_dict[col])

        self.row_array = [[0 for col in array_by_cols] for row in array_by_cols[0]]

        for i, col in enumerate(array_by_cols):
            for j, entry in enumerate(col):
                self.row_array[j][i] = array_by_cols[i][j]

    def to_array(self):
        return self.row_array

    def select_columns(self, columns_to_select):

        columns_to_return = {}

        for column in columns_to_select:
            columns_to_return[column] = self.data_dict[column]
        return DataFrame(columns_to_return, column_order=columns_to_select)

    def select_rows(self, rows_to_select):
        rows_to_return = []
        for row in rows_to_select:
            rows_to_return.append(self.row_array[row])
        return DataFrame(rows_to_return, column_order=self.column_order)
