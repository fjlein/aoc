def parse(puzzle_input):
    lines = [line.rstrip() for line in puzzle_input.split("\n")]

    data = []
    for line in lines:
        sets = line.split(": ")[1].split("; ")
        sets_in_numbers = []
        for s in sets:
            cubes = s.split(", ")
            cubes_in_numbers = [0, 0, 0]
            for c in cubes:
                if "red" in c:
                    cubes_in_numbers[0] = int(c.split()[0])
                if "green" in c:
                    cubes_in_numbers[1] = int(c.split()[0])
                if "blue" in c:
                    cubes_in_numbers[2] = int(c.split()[0])
            sets_in_numbers.append(cubes_in_numbers)
        data.append(sets_in_numbers)
    return data


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

    for game in data:
        r = max([s[0] for s in game])
        g = max([s[1] for s in game])
        b = max([s[2] for s in game])
        sum += r * g * b

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
