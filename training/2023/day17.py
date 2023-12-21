"""AoC 2023 day 17: https://adventofcode.com/2023/day/17

Usage: python day17.py --input_path <input_filepath>
"""
import argparse
import numpy as np
from collections import defaultdict
from typing import Generator
import heapq

TEST_DATA = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


class HeatLossOptimizer:
    def __init__(self, grid: str) -> None:
        self.grid = self._process_input(grid)
        print(f"Grid shape: {self.grid.shape}")
        self.distances = defaultdict(dict)

    @staticmethod
    def _process_input(grid: str) -> np.ndarray:
        return np.array(
            [
                [int(digit) for digit in line]
                for line in grid.splitlines()
                if line.strip()
            ]
        )


#     def solve_p1(self, view_path: bool = False) -> int:
#         start = (0, 0)
#         target = (self.grid.shape[0] - 1, self.grid.shape[1] - 1)
#         path_sum, path, *_ = self.djikstra_shortest_path_length(start, target)
#         print(f"Part 1: {path_sum=} {path=}", end="\n\n")
#         grid_str = self.grid.copy().astype(str)
#         if view_path:
#             for coord in path:
#                 grid_str[coord] = "X"
#             grid_str[grid_str != "X"] = "."
#             for row in grid_str:
#                 print(*row)
#         return path_sum

#     def get_neighbors(self, node: tuple[int]) -> Generator[tuple, None, None]:
#         """Return the neighbors of a given node"""
#         row_ind, col_ind = node
#         grid_nb_rows, grid_nb_cols = self.grid.shape
#         if row_ind > 0:
#             yield (row_ind - 1, col_ind), "u"
#         if row_ind < grid_nb_rows - 1:
#             yield (row_ind + 1, col_ind), "d"
#         if col_ind > 0:
#             yield (row_ind, col_ind - 1), "l"
#         if col_ind < grid_nb_cols - 1:
#             yield (row_ind, col_ind + 1), "r"

#     def path_is_valid(self, path: list[tuple[int, int]]) -> bool:
#         """Checks whether a path is valid i.e. does not feature more than 3 consecutive times the same direction

#         Args:
#             path (list[tuple[int, int]]): the path as a list of ordered grid coordinates

#         Returns:
#             bool: whether the path is valid
#         """
#         if len(path) <= 2:
#             return True
#         tail = path[
#             -5:
#         ]  # I need five coords to check for the 4th consecutive direction
#         directions = []
#         for i in range(1, len(tail)):
#             prev, curr = tail[i - 1], tail[i]
#             assert abs(prev[0] - curr[0]) + abs(prev[1] - curr[1]) == 1
#             if curr[0] == prev[0] + 1:
#                 directions.append("d")  # down
#             if curr[0] == prev[0] - 1:
#                 directions.append("u")  # up
#             if curr[1] == prev[1] + 1:
#                 directions.append("r")  # right
#             if curr[1] == prev[1] - 1:
#                 directions.append("l")  # left
#         # it can move at most three blocks in a single direction before it must turn 90 degrees left or right
#         if len(set(directions)) == 1 and len(directions) == 4:
#             return False
#         # The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.
#         for i in range(1, len(directions)):
#             if directions[i] == "u" and directions[i - 1] == "d":
#                 return False
#             if directions[i] == "d" and directions[i - 1] == "u":
#                 return False
#             if directions[i] == "l" and directions[i - 1] == "r":
#                 return False
#             if directions[i] == "r" and directions[i - 1] == "l":
#                 return False
#         return True

#     def collect_distances(self) -> None:
#         # Step1: Transform the  dataframe to a graph-like structure, linking each node to its neighbors and register their relative distance
#         grid_nb_rows, grid_nb_cols = self.grid.shape
#         nodes = [
#             (row_ind, col_ind)
#             for row_ind in range(grid_nb_rows)
#             for col_ind in range(grid_nb_cols)
#         ]

#         for node in nodes:
#             neighbors = self.get_neighbors(node)
#             for neighbor, _ in neighbors:
#                 self.distances[node][neighbor] = self.grid[neighbor]
#                 self.distances[neighbor][node] = self.grid[node]
#         print(self.distances)

#     def djikstra_shortest_path_length(
#         self, start: tuple[int], target: tuple[int]
#     ) -> tuple:
#         """Credits to 'data puzzles' for the Djikstra implem I took inspiration from"""
#         self.collect_distances()
#         # Initialise a set of 'visited' nodes as we are going to visit them one by one
#         visited = set()

#         # Initialise a dictionary registering for all nodes the shortest path discovered
#         # from the start node
#         # shortest_path = {start: (self.grid[0, 0], [start])}
#         shortest_path = {
#             (start, (start,)): (0, [start])
#         }  # store, path sum, path, last 3 directions
#         # While we have not visited all the connected nodes of the start node
#         unvisited = set(shortest_path) - visited
#         while unvisited:
#             # Take the one that is not visited and closest to the start node
#             current_node = min(unvisited, key=shortest_path.get)

#             # Update its neighbors shortest path value
#             for neighbor, distance in self.distances[current_node].items():
#                 # Check if we need to update the shortest path:
#                 # yes if we never seen this node before
#                 # yes if we just discovered a shorter path to this node
#                 new_dist = (
#                     shortest_path[current_node][0]
#                     + distance
#                 )
#                 new_path = shortest_path[current_node][1] + [neighbor]
#                 #new_directions = (shortest_path[current_node][2] + direction)[-3:]
#                 if (
#                     neighbor not in shortest_path
#                     or new_dist <= shortest_path[neighbor][0]
#                 ) and self.path_is_valid(new_path):
#                     shortest_path[neighbor, tuple(new_path[-3:])] = new_dist, new_path

#             # Mark visited and go to next one
#             visited.add(current_node)
#             unvisited = set(shortest_path) - visited

#         answer = shortest_path[target]
#         return answer

# We need to find a path from a start to a goal, where the cost varies depending on the path taken. As usual for a Dijkstra, we need to use a priority queue. First, we need to define some way to represent the state of our journey through the map. I'll represent state in a tuple that stores (cost, current position, direction, straight steps taken). It's important that cost comes first, because our priority queue pops the next state based on the lowest value of the first item in the tuple.

# We keep popping next states until we reach the goal. To determine valid next states:

#     We create set to store states that we've already explored.
#     If we're in our initial position, we don't have a direction yet. So we can try all adjacent squares, and with each, we set straight steps to 1.
#     If we're not on the first step, then our valid next moves are left, right, or straight on. We can't go backwards.
#         We can move left relative to our current direction by adding the vector Point(-dirn.y, dirn.x).
#         We can move right relative to our current direction by adding the vector Point(dirn.y, -dirn.x).
#         We can only go straight if straight steps is less than 3.
#     Now we've got our new position and new direction, we can determine the cost of the next move, and add that cost to our current cumulative cost.

# Finally, we return the total cumulative cost, when we reach the goal.


def get_path(
    grid: list[list[int]], start: tuple[int], goal: tuple[int], max_straight: int
):
    """Determine the path with lowest cost from start to goal

    Args:
        grid (list[list[int]]): A 2D grid containing int values
        start (Point): Starting point
        goal (Point): Final point
        max_straight (int): Max moves we can make in a straight line before turning

    Raises:
        ValueError: If no solution

    Returns:
        int: best cost for path
    """
    queue = []  # priority queue to store current state

    cost = 0
    current_posn = start
    dirn = None  # Current direction. (None when we start.)
    straight_steps: int = 0  # number of steps taken in one direction without turning
    heapq.heappush(
        queue, (cost, current_posn, dirn, straight_steps)
    )  # cost must come first for our priority queue

    seen = set()

    while queue:
        cost, current_posn, dirn, straight_steps = heapq.heappop(queue)
        # logger.debug(f"{cost=}, {current_posn=}, {dirn=}, {steps=}")

        if current_posn == goal:
            print(f"Found solution: {cost=}")
            return cost

        # check if we've been in this configuration before
        if (current_posn, dirn, straight_steps) in seen:
            continue

        seen.add((current_posn, dirn, straight_steps))  # explored

        next_states = []  # point, dirn, steps
        if dirn is None:  # we're at the start, so we can go in any direction
            for dir_x, dir_y in ((0, 1), (1, 0), (0, 1), (-1, 0)):
                dirn = (dir_x, dir_y)
                neighbour = (current_posn[0] + dir_x, current_posn[1] + dir_y)
                next_states.append((neighbour, dirn, 1))
        else:
            next_states.append(
                ((current_posn[0],current_posn[1]-1), (-dir_y, dir_x), 1)
            )  # turn 90 degrees CCW (left)
            next_states.append(
                ((current_posn[0],current_posn[1]+1), (dir_y, -dir_x), 1)
            )  # turn 90 degrees CW (right)

            if straight_steps < max_straight:  # we can move straight ahead.
                next_states.append(((current_posn + dirn), dirn, straight_steps + 1))

        for neighbour, dirn, new_steps in next_states:
            if 0 <= neighbour.x < len(grid[0]) and 0 <= neighbour.y < len(grid):
                new_cost = cost + grid[neighbour.y][neighbour.x]
                # heuristic = new_cost + neighbour.manhattan_distance_from(goal)
                heapq.heappush(queue, (new_cost, neighbour, dirn, new_steps))

    raise ValueError("No solution found")


def solve_part1(data: str, max_straight=3):
    grid = HeatLossOptimizer._process_input(data)

    start = (0, 0)
    goal = (grid.shape[0] - 1, grid.shape[1] - 1)
    cost = get_path(grid, start, goal, max_straight=max_straight)

    return cost


if __name__ == "__main__":
    solve_part1(TEST_DATA)
    # test_solver = HeatLossOptimizer(TEST_DATA)
    # assert test_solver.solve_p1(view_path=True) == 102
    # parser = argparse.ArgumentParser(description=__doc__)
    # parser.add_argument("--input_path", help="Input filepath", type=str)
    # args = parser.parse_args()
    # input_path = args.input_path
    # with open(input_path) as f:
    #     text = f.read()
    # solver = HeatLossOptimizer(text)
    # assert solver.path_is_valid([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]) is False
    # assert solver.path_is_valid([(0, 0), (0, 1), (0, 2), (0, 3), (0, 2)]) is False
    # solver.solve_p1()  # should be in ]947, 1013[
