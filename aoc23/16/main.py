def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    matrix = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            matrix[(x, y)] = char

    return matrix, len(lines[0]), len(lines)


def shoot_beam(matrix, beam):
    visited = set()
    beams = [beam]

    while len(beams) != 0:
        ((x, y), (dx, dy)) = beams.pop()
        nxt = (x + dx, y + dy)

        if not nxt in matrix:
            continue

        next_char = matrix[(nxt)]

        if nxt in visited and next_char in ("-", "|"):
            continue
        if next_char == "." or (next_char == "|" and dx == 0) or (next_char == "-" and dy == 0):
            beams.append((nxt, (dx, dy)))
        match next_char:
            case "\\":
                beams.append((nxt, (dy, dx)))
            case "/":
                beams.append((nxt, (dy * -1, dx * -1)))
            case "|":
                if dx != 0:
                    beams += [(nxt, (0, 1)), (nxt, (0, -1))]
            case "-":
                if dy != 0:
                    beams += [(nxt, (1, 0)), (nxt, (-1, 0))]
        if nxt in matrix:
            visited.add(nxt)

    return len(visited)


def part1(data):
    matrix = data[0]
    return shoot_beam(matrix, ((-1, 0), (1, 0)))


def part2(data):
    matrix, max_x, max_y = data

    beams = set()
    for x in range(max_x + 1):
        beams.update([((x, -1), (0, 1)), ((x, max_y + 1), (0, -1))])
    for y in range(max_y + 1):
        beams.update([((-1, y), (1, 0)), ((max_x + 1, y), (-1, 0))])

    return max(shoot_beam(matrix, beam) for beam in beams)


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
