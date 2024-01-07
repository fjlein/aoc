import re
import math


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    return [(l.split(" ")[0], l.split(" ")[1]) for l in lines]


def base_value(hand, cards):
    return sum([cards.index(char)*13**(i) for i, char in enumerate(reversed(hand))])


def type_value(hand, cards):
    counts = sorted([hand.count(c) for c in cards], reverse=True)
    if counts[0] == 5:
        return 7*13**5
    elif counts[0] == 4:
        return 6*13**5
    elif counts[0] == 3 and counts[1] == 2:
        return 5*13**5
    elif counts[0] == 3:
        return 4*13**5
    elif counts[0] == 2 and counts[1] == 2:
        return 3*13**5
    elif counts[0] == 2:
        return 2*13**5
    elif counts[4] == 1:
        return 1*13**5


def solve(data, cards):
    result = 0
    for i, hand in enumerate(sorted(data, key=lambda x: type_value(x[0]) + base_value(x[0], cards))):
        result += (i + 1) * int(hand[1])
    return result


def type_value_joker(hand, cards):
    values = []
    if not "J" in hand:
        return type_value(hand, cards)
    for c in cards[1:]:
        new_hand = hand.replace("J", c)
        values.append(type_value(new_hand, cards))

    return max(values)


def get_result(sorted_list):
    result = 0
    for i, hand in sorted_list:
        result += (i + 1) * int(hand[1])
    return result


def part1(data):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return get_result(enumerate(sorted(data, key=lambda x: type_value(x[0], cards) + base_value(x[0], cards))))


def part2(data):
    cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    return get_result(enumerate(sorted(data, key=lambda x: type_value_joker(x[0], cards) + base_value(x[0], cards))))


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
