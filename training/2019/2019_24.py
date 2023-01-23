import numpy as np
from functools import partial

# the first thing I thought about when reading the challenge was
# implementing some bitmasks to do it efficiently
# if I need to improve the perf then I'll consider this approach
# https://dev.to/anurag629/the-power-of-bit-manipulation-how-to-solve-problems-efficiently-3p1h

INPUT = """
..##.
..#..
##...
#....
...##"""

# INPUT = """
# ....#
# #..#.
# #..##
# ..#..
# #...."""

# first the intuitive method, then maybe I'll try some bitwise operations
class Eris:
    """Mimics life on Eris"""

    mapping = str.maketrans(".#", "01")
    numpy_to_bin = partial(int, base=2)

    def __init__(self, input_: str) -> None:
        self.grid = np.array(
            [
                list(row.translate(self.mapping))
                for row in input_.splitlines()
                if row.strip()
            ],
            dtype=int,
        )
        self.nb_rows, self.nb_cols = self.grid.shape
        self.neighbours = {
            (i, j): frozenset(
                (
                    (a, b)
                    for a, b in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j))
                    if 0 <= a < self.nb_rows and 0 <= b < self.nb_cols
                )
            )
            for i in range(self.nb_rows)
            for j in range(self.nb_cols)
        }
        assert len(self.neighbours) == self.grid.size

    def grid_to_bio_rating(self) -> int:
        """From numpy array to binary number representation"""
        return self.numpy_to_bin("".join(map(str, self.grid.flatten()))[::-1])

    def update_grid(self) -> None:
        new_grid = np.zeros_like(self.grid)
        for row, col in self.neighbours:
            adj_sum = sum(self.grid[neigh] for neigh in self.neighbours[(row, col)])
            new_grid[row, col] = (
                (0, 1)[adj_sum == 1]
                if self.grid[row, col] == 1
                else (0, 1)[adj_sum in (1, 2)]
            )
            # even fancier Python boolean indexing:
            # new_grid[row, col] = ((0, 1)[adj_sum == 1], (0, 1)[adj_sum in (1, 2)])[self.grid[row, col] == 0]
        self.grid = new_grid

    def solve(self) -> None:
        seen = set()
        current = self.grid_to_bio_rating()
        while current not in seen:
            seen.add(current)
            self.update_grid()
            current = self.grid_to_bio_rating()
        print("part 1:", current)


Eris_part1 = Eris(INPUT)
Eris_part1.solve()
