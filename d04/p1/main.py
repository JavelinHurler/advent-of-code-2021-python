def parse_board(lines):
    return [[elem for elem in line.split(" ") if elem.replace(" ", "") != ""] for line in lines]

def parse_input():
    with open("input.txt") as file:
        lines = [line.replace("\n", "") for line in file.readlines()]

    inputs = lines[0].split(",")
    boards = []

    index = 1
    while index + 5 < len(lines):
        assert lines[index].replace(" ","") == ""
        boards.append(
            parse_board(
                lines[index+1:index+6]
            )
        )
        index += 6

    return inputs, boards

def check_row(board, row_index):
    return all([board[row_index][index] == None for index in range(5)])

def check_col(board, col_index):
    return all([board[index][col_index] == None for index in range(5)])

def play(number, boards):
    for board in boards:
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if (col != None) and (int(col) == int(number)):
                    board[row_index][col_index] = None
                    if check_row(board, row_index) or check_col(board, col_index):
                        return board
    return None

def count_result(board):
    return sum([sum([int(col) for col in row if col != None]) for row in board])

if __name__ == "__main__":
    inputs, boards = parse_input()

    for number in inputs:
        winning_board = play(number, boards)
        if winning_board != None:
            print(count_result(winning_board) * int(number))
            break
