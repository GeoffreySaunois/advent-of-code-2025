from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


def parse_input(path: Path) -> list[str]:
    with open(path) as f:
        return list(map(lambda line_: line_.strip(), f.readlines()))


def first_problem(input: list[str], verbose: bool = False) -> int:
    return 0


def second_problem(input: list[str], verbose: bool = False) -> int:
    return 0


def test_parse_input():
    test_input = parse_input(test_path)
    assert test_input == []


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, verbose=True) == 0


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 0


if __name__ == "__main__":
    print(f"{DAY}:")

    val = parse_input(val_path)
    print("First problem val:", first_problem(val))
    print("Second problem val:", second_problem(val))
