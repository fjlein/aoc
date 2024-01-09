from itertools import product
import re


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    data = []
    for line in lines:
        springs = line.split(" ")[0]
        groups = list(map(int, line.split(" ")[1].split(",")))
        data.append((springs, groups))
    return data


def part1(data):
    s = 0
    for springs, groups in data:
        springs = "?".join([springs for i in range(5)])
        groups = groups * 5
        print(springs, groups)

        print(2**springs.count("?"))

        valid_options = 0

        options = []
        for i in product("#.", repeat=springs.count("?")):
            option = list(springs.replace("?", "X"))
            for c in i:
                option[option.index("X")] = c
            if list(map(len, re.findall("#+", "".join(option)))) == groups:
                valid_options += 1

        s += valid_options
    return s


def part2(data):
    return 2


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
