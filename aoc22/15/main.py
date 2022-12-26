input = """Sensor at x=3907621, y=2895218: closest beacon is at x=3790542, y=2949630
Sensor at x=1701067, y=3075142: closest beacon is at x=2275951, y=3717327
Sensor at x=3532369, y=884718: closest beacon is at x=2733699, y=2000000
Sensor at x=2362427, y=41763: closest beacon is at x=2999439, y=-958188
Sensor at x=398408, y=3688691: closest beacon is at x=2275951, y=3717327
Sensor at x=1727615, y=1744968: closest beacon is at x=2733699, y=2000000
Sensor at x=2778183, y=3611924: closest beacon is at x=2275951, y=3717327
Sensor at x=2452818, y=2533012: closest beacon is at x=2733699, y=2000000
Sensor at x=88162, y=2057063: closest beacon is at x=-109096, y=390805
Sensor at x=2985370, y=2315046: closest beacon is at x=2733699, y=2000000
Sensor at x=2758780, y=3000106: closest beacon is at x=3279264, y=2775610
Sensor at x=3501114, y=3193710: closest beacon is at x=3790542, y=2949630
Sensor at x=313171, y=1016326: closest beacon is at x=-109096, y=390805
Sensor at x=3997998, y=3576392: closest beacon is at x=3691556, y=3980872
Sensor at x=84142, y=102550: closest beacon is at x=-109096, y=390805
Sensor at x=3768533, y=3985372: closest beacon is at x=3691556, y=3980872
Sensor at x=2999744, y=3998031: closest beacon is at x=3691556, y=3980872
Sensor at x=3380504, y=2720962: closest beacon is at x=3279264, y=2775610
Sensor at x=3357940, y=3730208: closest beacon is at x=3691556, y=3980872
Sensor at x=1242851, y=838744: closest beacon is at x=-109096, y=390805
Sensor at x=3991401, y=2367688: closest beacon is at x=3790542, y=2949630
Sensor at x=3292286, y=2624894: closest beacon is at x=3279264, y=2775610
Sensor at x=2194423, y=3990859: closest beacon is at x=2275951, y=3717327"""


def get_triplet(input):
    triplets = set()
    for line in input.split("\n"):
        line = line.split(" ")
        sensor = (int(line[2][2:-1]), int(line[3][2:-1]))
        beacon = (int(line[8][2:-1]), int(line[9][2:]))
        triplets.add((sensor, beacon, manhatten(sensor, beacon)))
    return triplets


def manhatten(a, b):
    return abs(b[1] - a[1]) + abs(b[0] - a[0])


def in_reach(point: (int, int), triplets) -> bool:
    for s, _, m in triplets:
        if manhatten(point, s) <= m:
            return True
    return False


def collapse_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            last = merged.pop()
            merged.append((last[0], max(last[1], interval[1])))
    return merged


def part1(triplets, given_y):
    intervals = []

    for (x, y), b, d in triplets:
        if abs(y - given_y) <= d:
            dx = abs(d - abs(y - given_y))
            intervals.append((x - dx, x + dx))

    intervals = collapse_intervals(intervals)
    beacon_candidates = {b[0] for (s, b, m) in triplets if b[1] == given_y}

    return sum([r - l + 1 - len(list(filter(lambda x: l <= x <= r, beacon_candidates))) for l, r in intervals])


def get_formula(a, b):
    x1, y1 = a
    x2, y2 = b
    m = (y2 - y1) / (x2 - x1)
    return m, y1 - m * x1


def get_intersect(u, w):
    # print("lines=", u, w)
    a, b = u
    c, d = w
    x = (d - b) / (a - c)
    y = a * x + b
    return x, y


def part2(triplets, max_size):
    down = set()
    up = set()
    for (x, y), _, m in triplets:
        d = m + 1
        # up
        up.add(get_formula((x - d, y), (x, y + d)))
        up.add(get_formula((x + d, y), (x, y - d)))
        # down
        down.add(get_formula((x - d, y), (x, y - d)))
        down.add(get_formula((x + d, y), (x, y + d)))
    for line1 in up:
        for line2 in down:
            x, y = get_intersect(line1, line2)
            if x.is_integer() and not in_reach((x, y), triplets):
                if 0 <= x <= max_size and 0 <= y <= max_size:
                    return int(x * 4000000 + y)


def solve(input, part):
    triplets = get_triplet(input)
    if part == 1:
        return part1(triplets, given_y=2000000)
    else:
        return part2(triplets, max_size=4000000)


print("answer 1:", solve(input, part=1))
print("answer 2:", solve(input, part=2))
