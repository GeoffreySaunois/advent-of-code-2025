from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


def parse_input(path: Path) -> list[list[int]]:
    with open(path) as f:
        lines: list[list[int]] = []
        for id_range in f.readline().split(","):
            lines.append(list(map(int, id_range.strip().split("-"))))
    return lines


def first_invalid_half(start_range: int) -> int:
    range_str = str(start_range)
    n = len(range_str)
    if n % 2 != 0:
        return 10 ** (n // 2)

    first_half = int(range_str[: n // 2])
    second_half = int(range_str[n // 2 :])
    if first_half < second_half:
        return first_half + 1
    else:
        return first_half


def double_number(n: int) -> int:
    return int(str(n) * 2)


def first_problem(id_ranges: list[list[int]], verbose: bool = False) -> int:
    ans = 0
    for id_range in id_ranges:
        curr = first_invalid_half(id_range[0])
        while double_number(curr) <= id_range[1]:
            ans += double_number(curr)
            curr += 1
    return ans


def second_problem(id_ranges: list[list[int]], verbose: bool = False) -> int:
    ans = 0
    for a, b in id_ranges:
        ans += sum_multiple_numbers(a, b, verbose=verbose)
    return ans


def sum_multiple_numbers(
    start_range: int, end_range: int, verbose: bool = False
) -> int:
    count = 0
    for n in range(start_range, end_range + 1):
        if is_multiple_number(n):
            count += n
            if verbose:
                print(f"Found multiple number for range {start_range}-{end_range}: {n}")
    return count


def is_multiple_number(n: int) -> bool:
    mask = 10
    while mask <= n:
        if is_nth_number(n, mask):
            return True
        mask *= 10
    return False


def is_nth_number(n: int, mask: int) -> bool:
    pattern = n % mask
    n = n // mask

    # Make sure the first digit  is not 0
    if pattern < mask // 10:
        return False

    while n > 0:
        if n % mask != pattern:
            return False
        n = n // mask
    return True


def test_parse_input():
    test_input = parse_input(test_path)
    assert test_input[0] == [11, 22]


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, verbose=True) == 1227775554


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 4174379265


if __name__ == "__main__":
    print(f"{DAY}:")

    val = parse_input(val_path)
    print("First problem val:", first_problem(val))
    print("Second problem val:", second_problem(val))
