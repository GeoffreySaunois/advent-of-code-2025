from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from heapq import nsmallest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


@dataclass
class Point:
    x: int
    y: int
    z: int

    def euclidean_distance(self, other: Point) -> float:
        return (
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        ) ** 0.5


class UnionFind:
    def __init__(self, n: int):
        self.n_nodes = n
        self.n_components = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def union(self, a: int, b: int) -> None:
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
            self.n_components -= 1

    def find(self, x: int) -> int:
        next = self.parent[x]
        if next == x:
            return x
        comp = self.find(next)
        self.parent[x] = comp
        return comp


def parse_input(path: Path) -> list[Point]:
    with open(path) as f:
        return list(
            map(lambda line_: Point(*map(int, line_.strip().split(","))), f.readlines())
        )


def first_problem(jbox: list[Point], k: int, verbose: bool = False) -> int:
    # 1. Compute k smallest connexions (O(n ln(k)))
    n = len(jbox)
    dists = (
        (jbox[i].euclidean_distance(jbox[j]), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    k_smallest = nsmallest(k, dists)

    # 2. Build the graph
    graph = UnionFind(n)
    for _, i, j in k_smallest:
        graph.union(i, j)

    # 3. Retrieve components
    components: dict[int, list[int]] = {}
    for i in range(n):
        comp = graph.find(i)
        if comp in components:
            components[comp].append(i)
        else:
            components[comp] = [i]

    if verbose:
        print(f"Components: {components}")

    return reduce(
        lambda x, y: x * y,
        sorted([len(c) for c in components.values()], reverse=True)[:3],
    )


def second_problem(jbox: list[Point], verbose: bool = False) -> int | None:
    # 1. Compute sorted distances
    n = len(jbox)
    dists = (
        (jbox[i].euclidean_distance(jbox[j]), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    dists = sorted(dists)

    # 2. Add connexions until there's only one cluster left
    graph = UnionFind(n)
    for _, i, j in dists:
        graph.union(i, j)
        if graph.n_components == 1:
            return jbox[i].x * jbox[j].x
    return None


def test_parse_input():
    test_input = parse_input(test_path)
    assert len(test_input) == 20
    assert test_input[0] == Point(162, 817, 812)


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, k=10, verbose=True) == 40


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 25272


if __name__ == "__main__":
    print(f"{DAY}:")

    val = parse_input(val_path)
    print("First problem val:", first_problem(val, k=1000))
    print("Second problem val:", second_problem(val))
