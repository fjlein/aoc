chars = {
    "|": [" X ", " X ", " X "],
    "-": ["   ", "XXX", "   "],
    "L": [" X ", " XX", "   "],
    "J": [" X ", "XX ", "   "],
    "7": ["   ", "XX ", " X "],
    "F": ["   ", " XX", " X "],
    ".": ["   ", " . ", "   "],
    "S": [" X ", "XXX", " X "],
}


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    matrix = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                start = (x*3+1, y*3+1)
            for i in range(3):
                for j in range(3):
                    matrix[(x*3+j, y*3+i)] = chars[char][i][j]
    return matrix, start, (len(lines[0])*3, len(lines)*3)


def get_loop(matrix, start):
    queue = [start]
    loop = {start: 0}

    while queue:
        x, y = queue.pop(0)
        for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            c = (x+d[0], y+d[1])
            if not c in loop and matrix.get(c) == "X":
                loop[c] = loop[(x, y)] + 1
                queue.append(c)

    return loop


def part1(data):
    matrix, start, _ = data
    return int((max(get_loop(matrix, start).values())) / 3)


def part2(data):
    matrix, start, (max_x, max_y) = data
    loop = set(get_loop(matrix, start))

    queue = [(0, 0)]
    outside = {(0, 0)}

    while queue:
        x, y = queue.pop(0)

        for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            dx, dy = d
            c = (x+dx, y+dy)
            if not c in outside and not c in loop and 0 <= c[0] <= max_x and 0 <= c[1] <= max_y:
                outside.add(c)
                queue.append(c)

    def filter_center(x):
        return (x[0]-1) % 3 == 0 and (x[1]-1) % 3 == 0

    reached_fields = list(filter(filter_center, loop.union(outside)))

    return int((max_x / 3) * (max_y / 3) - len(reached_fields))


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
