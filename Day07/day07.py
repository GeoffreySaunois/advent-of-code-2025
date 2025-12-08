from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


def parse_input(path: Path) -> list[list[str]]:
    with open(path) as f:
        return list(map(lambda line_: list(line_.strip()), f.readlines()))


def first_problem(grid: list[list[str]], verbose: bool = False) -> int:
    n = len(grid)
    m = len(grid[0])
    splits = 0

    for i in range(1, n):
        for j in range(m):
            prev = grid[i - 1][j]
            # No beam
            if prev == "." or prev == "^":
                continue
            # In this case we have a beam
            if grid[i][j] == ".":
                # Beam goes down
                grid[i][j] = "|"
            elif grid[i][j] == "^":
                # Beam goes left and right
                grid[i][j - 1] = "|"
                grid[i][j + 1] = "|"
                splits += 1
    if verbose:
        for row in grid:
            print(row)
    return splits


def second_problem(grid: list[list[str]], verbose: bool = False) -> int:
    n = len(grid)
    m = len(grid[0])
    dp = [0 if cell == "." else 1 for cell in grid[0]]

    for i in range(1, n):
        # if i == 3:
        # break
        new_dp = [0] * m
        for j in range(m):
            if grid[i][j] == ".":
                # Beam goes down
                new_dp[j] += dp[j]
                print(f"  Beam at ({i},{j}) from above, dp[{j}] += {dp[j]}")
            if j > 0 and grid[i][j - 1] == "^":
                new_dp[j] += dp[j - 1]
                print(f"  Beam at ({i},{j}) from left, dp[{j}] += {dp[j - 1]}")
            if j < m - 1 and grid[i][j + 1] == "^":
                new_dp[j] += dp[j + 1]
                print(f"  Beam at ({i},{j}) from right, dp[{j}] += {dp[j + 1]}")

        dp = new_dp
        print(f"After row {i:02}: dp = {dp}")
    if verbose:
        for row in grid:
            print(row)
    return sum(dp)


def test_parse_input():
    test_input = parse_input(test_path)
    assert test_input[0] == list(".......S.......")
    assert test_input[-2] == list(".^.^.^.^.^...^.")


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, verbose=True) == 21


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 40


if __name__ == "__main__":
    print(f"{DAY}:")

    val = parse_input(val_path)
    # print("First problem val:", first_problem(val))
    print("Second problem val:", second_problem(val))
