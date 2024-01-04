import re
import math


def parse(puzzle_input):
    seeds = [int(x) for x in puzzle_input.split("\n\n")[0].split(" ")[1:]]
    maps = []
    for category in puzzle_input.split("\n\n")[1:]:
        m = []
        for row in category.split("\n")[1:]:
            m.append([int(x) for x in row.split(" ")])
        maps.append(m)
    return seeds, maps


def part1(data):
    seeds, maps = data
    results = []
    for seed in seeds:
        # print("seed:", seed)
        for m in maps:
            for row in m:
                dest, source, l = row
                offset = dest - source
                if seed >= source and seed <= source + l - 1:
                    seed += offset
                    break
            # print(seed)
        results.append(seed)
    return min(results)


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
