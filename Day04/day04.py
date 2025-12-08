from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def parse_input(path: Path) -> list[list[bool]]:
    with open(path) as f:
        raw = list(
            map(
                lambda line: list(map(lambda x: x == "@", line)),
                map(str.strip, f.readlines()),
            )
        )

    m = len(raw[0])
    padded = [[False] * (m + 2)]
    for row in raw:
        padded.append([False] + row + [False])
    padded.append([False] * (m + 2))
    return padded


def count_neighbors(grid: list[list[bool]], i: int, j: int) -> int:
    count = 0
    for di, dj in DIRECTIONS:
        if grid[i + di][j + dj]:
            count += 1
    return count


def first_problem(grid: list[list[bool]], verbose: bool = False) -> int:
    n = len(grid) - 2

    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if grid[i][j] and count_neighbors(grid, i, j) < 4:
                count += 1
    return count


def second_problem(grid: list[list[bool]], verbose: bool = False) -> int:
    n = len(grid) - 2

    count = 0
    queue: list[tuple[int, int]] = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if grid[i][j] and count_neighbors(grid, i, j) < 4:
                queue.append((i, j))

    while queue:
        i, j = queue.pop(0)
        if not grid[i][j]:
            continue
        grid[i][j] = False
        count += 1

        for di, dj in DIRECTIONS:
            ni, nj = i + di, j + dj
            if grid[ni][nj] and count_neighbors(grid, ni, nj) < 4:
                queue.append((ni, nj))

    return count


def test_parse_input():
    test_input = parse_input(test_path)
    assert len(test_input) == 12
    assert len(test_input[0]) == 12
    assert test_input[1][1] is False
    assert test_input[2][1] is True


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, verbose=True) == 13


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 43


if __name__ == "__main__":
    print(f"{DAY}:")

    val = parse_input(val_path)
    print("First problem val:", first_problem(val))
    print("Second problem val:", second_problem(val))
