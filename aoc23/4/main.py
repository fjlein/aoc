import re
import math


def parse(puzzle_input):
    lines = [line.rstrip() for line in puzzle_input.split("\n")]

    data = []
    for line in lines:
        data.append([set(map(int, re.findall(" ..", l)))
                    for l in line.split(":")[1].split(" |")])
    return data


def part1(data):
    points = []

    for card in data:
        winning, my = card
        wins = len(set(filter(lambda x: x in winning, my)))
        points.append(math.floor(2**(wins - 1)))
    return sum(points)


def part2(data):
    scratchcards = [1 for i in range(len(data))]

    for i, card in enumerate(data):
        winning, my = card
        wins = len(set(filter(lambda x: x in winning, my)))
        for j in range(i + 1, i + wins + 1):
            scratchcards[j] += scratchcards[i]
    return sum(scratchcards)


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
