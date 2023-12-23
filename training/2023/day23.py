"""AoC 2023 day 23: https://adventofcode.com/2023/day/23

Usage: python day23.py <input_path>
"""
import numpy as np
import argparse
from collections import deque, defaultdict

TEST_DATA = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


class Hiker:
    def __init__(self, grid: str) -> None:
        self.grid_str = grid
        self.process_grid()
        self.find_endpoints()
        self.neighbors_p1 = defaultdict(set)
        self.neighbors_p2 = defaultdict(set)

    def find_endpoints(self) -> None:
        """'You're currently on the single path tile in the top row;
        your goal is to reach the single path tile in the bottom row'"""
        for j in range(self.grid.shape[1]):
            if self.grid[0, j] == ".":
                self.start = (0, j)
                print(f"{self.start=}")
                break
        for j in range(self.grid.shape[1]):
            if self.grid[-1, j] == ".":
                self.target = (self.grid.shape[0] - 1, j)
                print(f"{self.target=}")
                break
        if not all([hasattr(self, "start"), hasattr(self, "target")]):
            raise ValueError("start and/or end coords not found: check grid")

    def process_grid(self) -> None:
        self.grid = np.array(
            [list(row) for row in self.grid_str.splitlines() if row.strip()]
        )
        print(f"{self.grid.shape=}")

    def find_neighbors(
        self,
        part1: bool,
    ) -> None:
        """Stores in a cache (a dict) valid neighbors

        Args:
            part1 (bool): whether to find neighbors as defined in part1 or in part2
        """
        neigh_dict = self.neighbors_p1 if part1 else self.neighbors_p2
        for x in range(self.grid.shape[0]):
            for y in range(self.grid.shape[1]):
                for neigh_x, neigh_y in [
                    (x + 1, y),
                    (x, y + 1),
                    (x - 1, y),
                    (x, y - 1),
                ]:
                    if any(
                        [
                            neigh_x < 0,
                            neigh_y < 0,
                            neigh_y > self.grid.shape[1] - 1,
                            neigh_x > self.grid.shape[0] - 1,
                        ]
                    ):
                        continue
                    if self.grid[neigh_x, neigh_y] == "#":
                        continue
                    if part1 is False:
                        neigh_dict[(x, y)].add((neigh_x, neigh_y))
                        continue
                    if not any(
                        [
                            (
                                self.grid[x, y] == "<"
                                and (neigh_x, neigh_y) != (x, y - 1)
                            ),
                            (
                                self.grid[x, y] == ">"
                                and (neigh_x, neigh_y) != (x, y + 1)
                            ),
                            (
                                self.grid[x, y] == "^"
                                and (neigh_x, neigh_y) != (x - 1, y)
                            ),
                            (
                                self.grid[x, y] == "v"
                                and (neigh_x, neigh_y) != (x + 1, y)
                            ),
                        ]
                    ):

                        neigh_dict[(x, y)].add((neigh_x, neigh_y))

    def solve(self, *, solve_part1: bool) -> int:
        self.find_neighbors(solve_part1)
        neighbors_dict = (self.neighbors_p2, self.neighbors_p1)[solve_part1]
        longest_to_coord: dict[tuple[int, int], int] = defaultdict(int)
        queue = deque(
            [(self.start[0], self.start[1], 0, {(self.start[0], self.start[1])})]
        )  # x, y, distance so far, unique visited coords so far
        longest_hike = 0
        while queue:
            x, y, dist, path = queue.popleft()
            if (x, y) == self.target:
                if dist > longest_hike:
                    longest_hike = dist
                    print(f"new best: {longest_hike=}")
                continue
            if longest_to_coord[(x, y)] > dist:
                continue
            longest_to_coord[(x, y)] = dist
            queue.extend(
                [
                    (neigh[0], neigh[1], dist + 1, path | {neigh})
                    for neigh in neighbors_dict[(x, y)]
                    if neigh not in path
                ]
            )
        return longest_hike


if __name__ == "__main__":
    test_hiker = Hiker(TEST_DATA)
    assert test_hiker.solve(solve_part1=True) == 94
    assert test_hiker.solve(solve_part1=False) == 154
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path) as f:
        text = f.read()
    hiker = Hiker(text)
    hiker.solve(solve_part1=True)
    # hiker.solve(solve_part1=False)
