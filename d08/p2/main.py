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

digit_segment_mapping = {
    "abcefg" : 0,
    "cf" : 1,
    "acdeg" : 2,
    "acdfg" : 3,
    "bcdf" : 4,
    "abdfg" : 5,
    "abdefg" : 6,
    "acf" : 7,
    "abcdefg" : 8,
    "abcdfg" : 9,
}

class row():
    def __init__(self, line):
        strips = line.replace("\n", "").split("|")

        assert len(strips) == 2

        self.signal_pattern = ["".join(sorted(digit)) for digit in strips[0].split(" ") if digit.replace(" ", "") != ""]
        self.output_pattern = ["".join(sorted(digit)) for digit in strips[1].split(" ") if digit.replace(" ", "") != ""]
        self.mapping = {
            "a" : None,
            "b" : None,
            "c" : None,
            "d" : None,
            "e" : None,
            "f" : None,
            "g" : None
        }

    def output_to_int(self):
        number = 0
        for digit in self.output_pattern:
            remapped_digit = ""
            for segment in digit:
                remapped_digit += self.mapping[segment]
            remapped_digit = "".join(sorted(remapped_digit))
            number *= 10
            number += digit_segment_mapping[remapped_digit]
        return number

def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()

    return [row(line) for line in lines if line.replace("\n", "").replace(" ", "") != ""]

def find_a(row):
    one, four, seven = None, None, None
    for digit in row.signal_pattern:
        if len(digit) == 2:
            one = digit
        elif len(digit) == 4:
            four = digit
        elif len(digit) == 3:
            seven = digit

    assert None not in [one, four, seven]

    return list(set(seven) - set(four))[0]

def get_bcef(row, a):
    count = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0
    }

    for digit in row.signal_pattern:
        for segment in digit:
            if segment != a:
                count[segment] += 1

    b. c, e, f = None, None, None, None

    for key, value in count.items():
        if value == 6:
            b = key
        elif value == 8:
            c = key
        elif value == 4:
            e = key
        elif value == 9:
            f = key

    assert None not in [b, c, e, f]

    return b, c, e, f

def get_dg(row, remainers, a):
    for digit in row.signal_pattern:
        if a not in digit:
            if remainers[0] in digit:
                return remainers[0] , remainers[1]
            if remainers[1] in digit:
                return remainers[1] , remainers[0]

def decode(row):
    a = find_a(row)
    b, c, e, f = get_bcef(row, a)
    row.mapping[a] = "a"
    row.mapping[b] = "b"
    row.mapping[c] = "c"
    row.mapping[e] = "e"
    row.mapping[f] = "f"
    remainers = [key for key, value in row.mapping.items() if value == None]

    assert len(remainers) == 2

    d, g = get_dg(row, remainers, a)
    row.mapping[d] = "d"
    row.mapping[g] = "g"

    assert None not in row.mapping.values()

    return row.output_to_int()

def solve(rows):
    return [decode(row) for row in rows]

if __name__ == "__main__":
    rows = parse_input()
    result = solve(rows)
    print(sum(result))
