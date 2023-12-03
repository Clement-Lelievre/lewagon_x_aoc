"""AoC 2023 day 3: https://adventofcode.com/2023/day/3
Usage: python day3.py day3_input.txt
"""

import argparse
import math
import re
from typing import Generator

TEST_DATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# TEST_DATA = """
# ..2.2......
# ...*.......
# ...........
# """

NOT_A_SYMBOL = {"."} | set(map(str, range(10)))


def main_p1(input_: str) -> int:
    # make sure we don't catch empty lines
    lines = [line for line in input_.splitlines() if line.strip()]
    # pad the grid
    padded_lines = ["." * (len(lines[0]) + 2)]
    padded_lines.extend(["." + line + "." for line in lines])
    padded_lines.append("." * (len(lines[0]) + 2))
    answer = 0
    for line_nb, line in enumerate(padded_lines[1:-1], start=1):
        numbers_ind = [
            (line_nb, match_.start(0), match_.end(0))
            for match_ in re.finditer(r"\d+", line)
        ]
        for data in numbers_ind:
            for x, y in get_bounding_box(data):
                if padded_lines[x][y] not in NOT_A_SYMBOL:
                    answer += int(padded_lines[data[0]][data[1] : data[2]])
                    break
    print(f"part 1: {answer=}")
    return answer


def get_bounding_box(number_coords: tuple[int]) -> Generator[tuple[int], None, None]:
    line_nb, leftmost, rightmost = number_coords
    yield line_nb, leftmost - 1
    yield line_nb, rightmost
    for i in range(leftmost - 1, rightmost + 1):
        yield line_nb - 1, i
        yield line_nb + 1, i


def main_p2(input_: str) -> int:
    # make sure we don't catch empty lines
    lines = [line for line in input_.splitlines() if line.strip()]
    # pad the grid
    padded_lines = ["." * (len(lines[0]) + 2)]
    padded_lines.extend(["." + line + "." for line in lines])
    padded_lines.append("." * (len(lines[0]) + 2))
    answer = 0
    gears_data = {}
    numbers_data = {}
    # gather data abt the grid
    for line_nb, line in enumerate(padded_lines):
        # get indices of asterisks
        asterisk_indices = [match_.start(0) for match_ in re.finditer(r"\*", line)]
        if asterisk_indices:
            gears_data[line_nb] = asterisk_indices
        # get indices of numbers
        numbers_data[line_nb] = {
            range(match_.start(0), match_.end(0)): int(match_.group())
            for match_ in re.finditer(r"\d+", line)
        }
    # find gears
    for gear_line_ind, gear_col_indices in gears_data.items():
        for gear_col_ind in gear_col_indices:
            neighbours = set()
            # numbers on the same line
            for number_range, number in numbers_data.get(gear_line_ind, {}).items():
                if gear_col_ind - 1 in number_range:
                    neighbours.add((gear_line_ind, number, gear_col_ind - 1))
                if gear_col_ind + 1 in number_range:
                    neighbours.add((gear_line_ind, number, gear_col_ind + 1))
            # numbers on the line above
            for number_range, number in numbers_data.get(gear_line_ind - 1, {}).items():
                for col_ in (gear_col_ind - 1, gear_col_ind, gear_col_ind + 1):
                    if col_ in number_range:
                        neighbours.add((gear_line_ind - 1, number, col_))
                        break
            # numbers on the line below
            for number_range, number in numbers_data.get(gear_line_ind + 1, {}).items():
                for col_ in (gear_col_ind - 1, gear_col_ind, gear_col_ind + 1):
                    if col_ in number_range:
                        neighbours.add((gear_line_ind + 1, number, col_))
                        break
            if len(neighbours) == 2:
                answer += math.prod(elem[1] for elem in neighbours)
    print(f"part 2: {answer=}")
    return answer


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 4361, "should be 4361 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    assert main_p2(TEST_DATA) == 467835, "should be 467835 for the test input p2"
    main_p2(text)
