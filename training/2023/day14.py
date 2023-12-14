"""AoC 2023 day 14: https://adventofcode.com/2023/day/14

Usage: python day14.py <input_filepath>
"""
import argparse

import numpy as np

TEST_DATA = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

# move all O north as far as possible, knowing that # prevents movement
# i'll use a numpy array for this


class Dish:
    def __init__(self, data: str) -> None:
        self.grid = np.array([list(line) for line in data.splitlines() if line.strip()])

    def solve(self) -> int:
        self.move_north()
        answer = self.compute_load()
        print(f"answer part 1: {answer}")
        return answer

    def move_north(self) -> None:
        for row_nb in range(1, self.grid.shape[0]):
            for col_nb in range(self.grid.shape[1]):
                if self.grid[row_nb, col_nb] != "O":
                    continue
                upper_row = row_nb - 1
                up_neighbor = self.grid[upper_row, col_nb]
                moved_up = False
                while up_neighbor == "." and upper_row >= 0:
                    moved_up = True
                    upper_row -= 1
                    up_neighbor = self.grid[upper_row, col_nb]

                if moved_up:
                    self.grid[upper_row + 1, col_nb] = "O"
                    self.grid[row_nb, col_nb] = "."

    def compute_load(self) -> int:
        load = 0
        for row_nb in range(self.grid.shape[0]):
            for col_nb in range(self.grid.shape[1]):
                if self.grid[row_nb, col_nb] != "O":
                    continue
                subcolumn = self.grid[row_nb:, col_nb]
                load += len(subcolumn != "#")  # .sum()
        return load


if __name__ == "__main__":
    test_dish = Dish(TEST_DATA)
    assert (
        attempt := test_dish.solve()
    ) == 136, f"should be 136 for the test input p1, found {attempt}"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path) as f:
        text = f.read()
    dish = Dish(text)
    dish.solve()
    # assert (
    #     attempt := main_p2(TEST_DATA)
    # ) == 400, f"should be 400 for the test input p2, found {attempt}"
    # main_p2(text)
