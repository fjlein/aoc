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
        for m in maps:
            for row in m:
                dest, source, l = row
                if seed >= source and seed < source + l:
                    seed += dest - source
                    break
        results.append(seed)
    return min(results)


def part2(data):
    seeds, maps = data
    ranges = []
    for i, s in enumerate(seeds[::2]):
        ranges.append((s, s+seeds[i*2+1] - 1))

    print(ranges)

    for m in maps:
        next_ranges = []
        print("map", m)
        print("ranges", ranges)
        while len(ranges) != 0:
            current = ranges.pop()
            seed_from, seed_to = current
            print("current:", current)
            start_in_map = False
            for row in m:
                dest, source, l = row
                if seed_from >= source and seed_from < source + l:  # range start is in map
                    start_in_map = True
                    if seed_to < source + l:  # completely in map
                        next_ranges.append(
                            (seed_from + dest - source, seed_to + dest - source))
                    else:  # partial in map
                        next_ranges.append(
                            seed_from + dest - source, source + l - 1 + dest - source)
                        ranges.append((source + l, seed_to))
            if not start_in_map:  # range start is not in any map
                # map one to one until first start of map
                print("hi")

        ranges = next_ranges
        print(ranges)

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
