input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


pair = set()


for line in input.split("\n"):
    line = line.split(" ")
    sensor = (int(line[2][2:-1]), int(line[3][2:-1]))
    beacon = (int(line[8][2:-1]), int(line[9][2:]))
    pair.add((sensor, beacon))

def manhatten(a, b):
    ax, ay = a
    bx, by = b
    return abs(by - ay) + abs(bx - ax)

print(manhatten((0, 11), (2, 10)))

y = 10

for p in pair:
    s = p[0]
    b = p[1]
    print(s,b)
    dis = manhatten(s,b)
