from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


@dataclass
class Point:
    x: int | float
    y: int | float


@dataclass
class Rectangle:
    c1: Point
    c2: Point

    def area(self) -> int:
        return (abs(self.c2.x - self.c1.x) + 1) * (abs(self.c2.y - self.c1.y) + 1)


def test_area():
    r = Rectangle(Point(1, 1), Point(3, 3))
    assert r.area() == 9
    r = Rectangle(Point(11, 1), Point(2, 5))
    assert r.area() == 50


def parse_input(path: Path) -> list[Point]:
    with open(path) as f:
        return list(
            map(lambda line_: Point(*map(int, line_.strip().split(","))), f.readlines())
        )


def first_problem(points: list[Point], verbose: bool = False) -> int:
    max_area = 0
    n = len(points)

    for i in range(n - 1):
        for j in range(i + 1, n):
            area = Rectangle(points[i], points[j]).area()
            max_area = max(max_area, area)
            if verbose:
                print(f"Rectangle: {points[i]} to {points[j]} has area {area}")

    return max_area


def second_problem(points: list[Point], verbose: bool = False) -> int:
    n = len(points)

    # 1. x and y axis + mappings
    x_axis = sorted(set(p.x for p in points))
    y_axis = sorted(set(p.y for p in points))

    x_mapping = {x_axis[i]: i for i in range(len(x_axis))}
    y_mapping = {y_axis[i]: i for i in range(len(y_axis))}

    r = len(x_axis)
    s = len(y_axis)

    # 2. Define the (p-1)(q-1) `pixels` grid, whether each point is inside the loop
    pixels = [[False for _ in range(s - 1)] for _ in range(r - 1)]

    # 2.a Compute vertical segments, for raycast inside computation (based on Jordan Theorem)
    # !! We expect the 2 first points to share the same x coordinate (rotate the input otherwise)
    vertical_segments: list[tuple[int, tuple[int, int]]] = []
    for i in range(0, n, 2):
        x = points[i].x
        y_min = min(points[i + 1].y, points[i].y)
        y_max = max(points[i + 1].y, points[i].y)
        vertical_segments.append((x, (y_min, y_max)))

    if verbose:
        print("Vertical segments:", *vertical_segments, sep="\n", end="\n\n")

    # 2.b Apply raycast inside check
    for i in range(r - 1):
        for j in range(s - 1):
            x = (x_axis[i] + x_axis[i + 1]) / 2
            y = (y_axis[j] + y_axis[j + 1]) / 2
            pixels[i][j] = is_inside(x, y, vertical_segments)

    if verbose:
        print("Pixels:", *pixels, sep="\n", end="\n\n")

    # 3. Compute prefixes
    prefixes = [[0 for _ in range(s)] for _ in range(r)]
    for i in range(1, r):
        for j in range(1, s):
            prefixes[i][j] = (
                pixels[i - 1][j - 1]
                + prefixes[i - 1][j]
                + prefixes[i][j - 1]
                - prefixes[i - 1][j - 1]
            )

    if verbose:
        print("Prefixes:", *prefixes, sep="\n", end="\n\n")

    # 4. Iterate through all recatangles, and check whether they satisfy the condition
    max_area = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            p = points[i]
            q = points[j]
            area = Rectangle(p, q).area()

            x_min, x_max = min(p.x, q.x), max(p.x, q.x)
            y_min, y_max = min(p.y, q.y), max(p.y, q.y)

            x_index_min = x_mapping[x_min]
            x_index_max = x_mapping[x_max]
            y_index_min = y_mapping[y_min]
            y_index_max = y_mapping[y_max]
            pixel_area = (x_index_max - x_index_min) * (y_index_max - y_index_min)

            inside_pixels = (
                prefixes[x_index_max][y_index_max]
                - prefixes[x_index_min][y_index_max]
                - prefixes[x_index_max][y_index_min]
                + prefixes[x_index_min][y_index_min]
            )

            if verbose:
                print(
                    f"Rectangle: {points[i]} to {points[j]} has pixel area {pixel_area} and inside count {inside_pixels}"
                )
            if inside_pixels == pixel_area:
                max_area = max(max_area, area)
                if verbose:
                    print(
                        f"  -> Valid rectangle: {points[i]} to {points[j]} with area {pixel_area}"
                    )

    return max_area


def is_inside(
    x: float, y: float, vertical_segments: list[tuple[int, tuple[int, int]]]
) -> bool:
    count = 0
    for a, (b, c) in vertical_segments:
        if a < x:
            continue
        if b < y < c:
            count += 1
    return count % 2 == 1


def test_parse_input():
    test_input = parse_input(test_path)
    assert len(test_input) == 8
    assert test_input[0].x == 7


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, verbose=True) == 50


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 24


if __name__ == "__main__":
    print(f"{DAY}:")

    val = parse_input(val_path)
    print("First problem val:", first_problem(val))
    print("Second problem val:", second_problem(val))
