# needed help on this one! learned a lot!
# credit goes to @xavdid and his post https://advent-of-code.xavd.id/writeups/2023/day/12/

import re
from functools import cache


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    data = []
    for line in lines:
        springs, raw_groups = line.split(" ")
        groups = tuple(map(int, re.findall(r"\d+", raw_groups)))
        data.append((springs, groups))
    return data


@cache
def num_valid_solutions(springs, groups):
    if len(springs) == 0:
        # if there are no more spots to check;
        # our only chance at success is if there are no `groups` left
        if len(groups) == 0:
            return 1
        return 0

    if len(groups) == 0:
        # if there are no more groups the only possibility of success is that there are no `#` remaining
        # here, `?` are treated as `.`, so no recursion is necessary
        if not "#" in springs:
            return 1
        return 0

    char, rest_of_springs = springs[0], springs[1:]

    if char == ".":
        return num_valid_solutions(rest_of_springs, groups)

    if char == "#":
        group = groups[0]
        # we're at the start of a group! make sure there are enough here to fill the first group
        # to be valid, we have to be:
        if (
            # long enough to match
            len(springs) >= group
            # made of only things that can be `#` (no `.`)
            and all(c != "." for c in springs[:group])
            # either at the end of the record (allowed)
            # or the next character isn't also a `#` (would be too big)
            and (len(springs) == group or springs[group] != "#")
        ):
            return num_valid_solutions(springs[group + 1:], groups[1:])
        return 0

    if char == "?":
        return num_valid_solutions(f"#{rest_of_springs}", groups) + num_valid_solutions(
            f".{rest_of_springs}", groups
        )


def part1(data):
    return sum([num_valid_solutions(springs, groups) for springs, groups in data])


def part2(data):
    return sum([num_valid_solutions("?".join([springs for i in range(5)]), groups*5) for springs, groups in data])


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
