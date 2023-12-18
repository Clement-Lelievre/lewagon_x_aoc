"""AoC 2023 day 18: https://adventofcode.com/2023/day/18

Usage: python day18.py <input_filepath>
"""

import argparse
from typing import Generator

import numpy as np

TEST_DATA = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


class Digger:
    def __init__(self, text: str) -> None:
        self.text = text
        self.w, self.h = 800, 800
        self.arr = np.zeros((self.w, self.h), dtype=int)
        self.instructions = self.get_instructions()
        self.answer = None
        print(f"{self.arr.shape=}")

    def get_instructions(self) -> list[tuple]:
        instructions = []
        for line in self.text.splitlines():
            direction, steps = line.split()[:2]
            steps = int(steps)
            instructions.append((direction, steps))
        return instructions

    def dig_trench(self) -> int:
        x, y = (self.arr.shape[0] // 2, self.arr.shape[1] // 2)  # start position
        self.arr[x, y] = 1
        for direction, size in self.instructions:
            if direction == "R":
                self.arr[x, y + 1 : y + size + 1] = 1
                y = y + size
            elif direction == "L":
                self.arr[x, y - size : y] = 1
                y = y - size
            elif direction == "U":
                self.arr[x - size : x, y] = 1
                x = x - size
            elif direction == "D":
                self.arr[x + 1 : x + size + 1, y] = 1
                x = x + size
        # for row in self.arr:
        #     print(*row)
        # print()

        return self.arr.sum()

    def dig_inside(self) -> int:
        # reduce array to fit exactly the trench, not more
        # on the left, the leftmost column should be the first column that contains a 1
        leftmost_one_column = np.where(self.arr.sum(axis=0) > 0)[0][0]
        rightmost_one_column = np.where(self.arr.sum(axis=0) > 0)[0][-1]
        topmost_one_row = np.where(self.arr.sum(axis=1) > 0)[0][0]
        bottommost_one_row = np.where(self.arr.sum(axis=1) > 0)[0][-1]
        self.arr = self.arr[
            topmost_one_row : bottommost_one_row + 1,
            leftmost_one_column : rightmost_one_column + 1,
        ]
        print(f"After focusing array: {self.arr.shape=}")
        # find starting point inside the trench
        x, y = (self.arr.shape[0] - 1, self.arr.shape[1] // 2)
        nb_rows_crossed = self.arr[:x, y].sum()
        while nb_rows_crossed % 2 == 0 or self.arr[x, y] == 1:
            x -= 1
            nb_rows_crossed = self.arr[:x, y].sum()
        # flood fill
        visited = set()
        todo = [(x, y)]
        while todo:
            x, y = todo.pop()
            if (x, y) in visited or self.arr[x, y] == 1:
                continue
            visited.add((x, y))
            self.arr[x, y] = 1
            for neigh in self.get_neighbors(x, y):
                todo.append(neigh)
        self.answer = self.arr.sum()
        # for row in self.arr:
        #     print(*row)
        # print()

        return self.answer

    def get_neighbors(self, x: int, y: int) -> Generator[tuple, None, None]:
        if x + 1 < self.arr.shape[0]:
            yield (x + 1, y)
        if x - 1 >= 0:
            yield (x - 1, y)
        if y + 1 < self.arr.shape[1]:
            yield (x, y + 1)
        if y - 1 >= 0:
            yield (x, y - 1)

    def solve_p1(self) -> int:
        self.dig_trench()
        self.dig_inside()
        # for row in self.arr:
        #     print(*row)
        print(f"Part 1: {self.answer}")
        return self.answer


if __name__ == "__main__":
    test_digger = Digger(TEST_DATA)
    assert test_digger.dig_trench() == 38
    assert test_digger.solve_p1() == 62
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path) as f:
        text = f.read()
    digger = Digger(text)
    digger.solve_p1()
