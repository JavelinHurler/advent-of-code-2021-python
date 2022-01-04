def parse_input():
    with open("input.txt") as file:
        return file.readlines()

def solve(lines):
    return len([1 for index in range(len(lines) - 1) if int(lines[index]) < int(lines[index + 1])])

if __name__ == "__main__":
    lines = parse_input()
    print(solve(lines))
