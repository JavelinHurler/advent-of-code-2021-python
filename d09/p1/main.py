def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()

    return [[int(col) for col in line.replace(" ", "").replace("\n", "")] for line in lines]

def get_left(matrix, row_index, col_index):
    if col_index - 1 < 0:
        return True
    else:
        return matrix[row_index][col_index - 1] > matrix[row_index][col_index]

def get_right(matrix, row_index, col_index):
    if col_index + 1 > 99:
        return True
    else:
        return matrix[row_index][col_index + 1] > matrix[row_index][col_index]

def get_up(matrix, row_index, col_index):
    if row_index - 1 < 0:
        return True
    else:
        return matrix[row_index - 1][col_index] > matrix[row_index][col_index]

def get_down(matrix, row_index, col_index):
    if row_index + 1 > 99:
        return True
    else:
        return matrix[row_index + 1][col_index] > matrix[row_index][col_index]


if __name__ == "__main__":
    matrix = parse_input()
    assert [len(matrix)] == list(set([len(row) for row in matrix]))

    lows = []

    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if get_left(matrix, row_index, col_index):
                if get_right(matrix, row_index, col_index):
                    if get_up(matrix, row_index, col_index):
                        if get_down(matrix, row_index, col_index):
                            lows.append(col)
    result = 0
    for low in lows:
        result += (1 + low)

    print(result)
