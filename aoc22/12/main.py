input = """abccccccccccccccccaaccccccccccccccccccccaaaaaaaaaaaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaa
abcccccccccccccaaaaaccccccccccccccccccccaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaa
abccccccccccccccaaaaaccccccccccccccaaaaacccaaaaaacccccaaccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaa
abccccccccccccccaaaaacccccccccaacccaaaaacccaaaaaaaccccaaaacaacaaccccccccccccccccccccccccaaaccccaaaccccccccccccaaaa
abcccccccccccccaaaaacccccccaaaaaccaaaaaacccaaaaaaaacaaaaaacaaaaaccccccccccccccccccccccccaaacccaaaaccccccccccccaaac
abccccccaacaaaccccaaccccccccaaaaacaaaaaaccaaaacaaaacaaaaaccaaaaaaccccccccccccccccccccccccaaaaaaaacccccccccccccaacc
abccccccaaaaaaccccccccccccccaaaaacaaaaaaccaaaaccaaaacaaaaacaaaaaacccccccccccccccccccccccaaaaaaaaaccccccccccccccccc
abccccccaaaaaacccccccccccccaaaaaccccaaccccaacccccaaccaacaacaaaaaccccccccccccccccccccccccccaaakkkkllllcccaaaccccccc
abccccccaaaaaaacccccccccccccccaaccccaacccccccccccccccccccccccaaaccccccaaaacccccccccjjjjkkkkkkkkkkllllccccaacaccccc
abcccccaaaaaaaacccccaaccccccccccccccaaaaaaccccccccccccccccccaaccccccccaaaaccccccccjjjjjkkkkkkkkkppllllcccaaaaacccc
abcccccaaaaaaaaccaaaacccccccccccccccaaaaaccccccccccccccccaacaaccccccccaaaacccccccjjjjjjjkkkkkppppppplllccaaaaacccc
abccccccccaaaccccaaaaaacccccccccccaaaaaaaccccccccccccccccaaaaacccccccccaacccccccjjjjoooooooppppppppplllcccaaaccccc
abccccccccaaccccccaaaaaccccaacccccaaaaaaaaccccaaacccccccccaaaaaaacccccccccccccccjjjooooooooppppuuppppllcccaaaccccc
abccccccaacccccccaaaaacccccaaaccaaaaaaaaaaccaaaaaaccccccaaaaaaaaaacaaaccccccccccjjjoooouuuoopuuuuupppllcccaaaccccc
abacccccaaccccccccccaacccccaaaaaaaccaaaaaaccaaaaaaccccccaaaaaccaaaaaaaccccaaccccjjoootuuuuuuuuuuuuvpqlllcccccccccc
abaccaaaaaaaacccccccccccccccaaaaaaccaacccccccaaaaacccccccacaaaccaaaaaaccaaaacaccjjooottuuuuuuuxyuvvqqljjccddcccccc
abcccaaaaaaaaccccccccccccaaaaaaaaacaacaaccccaaaaaccccccccccaaaaaaaaaacccaaaaaacciijootttxxxuuxyyyvvqqjjjjdddcccccc
abcccccaaaaccccaaacccccccaaaaaaaaacaaaaaccccaaaaaccccccccccccaaaaaaaaacccaaaaccciiinntttxxxxxxyyvvqqqqjjjddddccccc
abccccaaaaaccccaaaaacccccaaaaaaaaaaaaaaaaccccccccccccccccccccaaaaaaaaaaccaaaaccciiinntttxxxxxxyyvvvqqqqjjjdddccccc
abccccaaaaaaccaaaaaccccccccaaaaaaaaaaaaaacccccccccccccccccccccccaaacaaacaacaaccciiinnnttxxxxxyyyvvvvqqqqjjjdddcccc
SbccccaaccaaccaaaaacccccccccaaaaaaaaaaaaacccccccccccccccccccccccaaacccccccccccciiinnntttxxxEzzyyyyvvvqqqjjjdddcccc
abcccccccccccccaaaaacccccccaaaaaaaaacaaaccccccccccccccccccccccccaaccccccccccccciiinnnttxxxxyyyyyyyyvvvqqqjjjdddccc
abcccccccccccccaaccccccccccaaaaaaaaccccccccccccccccccccccccccccccccccccccccccciiinnntttxxyyyyyyyyyvvvvqqqjjjdddccc
abccccccccccccccccccccccccaaaaaaaacccccccccccccccccccccccccccccccccccccccccccciiinntttxxxwwwyyywwvvvvrqqjjjjdddccc
abcccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccccccccccccccccciinnntttxwwwwwyyywwvvvrrrqkkkeddcccc
abcccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccccccccccccccccchhnnntttsswwswwyywwrrrrrrkkkkeeecccc
abcccccccccccccccccccccccccccaaaaaacccccccccccccccccccaccccccccccccaaacccccccchhhnmmssssssswwwwwwrrrkkkkkeeeeecccc
abcccccccccccccccccccccccccccccaaacccccccccccccccccccaaccccccccccaaaaaacccccaahhhmmmmmsssssswwwwrrrkkkkkeeeeeccccc
abaacccccccccccccaccccccccccccccccccccccccccccccccaaaaacaacccccccaaaaaacaaaaaahhhhmmmmmmmmssswwwrrkkkkeeeeeacccccc
abacccccccccccccaaaaaaaaccccccccaaacccccccaaccccccaaaaaaaacccccccaaaaaacaaaaaaahhhhmmmmmmmmsssrrrrkkkeeeeeaacccccc
abaaaccccaaccccccaaaaaacccccccccaaacccaacaaaccccccccaaaacccccccccaaaaacccaaaaaaahhhhhhhmmmmlsssrrllkfeeeeaaaaacccc
abaaaccaaaaccccccaaaaaacccccccccaaaaaaaaaaaaaacccccaaaaacccccccccaaaaacccaaaaaaachhhhhgggmllsssrrllkffeaaaaaaacccc
abaacccaaaaaacccaaaaaaaacccccaaaaaaaaaaaaaaaaacccccaacaaacccccccccccccccaaaaaacccccchggggglllllllllfffaaaaaaaacccc
abaaccccaaaacccaaaaaaaaaaccccaaaaaaaaacaaaaaaaccaccaccaaacccccccccccccccaaaaaacccccccccgggglllllllffffaaaaaacccccc
abcccccaaaaacccaaaaaaaaaacccccaaaaaaaccaaaaacccaaaccccccccccccccccccccccccccaacccccccccagggglllllffffccccaaacccccc
abcccccaacaaccccccaaaaacaccaacccaaaaaaaaaaaaaccaaacccccccccccccccccccccccccccccccccccccaagggggffffffcccccccccccccc
abcccccccccccaaaaaaaaacccccaaccaaaaaaaccaaaaacaaaaccccccccccccccccccccccccccccccccccccaaaacgggfffffccccccccccccccc
abcccccccccccaaaaacaacccaaaaaaaaaaccaacccaaaaaaaacccaaccccccccccccccccccccccccccccccccccccccggfffccccccccccccaaaca
abccccccccccaaaaaaccccccaaaaaaaaacccccccccaaaaaaaaaaaacccccccccccccaaaccccccccccccccccccccccaaaccccccccccccccaaaaa
abccccccccccaaaaaaccccccccaaaacccccccccccccaaaaaaaaaaaaccccccccccccaaaaccccccccccccccccccccccaaaccccccccccccccaaaa
abcccccccccccaaaaacccccccaaaaaaccccccccccaaaaaaaaaaaaaaccccccccccccaaaaccccccccccccccccccccccccccccccccccccccaaaaa"""


class Entry():
    def __init__(self, score):
        self.score = score
        self.cost = 0
        self.path = []


def to_num(c):
    return ord(c) - 96


def transform(input):
    input = input.split("\n")
    m = []
    ex = None
    ey = None
    for i in range(len(input)):
        r = []
        for j in range(len(input[0])):
            if input[i][j] == "S":
                r.append(Entry(1))
                # print("S", j, i)
            elif input[i][j] == "E":
                r.append(Entry(26))
                # print("E", j, i)
            else:
                r.append(Entry(to_num(input[i][j])))
        m.append(r)
    return m



def solve(input, part):
    sx = 0
    sy = 20

    m = transform(input)

    def bfs(part):
        # m = transform(input)
        queue = []
        for i in range(len(m)):
            for j in range(len(m[0])):
                if part == 1:
                    # print("part1")
                    queue.append([0, 20])
                else:
                    # print("part2")
                    if m[i][j].score == 1:
                        queue.append([j, i])

        seen = []
        print(len(queue))
        while queue:
            point = queue.pop(0)
            x, y = point
            if point in seen:
                continue
            seen.append(point)
            if point == [91, 20]:
                return m[20][91].cost

            ways = []
            # left
            if x > 0 and (m[y][x - 1].score <= m[y][x].score + 1):
                ways.append([x - 1, y])
            # right
            if x < len(m[1]) - 1 and (m[y][x + 1].score <= m[y][x].score + 1):
                ways.append([x + 1, y])
            # print("up check")
            if y > 0 and (m[y - 1][x].score <= m[y][x].score + 1):
                ways.append([x, y - 1])
            # down
            if y < len(m) - 1 and (m[y + 1][x].score <= m[y][x].score + 1):
                ways.append([x, y + 1])

            # print("w", ways)
            for way in ways:
                wx, wy = way
                if not way in queue:
                    m[wy][wx].cost = m[y][x].cost + 1
                    queue.append(way)

    return bfs(part)


print("answer 1:", solve(input, part=1))
print("answer 1:", solve(input, part=2))
