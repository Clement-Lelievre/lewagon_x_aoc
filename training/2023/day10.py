"""AoC 2023 day 10: https://adventofcode.com/2023/day/10

Usage: python day10.py <input_filepath>
"""
import argparse
import numpy as np

TEST_DATA_1 = """
.....
.S-7.
.|.|.
.L-J.
.....
"""

TEST_DATA_2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""


def get_neighbors(pos: set, grid: np.ndarray) -> tuple[int, int]:
    x, y = pos
    match grid[pos]:
        case "|":
            return (x - 1, y), (x + 1, y)
        case "7":
            return (x, y - 1), (x + 1, y)
        case "F":
            return (x, y + 1), (x + 1, y)
        case "L":
            return (x, y + 1), (x - 1, y)
        case "J":
            return (x - 1, y), (x, y - 1)
        case "-":
            return (x, y - 1), (x, y + 1)
        case _:
            raise ValueError


def main_p1(grid: str) -> int:
    if grid.count("S") != 1:
        raise ValueError("There should be exactly one S in the grid")
    lines = [line for line in grid.splitlines() if line.strip()]
    # find S coords
    found_s = False
    for row_ind, line in enumerate(lines):
        for col_ind, char in enumerate(line):
            if char == "S":
                S_pos = (row_ind, col_ind)
                found_s = True
                break
        if found_s:
            break
    else:
        raise Exception("S not found on the grid")
    grid = np.array([list(line) for line in lines])
    # I cheated a bit by looking at the grid and seeing that the 2 connected neighbors of S are 7 up and - left
    # to work on ANY input grid, I need to add code that automates finding the two connected neighbors of S
    # i'll start left but that works starting north too obviously
    visited = set()
    visited.add(S_pos)
    # move left one step
    pos = S_pos[0], S_pos[1] - 1
    nb_steps = 1
    # move in the pipe
    while pos != S_pos:
        visited.add(pos)
        neighbors = get_neighbors(pos, grid)
        for neigh in neighbors:
            if neigh == S_pos and nb_steps > 2:
                answer = (nb_steps + 1) / 2
                print(f"part 1: {answer=}")
                return answer
            if neigh not in visited:
                nb_steps += 1
                pos = neigh
    raise Exception("No solution found")


if __name__ == "__main__":
    # assert main_p1(TEST_DATA_1) == 4, "should be 4 for the test input p1"
    # assert main_p1(TEST_DATA_2) == 8, "should be 8 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    # assert main_p2(TEST_DATA) == 2, "should be 2 for the test input p2"
    # main_p2(text)
