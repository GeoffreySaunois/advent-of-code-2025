day = "Day 4"

test_path = f"inputs/{day}/test.txt"
val_path = f"inputs/{day}/val.txt"

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def first_problem(grid: list[list[bool]]) -> int:
    n = len(grid) - 2

    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if grid[i][j] and count_neighbors(grid, i, j) < 4:
                count += 1
    return count


def count_neighbors(grid, i, j):
    count = 0
    for di, dj in DIRECTIONS:
        if grid[i + di][j + dj]:
            count += 1
    return count


def second_problem(grid: list[list[bool]], verbose=False) -> int:
    n = len(grid) - 2

    count = 0
    queue = []
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


def parse_input(path) -> list[list[bool]]:
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


if __name__ == "__main__":
    print(f"{day}:")
    print("Test input:", *parse_input(test_path), sep="\n")

    test = parse_input(test_path)
    val = parse_input(val_path)

    print("First problem test :", first_problem(test))
    print("First problem val:", first_problem(val))

    print("Second problem test:", second_problem(test, verbose=True))
    print("Second problem val:", second_problem(val))
