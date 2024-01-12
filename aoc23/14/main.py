import copy


def parse(puzzle_input):
    return [[*line] for line in puzzle_input.split("\n")]


def tilt(matrix, d):
    matrix = copy.deepcopy(matrix)
    for y in range(len(matrix) - 1, -1, -1) if d == (0, 1) else range(len(matrix)):
        for x in range(len(matrix[0]) - 1, -1, -1) if d == (1, 0) else range(len(matrix[0])):
            pos = (x, y)
            if matrix[y][x] != "O":
                continue
            while 0 <= pos[1] + d[1] < len(matrix) and 0 <= pos[0] + d[0] < len(matrix[0]) and matrix[pos[1] + d[1]][pos[0] + d[0]] == ".":
                pos = (pos[0] + d[0], pos[1] + d[1])
            matrix[pos[1]][pos[0]] = matrix[y][x]
            if pos != (x, y):
                matrix[y][x] = "."
    return matrix


def get_matrix_value(matrix):
    return sum((len(matrix) - i) * line.count("O") for i, line in enumerate(matrix))


def part1(data):
    result_matrix = tilt(data, (0, -1))
    return get_matrix_value(result_matrix)


def apply_cycle(matrix):
    for d in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        matrix = tilt(matrix, d)
    return matrix


def part2(data):
    matrix = data
    record = []

    n = 0
    while True:
        matrix = apply_cycle(matrix)
        if matrix in record:
            first = record.index(matrix)
            result = (1000000000 - first - 1) % (n - first) + first
            return get_matrix_value(record[result])
        record.append(matrix)
        n += 1


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
