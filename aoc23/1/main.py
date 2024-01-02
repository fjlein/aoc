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
        a = 0
        first = False
        last = False
        while a < len(line):
            pre = line[a]
            suf = line[-a - 1]
            if not first and pre.isnumeric():
                first = pre[0]
            if not last and suf.isnumeric():
                last = suf[0]
            a = a + 1
        sum += int(first + last)

    return sum


def part2(data):
    sum = 0
    for line in data:
        a = 0
        first = False
        last = False
        while a < len(line):
            pre = line[a:]
            suf = line[-a - 1:]
            if not first:
                if pre[0].isnumeric():
                    first = pre[0]
                else:
                    for k, v in numbers.items():
                        if pre.startswith(k):
                            first = str(v)
            if not last:
                if suf[0].isnumeric():
                    last = suf[0]
                else:
                    for k, v in numbers.items():
                        if suf.startswith(k):
                            last = str(v)
            a = a + 1
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
