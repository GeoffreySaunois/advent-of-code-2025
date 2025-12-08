from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


def parse_input(path: Path) -> list[str]:
    with open(path) as f:
        return list(map(lambda line_: line_.strip(), f.readlines()))


def first_problem(rotations: list[str], verbose: bool = False) -> int:
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


def second_problem(rotations: list[str], verbose: bool = False) -> int:
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


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, verbose=True) == 3


def test_parse_input():
    test_input = parse_input(test_path)
    assert test_input[0] == "L68"
    assert test_input[-1] == "L82"


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 6


if __name__ == "__main__":
    print(f"{DAY}:")
    print("Test input:", *parse_input(test_path), sep="\n")

    val = parse_input(val_path)
    print("First problem val:", first_problem(val))
    print("Second problem val:", second_problem(val))
