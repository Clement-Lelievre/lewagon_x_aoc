"https://adventofcode.com/2017/day/22"
import numpy as np
from tqdm import tqdm


INPUT_TEST = """
..#
#..
..."""

INPUT = """#.##.###.#.#.##.###.##.##
.##.#.#.#..####.###.....#
...##.....#..###.#..#.##.
##.###.#...###.#.##..##.#
###.#.###..#.#.##.#.###.#
.###..#.#.####..##..#..##
..###.##..###.#..#...###.
........##..##..###......
######...###...###...#...
.######.##.###.#.#...###.
###.##.###..##..#..##.##.
.#.....#.#.#.#.##........
#..#..#.#...##......#.###
#######.#...#..###..#..##
#..#.###...#.#.#.#.#....#
#.#####...#.##.##..###.##
..#..#..#.....#...#.#...#
###.###.#...###.#.##.####
.....###.#..##.##.#.###.#
#..#...######.....##.##.#
###.#.#.#.#.###.##..###.#
..####.###.##.#.###..#.##
#.#....###....##...#.##.#
###..##.##.#.#.##..##...#
#.####.###.#...#.#.....##
"""

TESTS_PART1 = ((7, 5), (70, 41), (10_000, 5_587))


def simulate(n_sim: int, grid: str) -> int:
    "simulation for part 1"
    # build the grid
    grid = grid.translate(str.maketrans("#.", "10"))
    grid = np.array([list(row) for row in grid.splitlines() if row.strip()], dtype=int)
    grid = np.pad(grid, 1_000, "constant", constant_values=0)
    facing = 0  # 0 means 'north', 90 means 'east', 180 means 'south', 270 means 'west'
    nb_rows, nb_cols = grid.shape
    pos = (nb_rows // 2, nb_cols // 2)
    nb_infections = 0
    for _ in range(n_sim):
        node = grid[pos]
        facing = (facing + 90) % 360 if node else (facing - 90) % 360
        if node == 0:
            nb_infections += 1
        grid[pos] = 1 - grid[pos]
        pos = (
            pos[0] + (facing == 180) - (facing == 0),
            pos[1] + (facing == 90) - (facing == 270),
        )
    print(nb_infections)
    return nb_infections


for nb_burst_test, nb_infections_test in TESTS_PART1:
    print(f"testing {nb_burst_test} bursts...")
    assert simulate(nb_burst_test, INPUT_TEST) == nb_infections_test

print("part 1:", simulate(10_000, INPUT))

# part 2
# Of the first 100 bursts, 26 will result in infection. Unfortunately, another feature of this evolved virus is speed;
# of the first 10000000 bursts, 2511944 will result in infection.


def simulate_part2(n_sim: int, grid: str) -> int:
    """simulation for part 2

    Args:
        n_sim (int): number of bursts
        grid (str): the string repr of the grid

    Returns:
        int: number of infections
    """
    # build the grid
    grid = grid.translate(str.maketrans("#.", "30"))
    assert set(grid.replace("\n", "")) == {"0", "3"}
    grid = np.array([list(row) for row in grid.splitlines() if row.strip()], dtype=int)
    facing = 0  # 0 means 'north', 90 means 'east', 180 means 'south', 270 means 'west'
    nb_rows, nb_cols = grid.shape
    pos = (nb_rows // 2, nb_cols // 2)
    nb_infections = 0
    states = {0: 1, 1: 3, 3: 2, 2: 0}
    # now, node has 4 possible values: 0 clean, 1 weakened, 2 flagged, 3 infected
    for _ in tqdm(range(n_sim)):
        if not 0 <= pos[0] < grid.shape[0] or not 0 <= pos[1] < grid.shape[1]:
            grid = np.pad(grid, 1, "constant", constant_values=0)
            # can be optimized as only a 1d array can be appended: no need for a padding
            pos = (pos[0] + 1, pos[1] + 1)
        node = grid[pos]
        if node == 0:
            facing = (facing - 90) % 360
        elif node == 3:
            facing = (facing + 90) % 360
        elif node == 2:
            facing = (facing - 180) % 360
        elif node == 1:
            nb_infections += 1
        grid[pos] = states[grid[pos]]
        pos = (
            pos[0] + (facing == 180) - (facing == 0),
            pos[1] + (facing == 90) - (facing == 270),
        )
    print(f"{nb_infections=}")
    return nb_infections


TESTS_PART2 = ((100, 26), (10_000_000, 2_511_944))
for nb_burst_test, nb_infections_test in TESTS_PART2:
    print(f"testing {nb_burst_test} bursts...")
    assert simulate_part2(nb_burst_test, INPUT_TEST) == nb_infections_test

print("part 2:", simulate_part2(10_000_000, INPUT))
