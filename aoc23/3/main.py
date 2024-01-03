def parse(puzzle_input):
    lines = [line.rstrip() for line in puzzle_input.split("\n")]
    numbers, chars = set(), set()
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
                numbers.add((coords, number))
            else:
                if lines[y][x] != ".":
                    chars.add(((x, y), lines[y][x]))
                x += 1
        y += 1
    return chars, numbers


def part1(data):
    chars, numbers = data
    char_positions = [(x, y) for ((x, y), _) in chars]
    sum = 0
    for n in numbers:
        (x, y), number = n
        neighbors = set([(x - 1, y), (x + len(number), y)])
        for i in range(x - 1, x + len(number) + 1):
            neighbors.add((i, y - 1))
            neighbors.add((i, y + 1))

        has_neighbor = False
        for neighbor in neighbors:
            if neighbor in char_positions:
                has_neighbor = True
                break
        if has_neighbor:
            sum += int(number)
    return sum


def part2(data):
    chars, numbers = data
    new_numbers = set()
    for number in numbers:
        (x, y), n = number
        for i in range(len(n)):
            new_numbers.add(((x + i, y), n))

    new_numbers_coords = {(x, y) for ((x, y), _) in new_numbers}

    sum = 0

    for char in chars:
        (x, y), c = char
        if c != "*":
            continue
        neighbor_numbers = set()
        neighbors = set([(-1, -1), (0, -1), (1, -1), (-1, 1),
                        (0, 1), (1, 1), (-1, 0), (1, 0)])

        for neighbor in neighbors:
            nx, ny = neighbor
            if (x + nx, y + ny) in new_numbers_coords:

                n = list(filter(lambda n: n[0][0] == x +
                                nx and n[0][1] == y + ny, new_numbers))[0]
                neighbor_numbers.add(n[1])
        if len(neighbor_numbers) == 2:
            a, b = list(neighbor_numbers)
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
