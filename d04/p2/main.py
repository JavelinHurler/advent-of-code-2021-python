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
    returner = None
    deleter = []
    for board_index, board in enumerate(boards):
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if col != None:
                    if int(col) == int(number):
                        boards[board_index][row_index][col_index] = None
                        if check_row(board, row_index) or check_col(board, col_index):
                            deleter.append(board_index)
                            if len(boards) == len(deleter):
                                returner = board

    deleter.sort(reverse=True)
    for delete in deleter:
        del boards[delete]

    return returner

def count_result(board):
    return sum([sum([int(col) for col in row if col != None]) for row in board])

if __name__ == "__main__":
    inputs, boards = parse_input()

    for number in inputs:
        result = play(number, boards)
        if result != None:
            print(count_result(result) * int(number))
            break
