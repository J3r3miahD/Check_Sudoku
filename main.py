# Check if matrix is valid
def matrix_check(matrix_data):
    try:
        if len(matrix_data) == 9:
            for row in matrix_data:
                if len(row) != 9:
                    return False
                for cell in row:
                    if cell not in range(1, 10):
                        return False
        else:
            return False
        return True
    except ValueError as value_error:  # Renamed exception to 'value_error' to avoid shadowing
        print(f"ValueError: {value_error}")
        return False

# Check if row is valid
def row_check(matrix_data):
    for row in matrix_data:
        count = {}
        for ele in row:
            count[ele] = count.get(ele, 0) + 1
            if count[ele] > 1:
                return False
    return True

# Check if column is valid
def column_check(matrix_data):
    for col_idx in range(9):
        count = {}
        for row in matrix_data:
            ele = row[col_idx]
            count[ele] = count.get(ele, 0) + 1
            if count[ele] > 1:
                return False
    return True

# Check if 3x3 square is valid
def square_check(matrix_data):
    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            count = {}
            for i in range(3):  # Renamed to avoid shadowing outer variable 'i'
                for j in range(3):
                    ele = matrix_data[row_start + i][col_start + j]
                    count[ele] = count.get(ele, 0) + 1
                    if count[ele] > 1:
                        return False
    return True

# Print matrix
def print_matrix(matrix_data):
    for row in matrix_data:
        print(" ".join(map(str, row)))

if __name__ == '__main__':

    # Take input put into an array
    sudoku_matrix = []
    try:
        for row_idx in range(9):  # Renamed to avoid shadowing outer variable 'i'
            sudoku_matrix.append(list(map(int, input(f"Sudoku row {row_idx + 1}: ").strip().split())))
        print()
    except ValueError as input_error:  # Renamed to 'input_error' to avoid shadowing
        print(f"ValueError: {input_error}")

    # Check if user input is valid
    if matrix_check(sudoku_matrix):
        if row_check(sudoku_matrix) and column_check(sudoku_matrix) and square_check(sudoku_matrix):
            print('Solution Valid')
            print_matrix(sudoku_matrix)
        else:
            print('Solution not Valid')
            print_matrix(sudoku_matrix)
    else:
        print('User input is not valid')
