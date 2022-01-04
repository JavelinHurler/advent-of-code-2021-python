def parse_input():
    with open("input.txt") as file:
        return [line.replace(" ", "").replace("\n", "") for line in file.readlines()]

def devide(numbers, bit, get_common):
    assert get_common in [True, False]
    one, zero = 0, 0
    for number in numbers:
        assert number[bit] in ["0", "1"]
        if number[bit] == "0":
            zero += 1
        elif number[bit] == "1":
            one += 1

    if one >= zero:
        common, uncommon = "1", "0"
    elif one < zero:
        common, uncommon = "0", "1"

    return [number for number in numbers if number[bit] == {True : common, False : uncommon}[get_common]]

def to_base_ten(number):
    returner = 0
    for index, bit in enumerate(str(number)[::-1]):
        if bit == "1":
            returner += (2**index)
    return returner


if __name__ == "__main__":
    most_common = parse_input()
    least_common = most_common

    for bit in range(12):
        most_common = devide(most_common, bit, get_common=True)
        if len(most_common) == 1:
            break

    for bit in range(12):
        least_common = devide(least_common, bit, get_common=False)
        if len(least_common) == 1:
            break

    print(to_base_ten(most_common[0]) * to_base_ten(least_common[0]))
