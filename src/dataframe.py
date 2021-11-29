class DataFrame:

    def __init__(self, data_dict, column_order):

        self.data_dict = data_dict
        self.column_order = column_order
        self.num_cols = len(column_order)
        self.num_rows = len(self.data_dict[column_order[0]])

        self.data_array = [[] for row in self.data_dict[column_order[0]]]

        for column in column_order:
            for i in range(0, self.num_rows):
                self.data_array[i].append(self.data_dict[column][i])

    def to_array(self):
        return self.data_array

    def select_columns(self, columns_to_select):

        columns_to_return = {}

        for column in columns_to_select:
            columns_to_return[column] = self.data_dict[column]
        return DataFrame(columns_to_return, column_order=columns_to_select)

    def select_rows(self, rows_to_select):
        rows_to_return = []
        for row in rows_to_select:
            rows_to_return.append(self.data_array[row])
        return DataFrame.from_array(rows_to_return, self.column_order)

    @classmethod
    def from_array(cls, array, column_order):
        data_dict = dict(zip(column_order, array))
        print(data_dict)
        return cls(data_dict, column_order=column_order)
