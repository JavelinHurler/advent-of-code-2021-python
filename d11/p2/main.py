class Node():
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

class Graph():
    def __init__(self, edges):
        self.edges = []


def parse_input():
    with open("input.txt") as file:
        return [line.replace(" ", "").replace("\n", "") for line in file.readlines()]

if __name__ == "__main__":
    graph = Graph(parse_input())
    x = 0
    while(True):
        grid.step()
        x += 1
        if grid.all_flashed() == True:
            break

    print(x)
