def parse(puzzle_input):
    return puzzle_input.replace("\n", "").split(",")


def hash_function(w):
    current = 0
    for c in w:
        current = (current + ord(c)) * 17
    return current % 256


def part1(data):
    return sum(hash_function(w) for w in data)


def get_boxes_value(boxes):
    return sum(sum((box + 1) * (i + 1) * lens[1] for i, lens in enumerate(lenses)) for (box, lenses) in boxes.items())


def dissect_instruction(w):
    if "-" in w:
        return w[:-1], hash_function(w[:-1]), None
    else:
        return w[:-2], hash_function(w[:-2]), int(w[-1])


def part2(data):
    boxes = {}
    for w in data:
        label, box_number, focal_length = dissect_instruction(w)
        if "-" in w:
            try:
                index = [label for (label, _)
                         in boxes[box_number]].index(label)
                boxes[box_number].pop(index)
            except Exception:
                pass  # nothing to delete, box not found or lens not found
        else:
            if box_number not in boxes:
                boxes[box_number] = []
            try:
                index = [label for (label, _)
                         in boxes[box_number]].index(label)
                boxes[box_number][index] = (label, focal_length)
            except ValueError:
                boxes[box_number].append((label, focal_length))

    return get_boxes_value(boxes)


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
