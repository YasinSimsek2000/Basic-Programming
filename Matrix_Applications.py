def convert(matrix):
    columns = 0
    new_string = ""
    try:
        for i in matrix:
            if i == "]" or i == "[":
                columns += 0.5  # We find number of columns using this loop.
            else:
                new_string += i  # We pick over numbers from string.
    except TypeError:
        return matrix

    numbers_of_matrix = []
    rows = ""
    for i in new_string:
        if not i == ",":
            rows += i
        else:
            numbers_of_matrix = numbers_of_matrix + [float(rows)]
            rows = ""
    numbers_of_matrix += [float(rows)]  # And we convert numbers of matrix to integer/float inside list.

    matrix = []
    for i in range(columns):
        matrix += [[numbers_of_matrix[i * 3 + x] for x in range(columns)]]  # Finally, we create the matrix.
    return matrix


def printer(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print()
    return None


def addition(array1, array2):
    for row in range(len(array1)):
        for column in range(len(array1)):
            array1[row][column] = array1[row][column] + array2[row][column]
    return array1


def subtraction(array1, array2):
    for row in range(len(array1)):
        for column in range(len(array1)):
            array1[row][column] = array1[row][column] - array2[row][column]
    return array1


def multiply_matrices(array1, array2):
    if not len(array1[0]) == len(array2):
        print('You cannot multiply these matrices.')
        return None
    new_matrix = []
    for i in range(len(array1)):
        array = []
        for j in range(len(array2[0])):
            result = 0
            for k in range(len(array2)):
                result += array1[i][k] * array2[k][j]
            array += [result]
        new_matrix += [array]
    return new_matrix


def sorting(item):
    for i in range(len(item)):
        for j in range(len(item) - 1 - i):
            if item[j] > item[j + 1]:
                item[j], item[j + 1] = item[j + 1], item[j]
    return item


def add_lists(list1, list2):
    for i in range(len(list1)):
        list1[i] = list1[i] + list2[i]
    return list1


def multiply_list(list1, number):
    list2 = list1 + []
    for i in range(len(list2)):
        list2[i] = list2[i] * number
    return list2


def scalar_multiply(array1, number):
    for i in range(len(array1)):
        array1[i] = multiply_list(array1[i], number)
    return array1


def combination(x):
    global first_step, second_step, third_step
    first_step = []
    second_step = []
    third_step = []
    for i in range(x):
        for j in range(x):
            if i > j:
                first_step += [(j, i)]
            elif i == j:
                second_step += [(j, i)]
            else:
                third_step += [(j, i)]
    first_step = sorting(first_step)
    third_step = sorting(third_step)


def identity(number):  # We create an identity matrix to find inverse of this matrix.
    identity_matrix = [[0.0] * number for y in range(number)]
    for position in range(number):
        identity_matrix[position][position] = 1.0
    return identity_matrix


def inverse(matrix, item):
    if not len(matrix) == len(matrix[0]):
        print('Inverse matrix does not exist.')
        return None
    i_matrix = identity(len(matrix))
    combination(len(matrix))

    try:
        for point in first_step:
            number = -1 * matrix[point[1]][point[0]] / matrix[point[0]][point[0]]
            numbers = multiply_list(matrix[point[0]], number)
            matrix[point[1]] = add_lists(matrix[point[1]], numbers)

            numbers = multiply_list(i_matrix[point[0]], number)
            i_matrix[point[1]] = add_lists(i_matrix[point[1]], numbers)

        for point in second_step:
            number = 1 / matrix[point[0]][point[0]]
            matrix[point[0]] = multiply_list(matrix[point[0]], number)

            i_matrix[point[0]] = multiply_list(i_matrix[point[0]], number)

        for point in third_step[-1::-1]:
            number = -1 * matrix[point[1]][point[0]] / matrix[point[0]][point[0]]
            numbers = multiply_list(matrix[point[0]], number)
            matrix[point[1]] = add_lists(matrix[point[1]], numbers)

            numbers = multiply_list(i_matrix[point[0]], number)
            i_matrix[point[1]] = add_lists(i_matrix[point[1]], numbers)

        return i_matrix
    except Exception:
        print('Inverse matrix does not exist.')
        return None


def running(function, item1, item2):
    item1 = convert(item1)
    item2 = convert(item2)
    return function(item1, item2)


first = [[1, 1, 0], [1, -1, 2], [0, 2, 3]]
second = [[1, -1, -1], [2, -1, 3], [1, 4, 1]]
number = 4

print(running(addition, first, second))
print(running(subtraction, first, second))
print(running(multiply_matrices, first, second))
print(running(scalar_multiply, first, number))
print(running(inverse, first, second))
