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


class Dish:
    def __init__(self, data: str) -> None:
        self.data = data
        self.grid: np.ndarray = np.array(
            [list(line) for line in data.splitlines() if line.strip()]
        )

    def reset_grid(self) -> None:
        self.grid = np.array(
            [list(line) for line in self.data.splitlines() if line.strip()]
        )

    def rotate_grid_counter_clockwise(self) -> None:
        self.grid = np.rot90(self.grid, 3)

    def solve_p1(self) -> int:
        self.move()
        answer = self.compute_load()
        print(f"answer part 1: {answer}")
        return answer

    def move(self) -> None:
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
                load += self.grid.shape[0] - row_nb
        return load

    def solve_p2(self, nb_cycles: int = 1_000_000_000) -> int:
        """Identify the begining sequence of load values, that does NOT contain a cycle, and its length, say l1

        Identify the cycle and its length say l2

        Compute the answer as the value of the load at the position (`nb_cycles` - l1) % l2 + l1,
        i.e. at index (nb_cycles - l1) % l2 + l1 - 1
        """
        grids_bytes = []
        ordered_load_values = []
        current_bytes_val = None
        while True:
            # complete one cycle
            for _ in range(4):
                self.move()
                self.rotate_grid_counter_clockwise()
            current_bytes_val = self.grid.tobytes()
            if current_bytes_val in grids_bytes:
                first_repeat_index = grids_bytes.index(current_bytes_val)
                break
            grids_bytes.append(current_bytes_val)
            ordered_load_values.append(self.compute_load())
        cycle_array = ordered_load_values[first_repeat_index:]
        answer = cycle_array[(nb_cycles - first_repeat_index) % len(cycle_array) - 1]
        print(f"answer part 2: {answer}")
        return answer


if __name__ == "__main__":
    test_dish = Dish(TEST_DATA)
    assert (
        attempt := test_dish.solve_p1()
    ) == 136, f"should be 136 for the test input p1, found {attempt}"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path) as f:
        text = f.read()
    dish = Dish(text)
    dish.solve_p1()
    test_dish.reset_grid()
    dish.reset_grid()
    assert (
        attempt := test_dish.solve_p2()
    ) == 64, f"should be 64 for the test input p2, found {attempt}"
    dish.solve_p2()
