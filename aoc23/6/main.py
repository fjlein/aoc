import re
import math


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    return [re.findall(r"\d+", l) for l in lines]


def part1(data):
    result = 1
    times, distances = data

    for i in range(len(times)):
        t, d = int(times[i]), int(distances[i])
        x1, x2 = t/2 + ((-t/2)**2-d)**(1/2), t/2 - ((-t/2)**2-d)**(1/2)
        low, high = sorted([x1, x2])
        if low.is_integer():
            low = int(low + 1)
        low = math.ceil(low)
        if high.is_integer():
            high = int(high - 1)
        high = math.floor(high)
        result *= high - low + 1

    return result


def part2(data):
    times, distances = data
    return part1((["".join(times)], ["".join(distances)]))


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
