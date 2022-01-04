from statistics import median

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
                return 0
    score = 0
    for elem in stack[::-1]:
        score *= 5
        score += {
            "(" : 1,
            "[" : 2,
            "{" : 3,
            "<" : 4
        }[elem]

    return score


if __name__ == "__main__":
    lines = parse_input()
    sorted_scores = sorted([check_line(line) for line in lines])

    sorted_scores = [elem for elem in sorted_scores if elem != 0]

    assert (len(sorted_scores) % 2) == 1

    print(median(sorted_scores))
