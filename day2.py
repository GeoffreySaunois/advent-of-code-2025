day = "Day 2"

test_path = f"inputs/{day}/test.txt"
val_path = f"inputs/{day}/val.txt"


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


def first_problem(id_ranges: list[list[int]]) -> int:
    ans = 0
    for id_range in id_ranges:
        curr = first_invalid_half(id_range[0])
        while double_number(curr) <= id_range[1]:
            # print(f"Adding double number {double_number(curr)}")
            ans += double_number(curr)
            curr += 1
    return ans


def second_problem(id_ranges):
    return 0


def parse_input(path):
    with open(path) as f:
        lines = []
        for id_range in f.readline().split(","):
            lines.append(list(map(int, id_range.strip().split("-"))))
    return lines


if __name__ == "__main__":

    # print("test input:", parse_input(test_path))
    # print("val input:", parse_input(val_path))

    lines = parse_input(test_path)
    print("First problem:", first_problem(lines))
    print("Second problem:", second_problem(lines))

    lines = parse_input(val_path)
    print("First problem:", first_problem(lines))
    print("Second problem:", second_problem(lines))
