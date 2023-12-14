"""AoC 2023 day 13: https://adventofcode.com/2023/day/13

Usage: python day13.py <input_filepath>
"""
import argparse
from tqdm import tqdm
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


def main_p1(text: str) -> int:
    grids = process_input(text)
    nb_cols_left = 0
    nb_rows_above = 0
    for grid in grids:
        nb_rows_above += find_reflection(grid)
        nb_cols_left += find_reflection(grid.T)
    answer = nb_cols_left + 100 * nb_rows_above
    print(f"part 1 {answer=}")
    return answer


def main_p2(text: str) -> int:
    grids = process_input(text)
    nb_cols_left = 0
    nb_rows_above = 0
    for grid in tqdm(grids):
        found = False
        for row_ind in range(grid.shape[0]):
            for col_ind in range(grid.shape[1]):
                fixed_grid = grid.copy()
                fixed_grid[row_ind, col_ind] = (
                    "#" if grid[row_ind, col_ind] == "." else "."
                )
                if nb_rows_fixed_grid := find_reflection(fixed_grid):
                    nb_rows_above += nb_rows_fixed_grid
                    found = True
                    print(f"found {nb_rows_fixed_grid} rows {row_ind=} {col_ind=}")
                    break
                if nb_cols_fixed_grid := find_reflection(fixed_grid.T):
                    nb_cols_left += nb_cols_fixed_grid
                    found = True
                    break

            if found:
                break
    answer = nb_cols_left + 100 * nb_rows_above
    print(f"part 2 {answer=}")
    return answer


if __name__ == "__main__":
    assert (
        attempt := main_p1(TEST_DATA)
    ) == 405, f"should be 405 for the test input p1, found {attempt}"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path) as f:
        text = f.read()
    main_p1(text)
    assert (
        attempt := main_p2(TEST_DATA)
    ) == 400, f"should be 400 for the test input p2, found {attempt}"
    main_p2(text)
