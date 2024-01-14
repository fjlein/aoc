import copy
import sys
import random


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    matrix = {}

    for y, line in enumerate(lines):
        for x, number in enumerate(line):
            matrix[(x, y)] = int(number)

    return matrix


def dijkstra(matrix, start):
    def straight_line_past(u, v):
        # print("check", v)
        try:

            if prev[prev[prev[u]]][0] == v[0] or prev[prev[prev[u]]][1] == v[1]:
                return True
        except KeyError:
            pass
            # print("check failed")
        return False
    dist = {}
    prev = {}
    Q = copy.deepcopy(matrix)
    # print(Q)

    dist[start] = 0

    while len(Q) != 0:
        u = min(Q, key=lambda x: dist.get(x) if x in dist else sys.maxsize)
        ux, uy = u
        # print("u", u)
        del Q[u]

        for (dx, dy) in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            neighbor = (ux + dx, uy + dy)
            try:
                alt = dist[u] + matrix[neighbor]
                if not neighbor in dist or alt < dist[neighbor]:

                    if straight_line_past(u, neighbor):
                        continue

                    dist[neighbor] = alt
                    prev[neighbor] = u
            except KeyError:
                pass  # out of bounds

    return dist[(12, 12)]


def part1(data):

    return dijkstra(data, (0, 0))


def pp(path):
    for y in range(13):
        for x in range(13):
            if (x, y) in path:
                print(".", end="")
            else:
                print("#", end="")
        print()
    print()


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
