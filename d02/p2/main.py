def parse_input():
    with open("input.txt") as file:
        return file.readlines()

def solve(lines):
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        if line[0:2].lower() == "up":
            temp = int(line[3:])
            aim -= temp
        elif line[0:4].lower() == "down":
            temp = int(line[5:])
            aim += temp
        elif line[0:7].lower() == "forward":
            temp = int(line[8:])
            horizontal += temp
            depth += (aim * temp)

    return horizontal * depth

if __name__ == "__main__":
    print(solve(parse_input()))
