def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()
    return [int(line) for line in lines]

def solve(lines):
    return sum([1 for index in range(len(lines) - 2) if sum(lines[index:index+3]) < sum(lines[index+1:index+4])])

if __name__ == "__main__":
    lines = parse_input()
    print(solve(lines))
