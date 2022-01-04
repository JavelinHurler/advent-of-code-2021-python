class Grid():
    def __init__(self, lines):
        self.grid = [[int(col) for col in line] for line in lines]
        self.flashes = 0

        assert len(list(set([len(row) for row in self.grid]))) == 1
        assert len(self.grid[0]) == len(self.grid)

    def __str__(self):
        result = ""
        for row in self.grid:
            for col in row:
                result += str(col) + " " * (4 - len(str(col)))
            result += "\n"
        return result

    def __increase_adjacent(self, row, col):
        self.__increase(row - 1, col - 1)
        self.__increase(row - 1, col)
        self.__increase(row - 1, col + 1)
        self.__increase(row, col - 1)
        self.__increase(row, col + 1)
        self.__increase(row + 1, col - 1)
        self.__increase(row + 1, col)
        self.__increase(row + 1, col + 1)

    def __increase(self, row, col):
        if row in list(range(len(self.grid))) and col in list(range(len(self.grid[row]))):
            self.grid[row][col] += 1
            if self.grid[row][col] == 10:
                self.flashes += 1
                self.__increase_adjacent(row, col)


    def step(self):
        for row_index, row in enumerate(self.grid):
            for col_index, col in enumerate(row):
                self.grid[row_index][col_index] += 1
                if self.grid[row_index][col_index] == 10:
                    self.flashes += 1
                    self.__increase_adjacent(row_index, col_index)

        for row_index, row in enumerate(self.grid):
            for col_index, col in enumerate(row):
                if self.grid[row_index][col_index] > 9:
                    self.grid[row_index][col_index] = 0

def parse_input():
    with open("input.txt") as file:
        return [line.replace(" ", "").replace("\n", "") for line in file.readlines()]

if __name__ == "__main__":
    grid = Grid(parse_input())
    for _ in range(100):
        grid.step()
    print("Total :", grid.flashes)
