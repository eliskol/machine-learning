import sys
sys.path.append('../')


class Matrix:
    
    def __init__(self, rows):

        self.rows = rows
        self.num_cols = len(self.rows[0])
        self.num_rows = len(self.rows)


    def transpose(self):
        raw_transpose = []

        for entry in self.rows[0]:
            raw_transpose.append([])

        for i, row in enumerate(self.rows):
            for j, entry in enumerate(row):
                raw_transpose[j].insert(i, entry)

        return Matrix(raw_transpose)


    def print(self):
        for row in self.rows:
            print(row)


    def add(self, matrix_to_add):

        if self.num_cols != matrix_to_add.num_cols or self.num_rows != matrix_to_add.num_rows:
            print("invalid matrix dimensions")
            return("invalid matrix dimensions")

        output_matrix = []

        for i in range(self.num_rows):
            output_matrix.append([])

            for j in range(self.num_cols):
                output_matrix[i].append(self.rows[i][j] + matrix_to_add.rows[i][j])

        return Matrix(output_matrix)


    def subtract(self, matrix_to_subtract):
        if self.num_cols != matrix_to_subtract.num_cols or self.num_rows != matrix_to_subtract.num_rows:
            print("invalid matrix dimensions")
            return("invalid matrix dimensions")

        output_matrix = []

        for i in range(self.num_rows):
            output_matrix.append([])

            for j in range(self.num_cols):
                output_matrix[i].append(self.rows[i][j] - matrix_to_subtract.rows[i][j])

        return Matrix(output_matrix)


    def scalar_multiply(self, scalar):
        new_rows = [[entry * scalar for entry in row] for row in self.rows]
        return Matrix(new_rows)


    def matrix_multiply(self, matrix_to_multiply):

        output_matrix = []

        for i in range(self.num_rows):
            output_matrix.append([])

            for j in range(matrix_to_multiply.num_cols):
                output_matrix[i].append(0)
                
                for k in range(self.num_cols):
                    output_matrix[i][j] += self.rows[i][k] * matrix_to_multiply.rows[k][j]


        return Matrix(output_matrix)
    
    def crop_matrix(self, j):
        cropped_rows = list(self.rows)
        del cropped_rows[0]
        for row in cropped_rows:
            del row[j]
        return Matrix(cropped_rows)



    # def calc_determinant(self):







test = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(test.determinant())

test1 = Matrix([[1, 1], [1, 1], [1, 1]])
test2 = Matrix([[2, 2], [2, 2], [2, 2]])
print(test.crop_matrix(2).rows)
print(test.rows)