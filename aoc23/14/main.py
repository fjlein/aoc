def parse(puzzle_input):
    matrix = {}
    for y, line in enumerate(puzzle_input.split("\n")):
        for x, char in enumerate(line):
            matrix[(x, y)] = char
    return matrix, len(puzzle_input.split("\n")[0]), len(puzzle_input.split("\n"))


def part1(data):
    matrix, size_x, size_y = data
    for y in range(size_y):
        for x in range(size_x):
            pos = (x, y)
            print("cur", pos, matrix.get(pos))
            if matrix.get(pos) != "O":
                continue
            while pos[1] > 0 and matrix.get((x, pos[1] - 1)) == ".":
                pos = (x, pos[1] - 1)
            matrix[pos] = matrix[(x, y)]
            if pos != (x, y):
                matrix[(x, y)] = "."

    return sum(size_y - y if matrix[((x, y))] == "O" else 0 for (x, y) in matrix)


def part2(data):
    return "part2"


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
