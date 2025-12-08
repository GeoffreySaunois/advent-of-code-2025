from enum import StrEnum
from functools import reduce
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


class Operation(StrEnum):
    ADD = "+"
    MUL = "*"


def first_parse_input(path: Path) -> tuple[list[list[int]], list[str]]:
    with open(path) as f:
        input = list(map(lambda line_: line_.strip(), f.readlines()))
    numbers = []
    n = len(input)
    for i in range(n - 1):
        numbers.append(list(map(int, input[i].split())))
    operators = list(map(Operation, input[n - 1].split()))
    return numbers, operators


def first_problem(
    numbers: list[list[int]], operators: list[str], verbose: bool = False
) -> int:
    m = len(operators)
    n = len(numbers)
    total = 0
    for i in range(m):
        op = operators[i]
        col_values = [numbers[j][i] for j in range(n)]
        if op == Operation.ADD:
            col_result = sum(col_values)
        elif op == Operation.MUL:
            col_result = reduce(lambda x, y: x * y, col_values)

        if verbose:
            print(
                f"Operation {i + 1}/{m}: {op} on column values {col_values} = {col_result}"
            )
        total += col_result
    return total


def second_parse_input(path: Path) -> list[tuple[Operation, list[int]]]:
    # Use 🎄 to keep spaces
    with open(path) as f:
        grid = list(map(lambda line_: line_.replace(" ", "🎄").strip(), f.readlines()))

    operators = list(filter(len, grid[-1].split("🎄")))

    n = len(grid) - 1
    m = len(grid[0])
    problems = [(operators[0], [])]
    operator_index = 0
    for j in range(m):
        col = reduce(lambda x, y: x + y, (grid[i][j] for i in range(n))).replace(
            "🎄", ""
        )
        if col:
            col_number = int(col)
            problems[operator_index][1].append(col_number)
        else:
            operator_index += 1
            problems.append(
                (operators[operator_index], [])
            )  # don't worry, last col is not empty

    return problems


def second_problem(
    problems: list[tuple[Operation, list[int]]], verbose: bool = False
) -> int:
    total = 0
    for op, numbers in problems:
        if op == Operation.ADD:
            result = sum(numbers)
        elif op == Operation.MUL:
            result = reduce(lambda x, y: x * y, numbers)

        if verbose:
            print(f"Operation {op} on numbers {numbers} = {result}")
        total += result
    return total


def test_first_parse_input():
    numbers, operators = first_parse_input(test_path)
    assert numbers[0] == [123, 328, 51, 64]
    assert len(numbers) == 3
    assert operators[0] == Operation.MUL


def test_second_parse_input():
    problems = second_parse_input(test_path)
    assert problems[0][0] == Operation.MUL
    assert problems[0][1] == [1, 24, 356]


def test_first_problem():
    numbers, operators = first_parse_input(test_path)
    assert first_problem(numbers, operators, verbose=True) == 4277556


def test_second_problem():
    problems = second_parse_input(test_path)
    assert second_problem(problems, verbose=True) == 3263827


if __name__ == "__main__":
    print(f"{DAY}:")

    numbers, operators = first_parse_input(val_path)
    print("First problem val:", first_problem(numbers, operators))

    problems = second_parse_input(val_path)
    print("Second problem val:", second_problem(problems))
