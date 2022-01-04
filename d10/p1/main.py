def parse_input():
    with open("input.txt") as file:
        return file.readlines()

def check_line(line):
    stack = []
    line = line.replace("\n", "").replace(" ", "")

    for char in line:
        assert char in ["(", "<", "[", "{", ")", ">", "]", "}"]

        if char in ["(", "<", "[", "{"]:
            stack.append(char)
        elif char in [")", ">", "]", "}"]:
            top = stack.pop()
            needed_top = {
                ">" : "<",
                ")" : "(",
                "}" : "{",
                "]" : "["
            }[char]
            if top != needed_top:
                return {
                    ")" : 3,
                    "]" : 57,
                    "}" : 1197,
                    ">" : 25137
                }[char]
    return 0

if __name__ == "__main__":
    lines = parse_input()
    print(
        sum(
            [check_line(line) for line in lines]
        )
    )
