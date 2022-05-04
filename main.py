
# Check if matrix is valid
def matrix_check():
    try:
        if len(matrix) == 9:
            for i in range(9):
                if len(matrix[i]) != 9:
                    return False
                for j in range(9):
                    if matrix[i][j] not in range(1,10):
                        return False

        else:
            return False
        return True
    except Exception as e:
        print(e)

#Check if row valid
def row_check():

    for i in range(9):
        dict = {}
        for ele in matrix[i]:
            try:
                dict[ele] += 1
            except:
                dict[ele] = 1

        for item in dict:

            # if frequency is more than 1
            if (dict[item] > 1):
                return False
    return True

#Check if column valid
def column_check():
    for i in range(9):
        dict = {}
        for j in range(9):
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False
    return True

#Check if square valid
def square_check():
    temp = []
    dict = {}
    # Top left square
    for i in range(3):
        for j in range(3):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False
    temp = []
    dict = {}
    # Top middle square
    for i in range(3):
        for j in range(3, 6):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False

    temp = []
    dict = {}
    # Top right square
    for i in range(3):
        for j in range(6, 9):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False

    temp = []
    dict = {}
    # Middle left square
    for i in range(3, 6):
        for j in range(3):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False

    temp = []
    dict = {}
    # Middle middle square
    for i in range(3, 6):
        for j in range(3, 6):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False

    temp = []
    dict = {}
    # Middle right square
    for i in range(3, 6):
        for j in range(6, 9):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False
    temp = []
    dict = {}
    # Bottle left square
    for i in range(6, 9):
        for j in range(3):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False
    temp = []
    dict = {}
    # Bottle middle square
    for i in range(6, 9):
        for j in range(3, 6):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False
    temp = []
    dict = {}
    # Bottle right square
    for i in range(6, 9):
        for j in range(6, 9):
            temp.append(matrix[i][j])
            try:
                dict[matrix[j][i]] += 1
            except:
                dict[matrix[j][i]] = 1
        for item in dict:
            if (dict[item] > 1):
                return False
    return True

#print matrix
def print_matrix():
    for i in matrix:
        for j in i:
            print(j, end =" ")
        print()



if __name__ == '__main__':

    # Take input put into an array
    matrix = []
    try:
        for i in range(9):
            matrix.append(list(map(int, input("Sudoku row {} : ".format(i+1)).strip().split())))
        print()
    except Exception as e:
        print(e)

    #Check if user input is valid
    valid = matrix_check()
    if valid == True:
        if row_check() and column_check() and square_check() == True:
            print('Solution Valid')
            print_matrix()
        else:
            print('Solution not Valid')
            print_matrix()
    else:
        print('User input is not valid')






