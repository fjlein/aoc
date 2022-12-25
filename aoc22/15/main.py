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
    pairs = set()
    sensors = set()
    beacons = set()
    for line in input.split("\n"):
        line = line.split(" ")
        sensor = (int(line[2][2:-1]), int(line[3][2:-1]))
        beacon = (int(line[8][2:-1]), int(line[9][2:]))
        sensors.add(sensor)
        beacons.add(beacon)
        pairs.add((sensor, beacon, manhatten(sensor, beacon)))
    return pairs, sensors, beacons


def manhatten(a, b):
    ax, ay = a
    bx, by = b
    return abs(by - ay) + abs(bx - ax)


def in_reach(point: (int, int), pairs) -> bool:
    for p in pairs:
        if manhatten(point, p[0]) <= p[2]:
            return True
    return False


def part1(pairs, sensors, beacons):
    y = 2000000

    yy = set()

    for p in pairs:
        sx, sy = p[0]
        dis = manhatten(p[0], p[1])
        if abs(sy - y) <= dis:
            d = abs(dis - abs(sy - y))
            for i in range(sx - d, sx + d + 1):
                yy.add((i, y))

    valid = yy - beacons - sensors

    return len(valid)


def part2(pairs):
    for p in pairs:
        (sx, sy), beacon, dis = p
        d = dis + 1
        for i in range(-d, d + 1):
            new_y = sy + i
            if not 0 <= new_y <= 4000000:
                continue
            new_x_1 = sx + abs(d - abs(i))
            new_x_2 = sx - abs(d - abs(i))
            if 0 <= new_x_1 <= 4000000:
                if not in_reach((new_x_1, new_y), pairs):
                    return new_x_1 * 4000000 + new_y
            if 0 <= new_x_2 <= 4000000:
                if not in_reach((new_x_2, new_y), pairs):
                    return new_x_2 * 4000000 + new_y
        print("added candidates")
    print("finished adding")


def solve(input, part):
    pairs, sensors, beacons = get_triplet(input)
    if part == 1:
        return part1(pairs, sensors, beacons)
    if part == 2:
        return part2(pairs)


print("answer 1:", solve(input, part=1))
print("answer 2:", solve(input, part=2))
