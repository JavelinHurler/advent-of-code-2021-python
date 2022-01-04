def parse_input():
    with open("input.txt") as file:
        return file.readlines()

def solve(lines):
    horizontal = 0
    depth = 0

    for line in lines:
        if line[0:2].lower() == "up":
            depth -= int(line[3:])
        elif line[0:4].lower() == "down":
            depth += int(line[5:])
        elif line[0:7].lower() == "forward":
            horizontal += int(line[8:])

    return depth * horizontal


if __name__ == "__main__":
    print(solve(parse_input()))
