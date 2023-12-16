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


def find_reflection(grid: np.ndarray) -> tuple[int]:
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
                return pat_width + pat_top_line_ind, pat_top_line_ind
    return 0, None


def main_p1(text: str) -> int:
    grids = process_input(text)
    nb_cols_left = 0
    nb_rows_above = 0
    for grid in grids:
        nb_rows_above += (a := find_reflection(grid)[0])
        nb_cols_left += (b := find_reflection(np.rot90(grid, k=3))[0])
        assert a ^ b, "should be only one reflection"
        if nb_rows_above == 0 and nb_cols_left == 0:
            raise ValueError("no reflection found")
    answer = nb_cols_left + 100 * nb_rows_above
    print(f"part 1 {answer=}")
    return answer


def main_p2(text: str) -> int:
    grids = process_input(text)
    nb_cols_left = 0
    nb_rows_above = 0
    line_ind_data = []
    #find_reflection(grids[9]); import sys; sys.exit()

    for grid in grids:
        if (line_ind_r := find_reflection(grid)[1]) is not None:
            line_ind_data.append(("h", line_ind_r))
            continue
        if (line_ind_c := find_reflection(np.rot90(grid, k=3))[1]) is not None:
            line_ind_data.append(("v", line_ind_c))
            continue
        raise ValueError("no reflection found")
    assert len(line_ind_data) == len(grids)

    for grid_ind, grid in enumerate(grids):
        found = False
        for row_ind in range(grid.shape[0]):
            for col_ind in range(grid.shape[1]):
                fixed_grid = grid.copy()
                fixed_grid[row_ind, col_ind] = (
                    "#" if grid[row_ind, col_ind] == "." else "."
                )
                nb_r_fixed, pat_top_line_ind = find_reflection(fixed_grid)
                if nb_r_fixed > 0 and (
                    pat_top_line_ind != line_ind_data[grid_ind][1]
                    or line_ind_data[grid_ind][0] == "v"
                ):
                    nb_rows_above += nb_r_fixed
                    found = True
                    # print(f"{grid_ind=} {pat_top_line_ind=} {line_ind_data[grid_ind][1]=}")
                    # print(f"found {nb_r_fixed} rows {row_ind=} {col_ind=}")
                    #break
                nb_c_fixed, pat_top_line_ind = find_reflection(np.rot90(fixed_grid, k=3))
                if nb_c_fixed > 0 and (
                    pat_top_line_ind != line_ind_data[grid_ind][1]
                    or line_ind_data[grid_ind][0] == "h"
                ):
                    nb_cols_left += nb_c_fixed
                    found = True
                    #print(f"found {nb_c_fixed} cols {row_ind=} {col_ind=}")
                    #break

            if found:
                break
    # for row in grids[-1].T:
    #     print(*row)
    answer = nb_cols_left + 100 * nb_rows_above
    print(f"part 2 {answer=}")
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
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
