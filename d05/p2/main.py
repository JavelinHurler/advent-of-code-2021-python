def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()

    returner = []

    for line in lines:
        temp = line.replace("->", ",").replace(" ", "").replace("\n", "").split(",")
        returner.append({
            "x1" : int(temp[0]),
            "y1" : int(temp[1]),
            "x2" : int(temp[2]),
            "y2" : int(temp[3])
        })

    max_x = 0
    max_y = 0
    for line in returner:
        if line["x1"] > max_x:
            max_x = line["x1"]
        if line["x2"] > max_x:
            max_x = line["x2"]
        if line["y1"] > max_y:
            max_y = line["y1"]
        if line["y2"] > max_y:
            max_y = line["y2"]
    return returner, max_x, max_y

def make_matrix(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

def draw_lines(matrix, lines):
    for line in lines:
        distance_x = abs(line["x2"] - line["x1"])
        distance_y = abs(line["y2"] - line["y1"])
        if distance_x == distance_y:
            distance = distance_x
        elif distance_x == 0 and distance_y != 0:
            distance = distance_y
        elif distance_x != 0 and distance_y == 0:
            distance = distance_x

        for index in range(distance + 1):
            x = int(line["x1"] + (index * (line["x2"] - line["x1"]) / distance))
            y = int(line["y1"] + (index * (line["y2"] - line["y1"]) / distance))
            matrix[x][y] += 1

def count_larger_two(matrix):
    return sum([sum([1 for col in row if int(col) >= 2]) for row in matrix])

if __name__ == "__main__":
    lines, max_x, max_y = parse_input()

    matrix = make_matrix(
        max_x + 1,
        max_y + 1
    )

    draw_lines(matrix, lines)

    print(count_larger_two(matrix))
