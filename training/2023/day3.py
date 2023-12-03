"""AoC 2023 day 3: https://adventofcode.com/2023/day/3"""

import argparse
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
    print(answer)
    return answer


def get_bounding_box(number_coords: tuple[int]) -> Generator[int, int]:
    line_nb, leftmost, rightmost = number_coords
    yield line_nb, leftmost - 1
    yield line_nb, rightmost
    for i in range(leftmost - 1, rightmost + 1):
        yield line_nb - 1, i
        yield line_nb + 1, i


def main_p2(input_: str) -> int:
    ...


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 4361, "should be 4361 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    # assert main_p2(TEST_DATA) == 2286, "should be 2286 for the test input p2"
    # main_p2(text)
