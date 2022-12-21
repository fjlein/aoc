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

pairs = set()
sensors = set()
beacons = set()

for line in input.split("\n"):
    line = line.split(" ")
    sensor = (int(line[2][2:-1]), int(line[3][2:-1]))
    beacon = (int(line[8][2:-1]), int(line[9][2:]))
    sensors.add(sensor)
    beacons.add(beacon)
    pairs.add((sensor, beacon))


def manhatten(a, b):
    ax, ay = a
    bx, by = b
    return abs(by - ay) + abs(bx - ax)


print(manhatten((0, 11), (2, 10)))

y = 2000000

yy = set()

for p in pairs:
    print("check", p)
    sx, sy = p[0]
    bx, by = p[1]
    dis = manhatten(p[0], p[1])
    if abs(sy - y) <= dis:
        d = abs(dis - abs(sy - y))
        for i in range(sx - d, sx + d + 1):
            yy.add((i, y))

valid = yy - beacons - sensors

print("len", len(valid))
