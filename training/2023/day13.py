"""AoC 2023 day 13: https://adventofcode.com/2023/day/13

Usage: python day13.py <input_filepath>
"""
import argparse
from typing import Generator

import numpy as np

TEST_DATA = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def process_input(text: str) -> list[np.ndarray]:
    """Process input text into a list of numpy arrays"""
    grids = []
    current_grid = []
    for row in text.splitlines():
        if not row.strip():
            grids.append(current_grid)
            current_grid = []
            continue
        current_grid.append(list(row))
    grids.append(current_grid)
    grids = list(map(np.array, grids))
    print(f"found {len(grids)} grids")
    return grids


def find_reflection(grid: np.ndarray) -> int:
    """Find the uniqe reflection of a grid, if any, for part 1
    specifically this returns the number of rows above the reflection
    (or columns to the left if the reflection is vertical)
    """
    for pat_width in range(grid.shape[0] // 2, 0, -1):
        for pat_top_line_ind in range(grid.shape[0] - 2 * pat_width + 1):
            if (
                grid[pat_top_line_ind : pat_top_line_ind + pat_width]
                == grid[
                    pat_top_line_ind + pat_width : pat_top_line_ind + 2 * pat_width
                ][::-1, :]
            ).all() and (
                pat_top_line_ind == 0
                or pat_top_line_ind + pat_width * 2 == grid.shape[0]
            ):
                return pat_width + pat_top_line_ind
    return 0


def find_all_reflections(grid: np.ndarray) -> Generator[int, None, None]:
    """Find all the reflections of a grid, if any, for part 2
    specifically this yields the number of rows above the reflection
    (or columns to the left if the reflection is vertical)
    """
    for pat_width in range(grid.shape[0] // 2, 0, -1):
        for pat_top_line_ind in range(grid.shape[0] - 2 * pat_width + 1):
            if (
                grid[pat_top_line_ind : pat_top_line_ind + pat_width]
                == grid[
                    pat_top_line_ind + pat_width : pat_top_line_ind + 2 * pat_width
                ][::-1, :]
            ).all() and (
                pat_top_line_ind == 0
                or pat_top_line_ind + pat_width * 2 == grid.shape[0]
            ):
                yield pat_width + pat_top_line_ind


def main_p1(text: str) -> int:
    grids = process_input(text)
    nb_cols_left = 0
    nb_rows_above = 0
    for grid in grids:
        nb_rows_above += (a := find_reflection(grid))
        nb_cols_left += (b := find_reflection(np.rot90(grid, k=3)))
        assert a ^ b, "should be only one reflection"
        if nb_rows_above == 0 and nb_cols_left == 0:
            raise ValueError("no reflection found")
    answer = nb_cols_left + 100 * nb_rows_above
    print(f"part 1 {answer=}")
    return answer


def process_p2(grid: np.ndarray, line_ind_data: list, grid_ind: int) -> int:
    for row_ind in range(grid.shape[0]):
        for col_ind in range(grid.shape[1]):
            fixed_grid = grid.copy()
            fixed_grid[row_ind, col_ind] = "#" if grid[row_ind, col_ind] == "." else "."
            for grid_nb_rows_above in find_all_reflections(fixed_grid):
                if (
                    grid_nb_rows_above != line_ind_data[grid_ind][1]
                    or line_ind_data[grid_ind][0] == "v"
                ):
                    return grid_nb_rows_above * 100

            for grid_nb_cols_above in find_all_reflections(np.rot90(fixed_grid, k=3)):
                if grid_nb_cols_above != 0 and (
                    grid_nb_cols_above != line_ind_data[grid_ind][1]
                    or line_ind_data[grid_ind][0] == "h"
                ):
                    return grid_nb_cols_above


def main_p2(text: str) -> int:
    # TODO: clean this up. Could use a namedtuple for dot notation access and enhanced readability
    grids = process_input(text)
    line_ind_data = []

    for grid in grids:
        if p1_nb_rows_above := find_reflection(grid):
            line_ind_data.append(("h", p1_nb_rows_above))
            continue
        if p1_nb_cols_left := find_reflection(np.rot90(grid, k=3)):
            line_ind_data.append(("v", p1_nb_cols_left))
            continue
        raise ValueError("no reflection found")
    assert len(line_ind_data) == len(grids)
    answer = 0
    for grid_ind, grid in enumerate(grids):
        answer += process_p2(grid, line_ind_data, grid_ind)
    print(f"part 2 {answer=}")
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path) as f:
        text = f.read()
    assert (
        attempt := main_p1(TEST_DATA)
    ) == 405, f"should be 405 for the test input p1, found {attempt}"
    main_p1(text)
    assert (
        attempt := main_p2(TEST_DATA)
    ) == 400, f"should be 400 for the test input p2, found {attempt}"
    main_p2(text)
