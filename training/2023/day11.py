"""AoC 2023 day 11: https://adventofcode.com/2023/day/11

Usage: python day11.py <input_filepath>
"""
import argparse
from itertools import combinations, starmap

import numpy as np

TEST_DATA = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

TEST_DATA_EXPANDED = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""


class GalaxyObserver:
    "Blueprint for a galaxy observer as described in the problem statement"

    def __init__(self, grid: str) -> None:
        self.grid = grid
        self.process_grid()
        print(f"grid initial shape: {self.grid.shape}")
        self.expanded = None
        self.paths_sum = 0
        self.paths_sum_p2 = 0

    def process_grid(self):
        self.grid = np.array(
            [list(line) for line in self.grid.splitlines() if line.strip()]
        )

    def expand(self):
        """Doubles any row or column that is empty that is made up of dots (.)"""
        self.expanded = self.grid.copy()
        empty_row_indices = []
        empty_col_indices = []
        for row_ind in range(self.grid.shape[0]):
            row = self.grid[row_ind, :]
            if (row == ".").all():
                empty_row_indices.append(row_ind)
        for col_ind in range(self.grid.shape[1]):
            col = self.grid[:, col_ind]
            if (col == ".").all():
                empty_col_indices.append(col_ind)
        for i, row_ind in enumerate(empty_row_indices):
            self.expanded = np.insert(
                self.expanded, row_ind + i, self.expanded[row_ind + i, :], axis=0
            )
        for j, col_ind in enumerate(empty_col_indices):
            self.expanded = np.insert(
                self.expanded, col_ind + j, self.expanded[:, col_ind + j], axis=1
            )
        print(f"expanded grid shape: {self.expanded.shape}")

    def compute(self) -> int:
        self._detect_galaxies()
        self.paths_sum = sum(
            starmap(self._get_shortest_path, combinations(self.galaxies_coords, 2))
        )
        print(f"{self.paths_sum=}")
        return self.paths_sum

    def _detect_galaxies(self) -> None:
        "detect # in the grid and get their (x, y) coordinates)"
        if not hasattr(self, "expanded"):
            raise Exception("You need to expand the grid first")
        self.galaxies_coords = np.argwhere(self.expanded == "#")
        # print(f"galaxies coords: {self.galaxies_coords}")

    def _get_shortest_path(
        self, galaxy1: tuple[int, int], galaxy2: tuple[int, int]
    ) -> int:
        "Returns the shortest path between two galaxies"
        return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    def expand_p2(self, expand_factor: int = 1_000_000) -> int:
        """This time we can no longer afford to store the whole grid in memory, let's retain only the coordinates of the galaxies"""
        initial_galaxies_coords = np.argwhere(self.grid == "#")
        expanded_galaxy_coords = initial_galaxies_coords.copy().tolist()
        initial_row_indices = sorted(set(initial_galaxies_coords[:, 0]))
        row_indices = initial_row_indices.copy()
        for ind in range(len(row_indices) - 1):
            if row_delta := initial_row_indices[ind + 1] - initial_row_indices[ind] - 1:
                for j in range(ind + 1, len(row_indices)):
                    row_indices[j] += expand_factor * row_delta - row_delta
        map_rows = dict(zip(initial_row_indices, row_indices))

        initial_col_indices = sorted(set(initial_galaxies_coords[:, 1]))

        col_indices = initial_col_indices.copy()
        for ind in range(len(col_indices) - 1):
            if col_delta := initial_col_indices[ind + 1] - initial_col_indices[ind] - 1:
                for j in range(ind + 1, len(col_indices)):
                    col_indices[j] += expand_factor * col_delta - col_delta
        map_cols = dict(zip(initial_col_indices, col_indices))

        for elem in expanded_galaxy_coords:
            elem[0] = map_rows[elem[0]]
            elem[1] = map_cols[elem[1]]

        self.paths_sum_p2 = sum(
            starmap(self._get_shortest_path, combinations(expanded_galaxy_coords, 2))
        )
        print(f"{self.paths_sum_p2=}")
        return self.paths_sum_p2


if __name__ == "__main__":
    # part 1
    galaxy_observer_test = GalaxyObserver(TEST_DATA)
    assert len(galaxy_observer_test.grid.shape) == 2
    galaxy_observer_test.expand()
    assert (
        galaxy_observer_test.expanded
        == np.array(
            [list(line) for line in TEST_DATA_EXPANDED.splitlines() if line.strip()]
        )
    ).all()
    galaxy_observer_test.compute()
    assert galaxy_observer_test.paths_sum == 374
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    galaxy_observer = GalaxyObserver(text)
    galaxy_observer.expand()
    galaxy_observer.compute()
    # part 2
    assert galaxy_observer_test.expand_p2(expand_factor=10) == 1030
    assert galaxy_observer_test.expand_p2(expand_factor=100) == 8410
    galaxy_observer.expand_p2()
