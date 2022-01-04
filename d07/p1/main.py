from statistics import median

def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()

    assert len(lines) == 1

    return [int(token) for token in lines[0].replace("\n","").replace(" ","").split(",")]

def solve(positions):
    return sum([abs(position - median(positions)) for position in positions])

if __name__ == "__main__":
    print(solve(parse_input()))
