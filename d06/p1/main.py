def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()

    assert len(lines) == 1

    return [int(token) for token in lines[0].replace("\n","").replace(" ","").split(",")]

def step_through_life(tokens):
    spawn_count = 0
    for index, token in enumerate(tokens):
        if token == 0:
            tokens[index] = 6
            spawn_count += 1
        else:
            tokens[index] -= 1
    for _ in range(spawn_count):
        tokens.append(8)
    return tokens

if __name__ == "__main__":
    tokens = parse_input()
    for _ in range(80):
        tokens = step_through_life(tokens)
    print(len(tokens))
