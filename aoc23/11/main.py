from itertools import combinations


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    galaxies = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.add((x, y))

    spaces_y = [line.count("#") for line in lines]
    spaces_x = [[l[i] for l in lines].count(
        "#") for i, _ in enumerate(lines[0])]

    return galaxies, spaces_x, spaces_y


def manhatten(a, b):
    return abs(a[1] - b[1]) + abs(a[0] - b[0])


def expand_universe(galaxies, spaces_x, spaces_y, n):
    new_galaxies = set()

    for (x, y) in galaxies:
        new_x = spaces_x[0:x].count(0) * n + x - spaces_x[0:x].count(0)
        new_y = spaces_y[0:y].count(0) * n + y - spaces_y[0:y].count(0)
        new_galaxies.add((new_x, new_y))

    return new_galaxies


def part1(data):
    new_galaxies = expand_universe(*data, n=2)
    return sum([manhatten(a, b) for (a, b) in list(combinations(new_galaxies, 2))])


def part2(data):
    new_galaxies = expand_universe(*data, n=1000000)
    return sum([manhatten(a, b) for (a, b) in list(combinations(new_galaxies, 2))])


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
