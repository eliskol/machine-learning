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

    def order_by(self, column_to_order_by, ascending):
        print(self.data_array)
        sorted_data = self.simple_sort_data(
            self.data_array,
            self.column_order.index(column_to_order_by),
            ascending=ascending,
        )
        return DataFrame.from_array(sorted_data, column_order=self.column_order)

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

    def find_index_of_min(self, arr, index):
        min_row = arr[0]

        for row in arr:
            if row[index] < min_row[index]:
                min_row = row

        return arr.index(min_row)

    def find_index_of_max(self, arr, index):
        max_row = arr[0]

        for row in arr:
            if row[index] > max_row[index]:
                max_row = row

        return arr.index(max_row)

    def simple_sort_data(self, data_to_sort, index_to_sort_by, ascending):
        output_data = []
        if ascending:
            for row in data_to_sort.copy():
                index_of_next_lowest = self.find_index_of_min(
                    data_to_sort, index_to_sort_by
                )
                output_data.append(data_to_sort[index_of_next_lowest])
                data_to_sort.pop(index_of_next_lowest)

        else:
            for row in data_to_sort.copy():
                index_of_next_highest = self.find_index_of_max(
                    data_to_sort, index_to_sort_by
                )
                output_data.append(data_to_sort[index_of_next_highest])
                data_to_sort.pop(index_of_next_highest)

        return output_data
