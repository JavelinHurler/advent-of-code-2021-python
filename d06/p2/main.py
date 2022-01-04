class Population():
    def __init__(self, tokens):
        self.count = [0] * 9
        for token in tokens:
            self.count[token] += 1

    def get_count(self):
        return sum(self.count)

    def step(self):
        temp = self.count[0]
        self.count[0] = self.count[1]
        self.count[1] = self.count[2]
        self.count[2] = self.count[3]
        self.count[3] = self.count[4]
        self.count[4] = self.count[5]
        self.count[5] = self.count[6]
        self.count[6] = self.count[7]
        self.count[7] = self.count[8]
        self.count[8] = temp
        self.count[6] += temp

    def __repr__(self):
        return f"""
            0 : {self.count[0]}
            1 : {self.count[1]}
            2 : {self.count[2]}
            3 : {self.count[3]}
            4 : {self.count[4]}
            5 : {self.count[5]}
            6 : {self.count[6]}
            7 : {self.count[7]}
            8 : {self.count[8]}
        """

def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()

    assert len(lines) == 1

    return [int(token) for token in lines[0].replace("\n","").replace(" ","").split(",")]

if __name__ == "__main__":
    population = Population(parse_input())
    for _ in range(256):
        population.step()
    print(population.get_count())
