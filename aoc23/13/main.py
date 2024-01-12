from itertools import combinations


def parse(puzzle_input):
    return [pattern.split("\n") for pattern in puzzle_input.split("\n\n")]


def mirror(pattern):
    mirror_axis = set()
    for y in range(len(pattern) - 1):
        up, down = y + 1, len(pattern) - y - 1
        found = True
        for yy in range(min(up, down)):
            if pattern[y-yy] != pattern[y+yy+1]:
                found = False
                break
        if found:
            mirror_axis.add(y)
    return mirror_axis


def get_pattern_value(h, v):
    return (100 * (list(h)[0] + 1)) if len(h) > 0 else list(v)[0] + 1


def t(matrix):
    return list(zip(*matrix))


def part1(data):
    return sum(get_pattern_value(mirror(pattern), mirror(t(pattern))) for pattern in data)


def after_smudge_axis(pattern):
    og_h, og_v = mirror(pattern), mirror(t(pattern))
    for y, line in enumerate(pattern):
        for x, _ in enumerate(line):
            copy = [list(l) for l in pattern]
            copy[y][x] = "#" if pattern[y][x] == "." else "."
            h, v = mirror(copy) - og_h, mirror(t(copy)) - og_v
            if len(h) > 0 or len(v) > 0:
                return h, v


def part2(data):
    return sum(get_pattern_value(*after_smudge_axis(pattern)) for pattern in data)


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
