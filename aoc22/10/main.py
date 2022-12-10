input = """noop
noop
addx 5
addx 1
addx 10
addx -4
noop
addx -1
noop
addx 5
addx -5
addx 9
addx 2
addx -15
addx 18
addx 8
addx -2
noop
addx -18
addx 21
addx 1
addx -37
addx 27
addx -24
addx 2
addx 5
addx -7
addx 26
addx -16
addx 2
addx 5
addx -15
noop
addx 20
addx 2
addx 4
addx -3
addx 2
noop
addx 3
addx 2
addx 5
addx -40
addx 2
addx 33
addx -30
addx 5
addx 5
addx 17
addx -19
addx 2
addx 5
addx 20
addx -16
addx 3
addx -2
addx 7
noop
addx -2
addx 5
addx 2
addx 3
addx -2
addx -38
addx 5
addx 2
addx 1
addx 15
addx -8
noop
addx -2
addx 4
addx 2
addx 4
addx -2
noop
addx 6
addx 2
addx -1
addx 4
noop
addx 1
addx 4
noop
noop
noop
addx -37
addx 5
addx 2
addx 22
addx -17
addx -2
noop
addx 3
addx 2
noop
addx 3
addx 2
noop
noop
noop
addx 5
addx 5
addx 2
addx 3
noop
addx 2
addx -23
addx 2
addx -14
noop
addx 29
addx -26
noop
addx 8
noop
noop
noop
addx -9
addx 11
addx 5
addx 2
noop
addx 1
noop
noop
addx 5
noop
noop
addx 2
noop
addx 3
addx 2
addx -2
noop
noop
noop"""

input = input.split("\n")

V = 0
X = 1
s = 0

img = [[0]*40 for _ in range(6)]

for i in input:
    for j in range(len(i.split(" "))):

        sprite = [X-1, X, X+1]
        if V % 40 in sprite:
            img[V // 40][V % 40] = 1

        V += 1
        for k in [20, 60, 100, 140, 180, 220]:
            if V == k:
                s += (X*V)

    if i[0:4] == "addx":
        X += (int(i[5:]))

print("answer 1:", s)
print("answer 2:")
for row in img:
    for e in row:
        print("X" if e else " ", end="")
    print("")
