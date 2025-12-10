from dataclasses import dataclass
from functools import reduce
from pathlib import Path

import pulp

BASE_DIR = Path(__file__).resolve().parent
DAY = BASE_DIR.name

test_path = BASE_DIR / "test"
val_path = BASE_DIR / "input"


@dataclass
class Machine:
    lights: list[bool]
    buttons: list[list[int]]
    joltages: list[int]


def parse_input(path: Path) -> list[Machine]:
    machines: list[Machine] = []
    with open(path) as f:
        for line_ in f.readlines():
            els = line_.strip().split()
            lights = list(map(lambda x: x == "#", els[0][1:-1]))
            buttons = list(map(lambda x: list(map(int, x[1:-1].split(","))), els[1:-1]))
            joltages = list(map(int, els[-1][1:-1].split(",")))
            machines.append(Machine(lights, buttons, joltages))

        return machines


def first_problem(machines: list[Machine], verbose: bool = False) -> int:
    fewest_total_presses = 0
    for machine in machines:
        fewest_total_presses += configure_lights(machine, verbose)

    return fewest_total_presses


INF: int = 42


def configure_lights(machine: Machine, verbose: bool = False) -> int:
    lights = machine.lights
    buttons = machine.buttons

    p = len(lights)
    target = reduce(lambda x, y: 2 * x + y, lights[::-1])

    n = 2**p
    dp = [INF * (i > 0) for i in range(n)]
    last_modified = [-1 for _ in range(n)]

    for i, button in enumerate(buttons):
        for j in range(n):
            if dp[j] == INF or last_modified[j] == i:
                continue
            mask = button_mask(button)
            new = mask ^ j
            if dp[j] + 1 < dp[new]:
                dp[new] = dp[j] + 1
                last_modified[new] = i

    if verbose:
        print(f"Fewest presses for machine: {dp[target]}")
        print(f"Target mask: {bin(target)}")
    return dp[target]


def button_mask(button: list[int]):
    return sum(2**light for light in button)


def second_problem(machines: list[Machine], verbose: bool = False) -> int:
    fewest_total_presses = 0
    for machine in machines:
        fewest_total_presses += configure_joltages(machine, verbose)

    return fewest_total_presses


def configure_joltages(machine: Machine, verbose: bool = False) -> int:
    buttons = machine.buttons
    joltages = machine.joltages

    A = [[1 if i in button else 0 for button in buttons] for i in range(len(joltages))]

    r = len(buttons)
    p = len(joltages)

    prob = pulp.LpProblem("Diophantine_AX_eq_Y", pulp.LpStatusOptimal)

    # We want integer non-negative variables
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(r)]

    # Constraints AX = Y
    for i in range(p):
        prob += sum(A[i][j] * x[j] for j in range(r)) == joltages[i]

    # Add an objective to get the fewest presses
    prob += sum(x)

    solver = pulp.PULP_CBC_CMD(msg=0)  # type: ignore
    prob.solve(solver)

    if verbose:
        print("Status:", pulp.LpStatus[prob.status])
        print("Solution:", [xi.value() for xi in x])
    return sum(xi.value() for xi in x)  # type: ignore


def test_parse_input():
    machines = parse_input(test_path)
    assert machines[0].lights == [False, True, True, False]
    assert machines[0].buttons == [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]
    assert machines[0].joltages == [3, 5, 4, 7]


def test_button_mask():
    assert button_mask([2]) == 4
    assert button_mask([1, 3]) == 10


def test_first_problem():
    machines = parse_input(test_path)
    assert first_problem(machines, verbose=True) == 7


def test_second_problem():
    test_input = parse_input(test_path)
    assert second_problem(test_input, verbose=True) == 33


if __name__ == "__main__":
    print(f"{DAY}:")

    val = parse_input(val_path)
    print("First problem val:", first_problem(val))
    print("Second problem val:", second_problem(val))
