day = "Day 1"

test_path = f"inputs/{day}/test.txt"
val_path = f"inputs/{day}/val.txt"


def first_problem(rotations):
    position = 50
    ans = 0
    for r in rotations:
        value = int(r[1:])
        if r[0] == "L":
            position -= value
        else:
            position += value
        position %= 100
        if position == 0:
            ans += 1
    return ans


def second_problem(rotations):
    position = 50
    ans = 0
    for r in rotations:
        value = int(r[1:])

        ans += value // 100
        value %= 100

        new_position = position
        if r[0] == "L":
            new_position -= value
        else:
            new_position += value

        if (position > 0 and new_position <= 0) or new_position >= 100:
            ans += 1
        position = new_position % 100
    return ans


def parse_input(path):
    with open(path) as f:
        lines = list(map(lambda line_: line_.strip(), f.readlines()))
    return lines


if __name__ == "__main__":
    lines = parse_input(test_path)
    print("First problem:", first_problem(lines))
    print("Second problem:", second_problem(lines))

    lines = parse_input(val_path)
    print("First problem:", first_problem(lines))
    print("Second problem:", second_problem(lines))
