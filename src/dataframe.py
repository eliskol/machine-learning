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
    def from_array(cls, row_array, column_order):
        column_array = cls.row_array_to_column_array(cls, row_array)
        data_dict = dict(zip(column_order, column_array))
        return cls(data_dict, column_order=column_order)

    def row_array_to_column_array(self, row_array):
        column_array = [[0 for row in row_array] for el in row_array[0]]
        for i in range(0, len(row_array)):
            for j in range(0, len(row_array[0])):
                column_array[j][i] = row_array[i][j]
        return column_array

    # def order_by(self, column_to_order_by, ascending):
    #     if type(self.data_dict[column_to_order_by][0]) is int:
    #         for row in

    def to_json(self):
        json_to_return = [{} for row in self.data_array]
        for column in self.column_order:
            for i in range(0, len(self.data_array)):
                json_to_return[i][column] = self.data_dict[column][i]
        return json_to_return

    @classmethod
    def from_json(cls, json, column_order):
        data_dict = {column: [] for column in column_order}
        for row in json:
            for column in column_order:
                data_dict[column].append(row[column])
        return cls(data_dict, column_order=column_order)
