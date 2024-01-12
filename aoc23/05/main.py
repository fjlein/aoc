def parse(puzzle_input):
    seeds = [int(x) for x in puzzle_input.split("\n\n")[0].split(" ")[1:]]
    maps = []
    for category in puzzle_input.split("\n\n")[1:]:
        m = []
        for row in category.split("\n")[1:]:
            m.append([int(x) for x in row.split(" ")])
        m.sort(key=lambda x: x[1])
        maps.append(m)
    return seeds, maps


def part1(data):
    seeds, maps = data
    results = []
    for seed in seeds:
        for m in maps:
            for row in m:
                b, a, d = row
                if seed >= a and seed < a + d:
                    seed += b - a
                    break
        results.append(seed)
    return min(results)


def part2(data):
    seeds, maps = data
    ranges = []
    for i, s in enumerate(seeds[::2]):
        ranges.append((s, s+seeds[i*2+1] - 1))

    for m in maps:
        next_ranges = []
        while len(ranges) != 0:
            current = ranges.pop()
            s_from, s_to = current
            if s_from >= m[-1][1] + m[-1][2] or s_to < m[0][1]:
                next_ranges.append(current)
            for row in m:
                b, a, d = row
                if s_from >= a + d or s_to < a:
                    continue
                elif s_from >= a and s_to < a + d:
                    next_ranges.append((s_from + b - a, s_to + b - a))
                elif s_from >= a:
                    ranges.extend([(s_from, a + d - 1), (a + d, s_to)])
                elif s_to < a + d:
                    ranges.extend([(s_from, a - 1), (a, s_to)])
        ranges = next_ranges

    return sorted(ranges, key=lambda x: x[0])[0][0]


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
