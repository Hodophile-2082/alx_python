def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    max_width = max(len(str(num)) for row in matrix for num in row)

    for row in matrix:
        for num in row:
            if num < 0:
                print("{:d}".format(num), end=" " * (max_width - len(str(num)) + 1))
            else:
                print(" " * (max_width - len(str(num)) + 1), end="")
                print("{:d}".format(num), end=" ")
        print()