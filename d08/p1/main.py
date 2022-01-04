#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# 0 : 6
# 1 : 2 -- cf
# 2 : 5
# 3 : 5
# 4 : 4 -- cbdf
# 5 : 5
# 6 : 6
# 7 : 3 -- acf
# 8 : 7 -- abcdef
# 9 : 6

class row():
    def __init__(self, line):
        strips = line.replace("\n", "").split("|")

        assert len(strips) == 2

        self.signal_pattern = [digit for digit in strips[0].split(" ") if digit.replace(" ", "") != ""]
        self.output_pattern = [digit for digit in strips[1].split(" ") if digit.replace(" ", "") != ""]

def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()

    return [row(line) for line in lines]

if __name__ == "__main__":
    count = 0
    tokens = parse_input()
    for token in tokens:
        for digit in token.output_pattern:
            if len(digit) in [2, 4, 3, 7]:
                count += 1
    print(count)
