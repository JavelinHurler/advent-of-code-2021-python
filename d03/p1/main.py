def parse_input():
    with open("input.txt") as file:
        return file.readlines()

def solve(lines):
    mask = []

    for line in lines:
        line = line.replace("\n","")
        for index, bit in enumerate(line):
            assert bit in ["0", "1"]
            if index >= len(mask):
                mask.append(0)
            if bit == "0":
                mask[index] -= 1
            elif bit == "1":
                mask[index] += 1

    gamma_most_used = 0
    epsilon_least_used = 0

    for index, bit in enumerate(mask[::-1]):
        bit = int(bit)
        assert bit != 0
        if bit < 0:
            gamma_most_used += 2**index
        elif bit > 0:
            epsilon_least_used += 2**index

    return gamma_most_used * epsilon_least_used

if __name__ == "__main__":
    print(solve(parse_input()))
