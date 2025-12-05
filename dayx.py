day = "Day replace_me"

test_path = f"inputs/{day}/test.txt"
val_path = f"inputs/{day}/val.txt"


def first_problem(input: list[list], verbose=False) -> int:
    return 0


def second_problem(input: list[int], verbose=False) -> int:
    return 0


def parse_input(path):
    with open(path) as f:
        lines = []
        for id_range in f.readline().split(","):
            lines.append(list(map(int, id_range.strip().split("-"))))
    return lines


if __name__ == "__main__":
    print(f"{day}:")
    print("Test input:", *parse_input(test_path), sep="\n")

    test = parse_input(test_path)
    val = parse_input(val_path)

    print("First problem test :", first_problem(test))
    print("First problem val:", first_problem(val))

    print("Second problem test:", second_problem(test, verbose=True))
    print("Second problem val:", second_problem(val))
