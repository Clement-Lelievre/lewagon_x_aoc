"""AoC 2023 day 11: https://adventofcode.com/2023/day/11

Usage: python day11.py <input_filepath>
"""
import argparse
import numpy as np
from itertools import combinations, starmap



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
        print(f"grid inital shape: {self.grid.shape}")
        self.expanded = None
        self.paths_sum = 0

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
            self.expanded = np.insert(self.expanded, row_ind+i, self.expanded[row_ind+i, :], axis=0)
        for j, col_ind in enumerate(empty_col_indices):
            self.expanded = np.insert(self.expanded, col_ind+j, self.expanded[:, col_ind+j], axis=1)
        print(f"expanded grid shape: {self.expanded.shape}")

    def compute(self) -> int:
        self._detect_galaxies()
        self.paths_sum = sum(
            starmap(self.get_shortest_path, combinations(self.galaxies_coords, 2))
        )
        print(f"{self.paths_sum=}")
        return self.paths_sum

    def _detect_galaxies(self) -> None:
        "detect # in the grid and get their (x, y) coordinates)"
        if not hasattr(self, "expanded"):
            raise Exception("You need to expand the grid first")
        self.galaxies_coords = np.argwhere(self.expanded == "#")
        #print(f"galaxies coords: {self.galaxies_coords}")

    def get_shortest_path(
        self, galaxy1: tuple[int, int], galaxy2: tuple[int, int]
    ) -> int:
        "Returns the shortest path between two galaxies"
        return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


if __name__ == "__main__":
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
