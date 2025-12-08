from pathlib import Path

InputType = tuple[list[tuple[int, int]], list[int]]

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


def first_problem(input: InputType, verbose: bool = False) -> int:
    ranges, ingredients = input
    ranges = sorted(ranges, key=lambda x: (x[0], x[1]))
    ingredients = sorted(ingredients)

    fresh = 0

    n_ranges = len(ranges)
    n_ingredients = len(ingredients)
    range_index = 0
    ingredient_index = 0

    while ingredient_index < n_ingredients and range_index < n_ranges:
        ingredient = ingredients[ingredient_index]
        start, end = ranges[range_index]
        if ingredient < start:
            ingredient_index += 1
            continue
        if start <= ingredient <= end:
            fresh += 1
            ingredient_index += 1
            continue
        range_index += 1

    return fresh


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, verbose=True) == 3


def second_problem(input: InputType, verbose: bool = False) -> int:
    ranges, _ = input
    ranges = sorted(ranges, key=lambda x: (x[0], x[1]))

    fresh = 0
    start = 0
    end = -1

    for a, b in ranges:
        if a > end:
            fresh += end - start + 1
            if verbose:
                print(end - start + 1)
            start, end = a, b
        end = max(end, b)

    fresh += end - start + 1
    if verbose:
        print(end - start + 1)

    return fresh


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 14


def parse_input(path: Path) -> InputType:
    with open(path) as f:
        ranges: list[tuple[int, int]] = []
        ingredients: list[int] = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        for line in f.readlines():
            ingredients.append(int(line.strip()))

        return (ranges, ingredients)


def main():
    print(f"{DAY}:")
    print("Test input:", *parse_input(test_path), sep="\n")

    test = parse_input(test_path)
    val = parse_input(val_path)

    print("First problem test :", first_problem(test))
    print("First problem val:", first_problem(val))

    print("Second problem test:", second_problem(test, verbose=True))
    print(
        "Second problem custom:",
        second_problem(([(10, 50), (20, 25)], [42]), verbose=True),
    )
    print("Second problem val:", second_problem(val))


if __name__ == "__main__":
    main()
