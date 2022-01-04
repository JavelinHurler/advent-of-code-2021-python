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

def region_growing(matrix, row_index, col_index, label):
    matrix[row_index][col_index] = label
    children = []
    if (row_index - 1) >= 0 :
        children.append([row_index - 1, col_index])
    if (row_index + 1) < 100 :
        children.append([row_index + 1, col_index])
    if (col_index - 1) >= 0 :
        children.append([row_index, col_index - 1])
    if (col_index + 1) < 100 :
        children.append([row_index, col_index + 1])

    for child in children:
        assert matrix[child[0]][child[1]] in [None, False, label]
        if matrix[child[0]][child[1]] == None:
            region_growing(matrix, child[0], child[1], label)

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
                            lows.append([row_index, col_index])

    matrix = [[None if col != 9 else False for col in row] for row in matrix]

    low_count = {}

    for low_index, low in enumerate(lows):
        low_count[low_index] = 0
        region_growing(matrix, low[0], low[1], low_index)

    for row in matrix:
        for col in row:
            assert col != None
            if col != False:
                low_count[col] += 1

    low_sorted = sorted(low_count.values())
    print(low_sorted[-1] * low_sorted[-2] * low_sorted[-3])
