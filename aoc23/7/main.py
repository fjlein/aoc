import re
import math


def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    return [(l.split(" ")[0], l.split(" ")[1]) for l in lines]


def base_value(hand, cards):
    return sum([cards.index(char)*13**(i) for i, char in enumerate(reversed(hand))])


def type_value(hand, cards):
    counts = sorted([hand.count(c) for c in cards], reverse=True)
    if counts[0] == 5:  # Five of a kind
        return 7*13**5
    elif counts[0] == 4:  # Four of a kind
        return 6*13**5
    elif counts[0] == 3 and counts[1] == 2:  # Full house
        return 5*13**5
    elif counts[0] == 3:  # Three of a kind
        return 4*13**5
    elif counts[0] == 2 and counts[1] == 2:  # Two pair
        return 3*13**5
    elif counts[0] == 2:  # One pair
        return 2*13**5
    return 1*13**5  # High card


def type_value_joker(hand, cards):
    return max([(type_value(hand.replace("J", c), cards)) for c in cards])


def determine_total_winnings(sorted_list):
    return sum([(i + 1) * int(hand[1]) for i, hand in enumerate(sorted_list)])


def part1(data):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def calculate_value(hand):
        return type_value(hand[0], cards) + base_value(hand[0], cards)

    return determine_total_winnings(sorted(data, key=calculate_value))


def part2(data):
    cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    def calculate_value(hand):
        return type_value_joker(hand[0], cards) + base_value(hand[0], cards)

    return determine_total_winnings(sorted(data, key=calculate_value))


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
