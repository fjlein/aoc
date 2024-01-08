def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    return [list(map(int, l.split(" "))) for l in lines]


def part1(data):
    values = []

    for line in data:
        sub_lines = [line]
        while not all([x == 0 for x in sub_lines[-1]]):
            new_line = []
            for i in range(len(sub_lines[-1]) - 1):
                new_line.append(sub_lines[-1][i+1]-sub_lines[-1][i])
            sub_lines.append(new_line)
        sub_lines[-1].append(0)
        sub_lines.reverse()
        for r in range(len(sub_lines) - 1):
            sub_lines[r+1].append(sub_lines[r+1][-1] + sub_lines[r][-1])
        values.append(sub_lines[-1][-1])

    return sum(values)


def part2(data):
    values = []

    for line in data:
        sub_lines = [line]
        while not all([x == 0 for x in sub_lines[-1]]):
            new_line = []
            for i in range(len(sub_lines[-1]) - 1):
                new_line.append(sub_lines[-1][i+1]-sub_lines[-1][i])
            sub_lines.append(new_line)
        sub_lines[-1].append(0)
        sub_lines.reverse()
        for r in range(len(sub_lines) - 1):
            sub_lines[r+1].insert(0, sub_lines[r+1][0] - sub_lines[r][0])
        values.append(sub_lines[-1][0])

    return sum(values)


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
