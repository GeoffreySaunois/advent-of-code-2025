day = "Day 3"

test_path = f"inputs/{day}/test.txt"
val_path = f"inputs/{day}/val.txt"


def first_problem(batteries: list[list[int]], verbose=False) -> int:
    n = len(batteries[0])
    ans = 0
    for battery in batteries:
        a = battery[0]
        b = battery[1]
        for index, charge in enumerate(battery[1:]):
            if charge > a and index < n - 2:
                a = charge
                b = 0
            elif charge > b:
                b = charge
        line_val = a * 10 + b
        if verbose:
            print(f"Battery: {battery} -> a: {a}, b: {b}, val: {line_val}")
        ans += line_val
    return ans


def second_problem(batteries: list[list[int]], verbose=False) -> int:
    ans = 0
    for battery in batteries:
        ans += solve_battery(battery, verbose)
    return ans


def solve_battery(battery: list[int], verbose=False) -> int:
    n = len(battery)
    dp = [0] * (n + 1)

    for p in range(12):
        prev = dp.copy()
        pow = 10**p
        for k in range(n - p):
            ind = n - p - k - 1
            joltage = battery[ind]
            dp[ind] = max(dp[ind + 1], joltage * pow + prev[ind + 1])
        # print(f"After power {p}: {dp}")

    if verbose:
        print(f"Battery: {battery} -> val: {dp[0]}")
    return dp[0]


def parse_input(path) -> list[list[int]]:
    with open(path) as f:
        return list(
            map(lambda line: list(map(int, line)), map(str.strip, f.readlines()))
        )


if __name__ == "__main__":
    print(f"{day}:")
    # print("Test input:", parse_input(test_path))

    test = parse_input(test_path)
    val = parse_input(val_path)

    # print("First problem test :", first_problem(test, verbose=True))
    # print("First problem val:", first_problem(val))

    # solve_battery([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], verbose=True)
    print("Second problem test:", second_problem(test, verbose=True))
    print("Second problem val:", second_problem(val))
