lines = []
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

sum1 = 0

for line in lines:
    a = 0
    first = False
    last = False
    while a < len(line):
        pre = line[a]
        suf = line[-a - 1]
        if not first and pre.isnumeric():
            first = pre[0]
        if not last and suf.isnumeric():
            last = suf[0]
        a = a + 1
    sum1 += int(first + last)

print(sum1)

sum2 = 0
for line in lines:
    a = 0
    first = False
    last = False
    while a < len(line):
        pre = line[a:]
        suf = line[-a - 1:]
        if not first:
            if pre[0].isnumeric():
                first = pre[0]
            else:
                for k, v in numbers.items():
                    if pre.startswith(k):
                        first = str(v)
        if not last:
            if suf[0].isnumeric():
                last = suf[0]
            else:
                for k, v in numbers.items():
                    if suf.startswith(k):
                        last = str(v)
        a = a + 1
    sum2 += int(first + last)

print(sum2)
