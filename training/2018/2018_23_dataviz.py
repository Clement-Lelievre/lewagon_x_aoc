"""Dataviz for Advent of Code 2018, day 23
Note this is intended for small values: it does not scale to large number of bots and especially
to large radiuses"""
import re
from functools import cache
from collections import defaultdict
import plotly.express as px
import pandas as pd


INPUT_TEST = """pos=<1,0,0>, r=4
pos=<0,0,6>, r=1
pos=<0,-8,0>, r=3"""


class Nanobots:
    """Extracts and computes coordinates data about the nanobots given in the input"""

    NUMBERS_PAT = re.compile(r"[-\d]+")

    def __init__(self, input_: str) -> None:
        self.get_nanobots(input_)
        self.get_in_range_coords()

    def get_nanobots(self, input_: str) -> None:
        self.nanobots = []
        for row in input_.splitlines():
            if numbers := Nanobots.NUMBERS_PAT.findall(row):
                *pos, radius = map(int, numbers)
                self.nanobots.append((tuple(pos), radius))

    @cache
    @staticmethod
    def manhattan_dist(pos1: tuple[int], pos2: tuple[int]) -> int:
        """Computes the Manhattan distance between two points

        Args:
            pos1 (tuple[int]): x,y,z
            pos2 (tuple[int]): x,y,z

        Returns:
            int: the Manhattan distance
        """
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

    def get_in_range_coords(self) -> None:
        """Creates a dict (`self.in_range_coords`) that stores the coordinates in range of each nanobot
        (key: nanobot, value: set of its in-range coordinates)
        """
        self.in_range_coords = defaultdict(list)
        for (x, y, z), radius in self.nanobots:
            for x_cand in range(x - radius, x + radius + 1):
                for y_cand in range(y - radius, y + radius + 1):
                    for z_cand in range(z - radius, z + radius + 1):
                        if (
                            Nanobots.manhattan_dist((x, y, z), (x_cand, y_cand, z_cand))
                            <= radius
                        ):
                            self.in_range_coords["x"].append(x_cand)
                            self.in_range_coords["y"].append(y_cand)
                            self.in_range_coords["z"].append(z_cand)
                            self.in_range_coords["center"].append((x, y, z))

    def plot_in_range(self) -> None:
        fig = px.scatter_3d(
            pd.DataFrame(self.in_range_coords),
            x="x",
            y="y",
            z="z",
            color="center",
            title="The bots and their respective reach",
        )
        fig.show()


if __name__ == "__main__":
    bots = Nanobots(INPUT_TEST)
    bots.plot_in_range()
