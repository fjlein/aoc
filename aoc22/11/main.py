input = """Monkey 0:
  Starting items: 85, 77, 77
  Operation: new = old * 7
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 7

Monkey 1:
  Starting items: 80, 99
  Operation: new = old * 11
  Test: divisible by 3
    If true: throw to monkey 3
    If false: throw to monkey 5

Monkey 2:
  Starting items: 74, 60, 74, 63, 86, 92, 80
  Operation: new = old + 8
  Test: divisible by 13
    If true: throw to monkey 0
    If false: throw to monkey 6

Monkey 3:
  Starting items: 71, 58, 93, 65, 80, 68, 54, 71
  Operation: new = old + 7
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 4

Monkey 4:
  Starting items: 97, 56, 79, 65, 58
  Operation: new = old + 5
  Test: divisible by 5
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 5:
  Starting items: 77
  Operation: new = old + 4
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 3

Monkey 6:
  Starting items: 99, 90, 84, 50
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 7:
  Starting items: 50, 66, 61, 92, 64, 78
  Operation: new = old + 3
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 1"""

class Monkey():
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspections = 0


def getMonkeys(input):
    input = input.split("\n\n")
    monkeys = []
    for m in input:
        m = m.split("\n")
        items = [int(x) for x in m[1][18:].split(",")]
        true = int(m[4].split(" ")[-1])
        false = int(m[5].split(" ")[-1])
        operation = m[2].split(" ")[-2:]
        test = int(m[3].split(" ")[-1])
        monkeys.append(Monkey(items, operation, test, true, false))
    return monkeys



def solve(rounds, monkeys, div3):
    mod = 1
    for m in monkeys:
        mod = mod * m.test

    for _ in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                monkey.inspections += 1
                item = monkey.items.pop(0)

                if monkey.operation[0] == "*":
                    if monkey.operation[1] == "old":
                        item *= item
                    else:
                        item *= int(monkey.operation[1])
                else:
                    item += int(monkey.operation[1])

                if div3:
                    item = item // 3
                else:
                    item = item % mod

                if item % monkey.test == 0:
                    monkeys[monkey.true].items.append(item)
                else:
                    monkeys[monkey.false].items.append(item)

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse = True)
    return inspections[0]*inspections[1]

monkeys = getMonkeys(input)
print("answer 1:", solve(20, monkeys, True))

monkeys = getMonkeys(input)
print("answer 2:", solve(10000, monkeys, False))
