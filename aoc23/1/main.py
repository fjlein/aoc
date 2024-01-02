numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    return [line.rstrip() for line in lines]


def part1(data):
    sum = 0

    for line in data:
        first = False
        last = False
        for i in range(len(line)):
            if not first and line[i].isnumeric():
                first = line[i]
            if not last and line[-i - 1].isnumeric():
                last = line[-i - 1]
        sum += int(first + last)

    return sum


def part2(data):
    sum = 0

    for line in data:
        first = False
        last = False
        for i in range(len(line)):
            if not first:
                if line[i:][0].isnumeric():
                    first = line[i:][0]
                else:
                    for k, v in numbers.items():
                        if line[i:].startswith(k):
                            first = str(v)
            if not last:
                if line[-i - 1:][0].isnumeric():
                    last = line[-i - 1:][0]
                else:
                    for k, v in numbers.items():
                        if line[-i - 1:].startswith(k):
                            last = str(v)
        sum += int(first + last)

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
