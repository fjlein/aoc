def parse(puzzle_input):
    lines = [line.rstrip() for line in puzzle_input.split("\n")]

    res = []
    for line in lines:
        sets = line.split(": ")[1].split("; ")
        set_result = []
        for s in sets:
            cubes = s.split(", ")
            x = [0, 0, 0]
            for c in cubes:
                if "red" in c:
                    x[0] = int(c.split()[0])
                if "green" in c:
                    x[1] = int(c.split()[0])
                if "blue" in c:
                    x[2] = int(c.split()[0])
            set_result.append(x)
        res.append(set_result)
    return res


def part1(data):
    maxes = [12, 13, 14]

    sum = 0

    for i, game in enumerate(data):
        possible = True
        for s in game:
            if s[0] > maxes[0] or s[1] > maxes[1] or s[2] > maxes[2]:
                possible = False
                break
        if possible:
            sum += i + 1

    return sum


def part2(data):
    sum = 0

    for i, game in enumerate(data):
        sum += max([s[0] for s in game]) * max([s[1]
                                                for s in game]) * max([s[2] for s in game])

    return sum


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
