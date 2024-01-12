import math


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    return lines[0], {l[0:3]: {"L": l[7:10], "R": l[12:15]} for l in lines[2:]}


def part1(data):
    instructions, nodes = data
    current = "AAA"

    steps = 0
    while current != "ZZZ":
        current = nodes[current][instructions[steps % len(instructions)]]
        steps += 1

    return steps


def part2(data):
    instructions, nodes = data
    results = []

    for current in list(filter(lambda c: c[2] == "A", nodes)):
        steps = 0

        while current[2] != "Z":
            current = nodes[current][instructions[steps % len(instructions)]]
            steps += 1
        results.append(steps)

    return math.lcm(*results)


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    with open('input.txt') as f:
        puzzle_input = f.read()
    solution1, solution2 = solve(puzzle_input)
    print(f"{solution1}\n{solution2}")
