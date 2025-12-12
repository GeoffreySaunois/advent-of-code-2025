from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
test_path2 = BASE_DIR / "test2"
val_path = BASE_DIR / "input"


def parse_input(path: Path) -> dict[str, list[str]]:
    graph = {}
    with open(path) as f:
        for line in f.readlines():
            input = line.strip().split(": ")
            sources = input[0]
            destinations = input[1].split()
            graph[sources] = destinations
    return graph


def first_problem(graph: dict[str, list[str]], verbose: bool = False) -> int:
    return nb_paths(graph, "you", "out", verbose)


def nb_paths(
    graph: dict[str, list[str]], start: str, end: str, verbose: bool = False
) -> int:
    if verbose:
        print(graph)

    in_degrees = {node: 0 for node in graph}
    for sources in graph.values():
        for dest in sources:
            if dest in in_degrees:
                in_degrees[dest] += 1
            else:
                in_degrees[dest] = 1
    queue = [node for node, degree in in_degrees.items() if degree == 0]

    if verbose:
        print(in_degrees)
        print(queue)
    dp = {start: 1}
    while queue:
        node = queue.pop()
        paths = dp[node] if node in dp else 0
        if node in graph:
            for dest in graph[node]:
                in_degrees[dest] -= 1
                if in_degrees[dest] == 0:
                    queue.append(dest)

                if dest in dp:
                    dp[dest] += paths
                else:
                    dp[dest] = paths

    if verbose:
        print(dp)
    return dp[end]


def second_problem(graph: dict[str, list[str]], verbose: bool = False) -> int:
    return (
        nb_paths(graph, "svr", "fft", verbose)
        * nb_paths(graph, "fft", "dac", verbose)
        * nb_paths(graph, "dac", "out", verbose)
    )


def test_parse_input():
    _test_input = parse_input(test_path)


def test_first_problem():
    test_input = parse_input(test_path)
    assert first_problem(test_input, verbose=True) == 5


def test_second_problem():
    test_input = parse_input(test_path2)
    assert second_problem(test_input, verbose=True) == 2


if __name__ == "__main__":
    print(f"{DAY}:")

    val = parse_input(val_path)
    print("First problem val:", first_problem(val))
    print("Second problem val:", second_problem(val))
