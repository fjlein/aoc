import re
import math


def parse(puzzle_input):
    lines = [line.rstrip() for line in puzzle_input.split("\n")]

    data = []
    for line in lines:
        data.append([list(map(int, re.findall(" ..", l)))
                    for l in line.split(":")[1].split(" |")])
    return data


def part1(data):
    sum = 0

    for card in data:
        winning, my = card
        wins = list(filter(lambda x: x in winning, my))
        sum += math.floor(2**(len(wins) - 1))

    return sum


def part2(data):
    scratchcards = [1 for i in range(len(data))]

    for i, card in enumerate(data):
        winning, my = card
        l = len(list(filter(lambda x: x in winning, my)))
        for k in range(scratchcards[i]):
            for j in range(i + 1, i + l + 1):
                scratchcards[j] += 1
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
