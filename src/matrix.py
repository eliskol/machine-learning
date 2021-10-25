# import sys
# sys.path.append('../')


class Matrix:
    
    def __init__(self, rows):

        self.rows = rows
        self.num_cols = len(self.rows[0])
        self.num_rows = len(self.rows)
        self.is_square = self.num_rows == self.num_cols


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

    def copy(self):
        return Matrix([[element for element in row] for row in self.rows])


    def crop_matrix(self, j):
        cropped_rows = self.copy().rows
        cropped_rows.pop(0)
        for i, row in enumerate(cropped_rows):
            cropped_rows[i].pop(j)
        return Matrix(cropped_rows)



    def calc_determinant_recursive(self):

        if self.num_rows != self.num_cols:
            return "invalid matrix dimensions (calc_determinant_recursive)"

        else:
            determinant = 0
            if self.num_rows == 2:
                determinant = (self.rows[0][0] * self.rows[1][1]) - (self.rows[0][1] * self.rows[1][0])
                return determinant
            
            else:
                determinant = 0
                for j, entry in enumerate(self.rows[0]):
                    cofactor = entry*((-1)**j)
                    trimmed_matrix = self.crop_matrix(j)
                    determinant += cofactor*trimmed_matrix.calc_determinant_recursive()

                return determinant


    def find_index_of_first_nonzero_of_row(self, i):
        for j in range(0, self.num_cols):
            if self.rows[i][j] != 0:
                return j
        return None

    def find_pivot_row_index_for_col(self, j):
        for i, row in enumerate(self.rows):
            if self.find_index_of_first_nonzero_of_row(i) == j:
                return i


    def swap_rows(self, a, b):
        # print('swapping rows ' + str(a) + ' and ' + str(b))
        self.rows[a], self.rows[b] = self.rows[b], self.rows[a]

    
    def scale_row(self, i, s):
        # print('scaling row with index ' + str(i))
        for col_index in range(0, self.num_cols):
            self.rows[i][col_index] *= s

    def clear_above(self, i, j):
        if i != 0:
            # print('clearing above row with index ' + str(i))
            for l in range(0, i):

                scalar = self.rows[l][j]

                for m in range(0, self.num_cols):

                    row_to_subtract_entry = self.rows[i][m]

                    current_entry = self.rows[l][m]

                    self.rows[l][m] -= scalar*row_to_subtract_entry
                    
                    if abs(current_entry) < 1e-14:
                        current_entry = 0


    def clear_below(self, i, j):
        # print('clearing below row with index ' + str(i) + ', j = ' + str(j))

        if i != self.num_rows-1:

            for l in range(i+1, self.num_rows):

                scalar = self.rows[l][j]

                # print(scalar)

                for m in range(0, self.num_cols):

                    self.rows[l][m] -= self.rows[i][m]*scalar

                    if abs(self.rows[l][m]) < 1e-14:
                        self.rows[l][m] = 0


    def clean(self):
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                if abs(round(self.rows[i][j], 10) - self.rows[i][j]) < 0.0000000000001:
                    self.rows[i][j] = round(self.rows[i][j], 10)
                if abs(self.rows[i][j]) < 1e-13:
                    self.rows[i][j] = 0

    def rref(self, for_determinant=False):
        mutable_matrix = self.copy()
        row_index = 0
        scales = []
        number_of_swaps = 0

        for col_index in range(0, self.num_cols):

            pivot_row_index = mutable_matrix.find_pivot_row_index_for_col(col_index)

            if pivot_row_index != None:

                if pivot_row_index != row_index:
                    mutable_matrix.swap_rows(pivot_row_index, row_index)
                    number_of_swaps += 1

                if mutable_matrix.rows[row_index][col_index] != 0:
                    scalar = 1/mutable_matrix.rows[row_index][col_index]
                    scales.append(1/scalar)
                    mutable_matrix.scale_row(row_index, 1/mutable_matrix.rows[row_index][col_index])

                mutable_matrix.clear_above(row_index, col_index)
                mutable_matrix.clear_below(row_index, col_index)

                mutable_matrix.clean()

                row_index += 1
        
        if for_determinant:
            return scales, number_of_swaps, mutable_matrix

        return mutable_matrix
        

    def create_identity(self):
        identity_rows = []

        for i in range(0, self.num_rows):
            identity_rows.append([0 for col in range(0, self.num_cols)])
            identity_rows[i][i] = 1
        
        return Matrix(identity_rows)

    def augment_matrix(self, matrix_to_augment):
        if self.num_rows != matrix_to_augment.num_rows: return "invalid dimensions"

        mutable_matrix = self.copy()

        for i in range(0, self.num_rows):
            mutable_matrix.rows[i] = self.rows[i] + matrix_to_augment.rows[i]
        
        return mutable_matrix


    def cut_matrix(self, side):

        mutable_matrix = self.copy()
        for i in range(0, self.num_rows):
                for j in range(0, int(self.num_cols/2)):
                    if side == "left":
                        del mutable_matrix.rows[i][0]
                    elif side == "right":
                        del mutable_matrix.rows[i][-1]

        # mutable_matrix.num_cols = int(self.num_cols/2)

        return Matrix(mutable_matrix.rows)


    def inverse(self):

        if self.num_cols != self.num_rows: return "invalid dimensions, need square matrix"

        mutable_matrix = self.copy()

        identity_matrix = mutable_matrix.create_identity()

        augmented_matrix = mutable_matrix.augment_matrix(identity_matrix)

        rref_augmented = augmented_matrix.rref()

        if rref_augmented.cut_matrix("right").rows != identity_matrix.rows:
            print("no inverse")
            return "no inverse"

        inverse = rref_augmented.cut_matrix("left")

        inverse.clean()

        return inverse

<<<<<<< HEAD

    def determinant_rref(self):

        if self.num_rows != self.num_cols: return "cant take determinant"

        determinant = 1

        scales, number_of_swaps, rrefed_form = self.rref(True)

        if rrefed_form.rows != self.create_identity().rows:
            return 0
        
        for scalar in scales:
            determinant *= scalar

        determinant *= (-1)**number_of_swaps

        return determinant
=======
    # this is a test btwe