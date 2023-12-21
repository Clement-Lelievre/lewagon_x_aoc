"""AoC 2023 day 21

Performance note for part 1: replacing the deque with a list is OK for my input (the run time diff is negligible),
however it is critical to visit only once the same state (position, nb of steps) to avoid an explosion of the number
"""
import argparse
from collections import deque
from typing import Generator

import numpy as np

TEST_DATA = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


class StepCounter:
    def __init__(self, text: str) -> None:
        self.grid = None
        self.start_pos = None
        self.text = text
        self.process_input()

    def process_input(self) -> None:
        grid = np.array([list(line) for line in self.text.splitlines() if line.strip()])
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i, j] == "S":
                    print(f"Start position: {(i, j)}")
                    self.start_pos = (i, j)
                    grid[self.start_pos] = "."
                    self.grid = grid
                    print(f"{self.grid.shape=}")
                    return

    def neighbors(self, pos: tuple[int, int]) -> Generator[tuple[int, int], None, None]:
        i, j = pos
        if i - 1 >= 0 and self.grid[i - 1, j] == ".":
            yield (i - 1, j)
        if i + 1 < self.grid.shape[0] and self.grid[i + 1, j] == ".":
            yield (i + 1, j)
        if j - 1 >= 0 and self.grid[i, j - 1] == ".":
            yield (i, j - 1)
        if j + 1 < self.grid.shape[1] and self.grid[i, j + 1] == ".":
            yield (i, j + 1)

    def solve_p1(self, goal_nb_steps: int = 64) -> int:
        queue = deque(
            [(self.start_pos, 0)],
        )  # a queue storing (position, nb of steps), with O(1) pop and append
        end_pos = set()
        seen_pos = set()
        while queue:
            pos, nb_steps = queue.popleft()
            if (pos, nb_steps) in seen_pos:  # do not visit twice the same state
                continue
            seen_pos.add((pos, nb_steps))
            if nb_steps == goal_nb_steps:
                end_pos.add(pos)
                continue
            for neighbor in self.neighbors(pos):
                queue.append((neighbor, nb_steps + 1))
        answer = len(end_pos)
        print(f"Part 1: {answer=}")
        return answer


if __name__ == "__main__":
    test_step_counter = StepCounter(TEST_DATA)
    assert test_step_counter.solve_p1(goal_nb_steps=6) == 16
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()
    with open(args.input_file) as f:
        step_counter = StepCounter(f.read())
    step_counter.solve_p1()
