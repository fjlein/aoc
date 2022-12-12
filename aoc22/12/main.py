input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


print(input)

def transform(input):
    input = input.split("\n")
    m = []
    for row in input:
        r = []
        for c in row:
            if c == "S":
                r.append(0)
            elif c == "E":
                r.append(27)
            else:
                r.append(toNum(c))
        m.append(r)
    return m


def toNum(c):
    return ord(c)-96

def p(m):
    for r in m:
        print(r)

m = transform(input)
p(m)


def solve(m):
    for i in range(len(m)):
        if 0 in m[i]:
            y = i
            x = m[i].index(0)
    print(x, y)

solve(m)




    
