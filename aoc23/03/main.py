def parse(puzzle_input):
    lines = [line.rstrip() for line in puzzle_input.split("\n")]
    numbers, chars = dict(), set()
    x, y = 0, 0

    while y < len(lines[0]):
        x = 0
        while x < len(lines):
            if lines[y][x].isnumeric():
                number = ""
                coords = (x, y)
                while x < len(lines[0]) and y < len(lines) and lines[y][x].isnumeric():
                    number += lines[y][x]
                    x += 1
                numbers[coords] = number
            else:
                if lines[y][x] != ".":
                    chars.add((x, y))
                x += 1
        y += 1

    return chars, numbers, lines


def part1(data):
    chars, numbers, lines = data
    sum = 0

    for n in numbers:
        (x, y) = n
        neighbors = set([(x - 1, y), (x + len(numbers[(x, y)]), y)])
        for i in range(x - 1, x + len(numbers[(x, y)]) + 1):
            neighbors.update([(i, y - 1), (i, y + 1)])

        has_neighbor = False
        for neighbor in neighbors:
            if neighbor in chars:
                has_neighbor = True
                break
        if has_neighbor:
            sum += int(numbers[(x, y)])

    return sum


def part2(data):
    chars, numbers, lines = data
    new_numbers = dict()
    sum = 0

    for number in numbers:
        (x, y) = number
        for i in range(len(numbers[(x, y)])):
            new_numbers[(x + i, y)] = numbers[(x, y)]

    for char in chars:
        (x, y) = char
        if lines[y][x] != "*":
            continue

        neighbors = set()

        for n in set([(-1, -1), (0, -1), (1, -1), (-1, 1),
                      (0, 1), (1, 1), (-1, 0), (1, 0)]):
            neighbor = (x + n[0], y + n[1])
            if neighbor in new_numbers:
                neighbors.add(new_numbers[neighbor])

        if len(neighbors) == 2:
            a, b = list(neighbors)
            sum += int(a) * int(b)

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
