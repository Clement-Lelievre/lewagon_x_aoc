"This challenge reminds me of 2016 day 24, with more constraints though"
import numpy as np
import networkx as nx
from string import ascii_lowercase, ascii_uppercase
from itertools import combinations

INPUT = """#################################################################################
#.......#.......#.......O...#.D.........#.......#.......#.....U...#...#.......#.#
#.#####.#.#######.#####.#.###.#########.#####.#.#.###.###.#.###.###.#.#.###.#.#.#
#...#.#.#............j#.#.#...#.....#b..#.....#.#.#.#.#...#.#...#...#...#...#...#
#.#.#.#.#.###########.#.#.#.###.#.###.###.#######.#.#.#.###.#####.#######.#####.#
#v#.#.#.#.#.#...#.....#.#.#.#...#.#...#.#...#.....#.#...#.#...#...#.......#.....#
#.#.#.#.#.#.#.#.#######.#.#.#.#####.###.#.#.#.#####.#####.###.#.###.###########.#
#.#.#r#.#...#.#...#.....#.#.#.#.....#...#.#...#.......#.....#.....#.....A.....#.#
###.#.#.###.#.###.#.#####.#.#.#.#######.#.#####.#####.#.#########.#########.#.#.#
#...#...#...#.#.....#.....#...#.#.....#.#.#.....#.....#...#...#.....#.....#.#.#.#
#.###.###.###.#.#######.###.###.###.#.#.#.#.#####.#######.#.#.#######.###.###.###
#.#.....#.#...#.#.....#.#...#...#...#.N.#.#.#...#.......#.#.#...#...#s..#...#...#
#.#####.###.#####.###.###.###.###.#######.#.#.#.#######.#.#C###.#.#.###.###.###.#
#...#.......#.....#.#.......#.#...#.....#.#...#.#.#.....#.#...#..c#...#.#...X.#.#
#.#.#.#######.#####.#########.#.###.###.#.#####.#.#.#####.###.#######Y#.#####.#.#
#.#.#.#...#...#.....#.........#.......#.#.......#...#.......#g......#.#.....#...#
#.#.###.#.#.#######.#.#########.#######.#########.###.#.###########.#.#####.###.#
#.#.....#.#.......#.#.#.......#...#.....#.#.......#...#...........#.#.......#...#
#######.#.#######.#.#.###.###.#####.###.#.#.#######.#############.#.#########.###
#.....#.#.......#...#...#...#...#...#...#.#.....#...#.....#.......#...#.....#.#.#
#.###.###.#####.###.###.#.#.###.#.###.###.#####.#.#######.#Q#######.#.###.###.#.#
#.#...#...#...#.#...#...#.#...#...#.#...#.#.....#.........#.#...P.#.#.G.#.....#.#
#.###.#.###.###.#.#########.#.#####.###.#.#.###############.#####.#.###.#.#####.#
#...#...#...#...#.........#.#.#.....#...#.#.#.......#.........#...#...#.#.....#.#
###.#####.###.###########.###.###.###.###.#.#.###.#.#.#####.###.#####.#.#####.#.#
#...#...#...#.#.......#.#...#...#.......#...#...#.#.#...#...#...#.....#i..#.#...#
#.###.###.#.#.#####.#.#.###.###.#######.#.#######.#.###.#.###.#########.#.#.###.#
#.#...#...#.#...#...#.....#...#.....#...#.#.......#.....#.#p..#.......#.#.#.#...#
#.#.#.#.###.###.#.#.#####.###.#####.#####.###.#########.###.###.#####.###.#.#.###
#.#.#...#.#...#.#.#.#...#...#.....#.....#...#.#...#.....#...#...#.#..l#...#.....#
#.###.###.###.#.#.###.#.###.#####.#####.###.#.#.#.#######.###L###.#.###.#########
#...#.#.....#...#.....#.#.#...#..e#.....#...#...#.....#.Z.#...#..t#.T.#......w..#
###.#.#.###.###########.#.###.#.###.#####.###.#######.#.###.###.#.###.#.#######.#
#...#.#.#.#.........#...#...#.#.#....h..#.#...#.......#.#...#.F.#...#.#.I.....#.#
#.###.#.#.#.#######.#.###.###.#.#.#####.#.#####.#####.#.#.###.#####.#.#.#######.#
#.#.....#...#.....#.#.#.......#.#.#...#.#.......#.#...#..z#.#.....#...#.#..k..#.#
#.#########.#.###.#.#.#########.#.#.#.#.#########.#.#######.#####.#######.###.#.#
#...M.#...#.#.#.#.#...#.....#...#.#.#...#...#.....#.#.........#...#.......#.#.#.#
#.###.#.#.###.#.#.#####.###.#.#####.###.#.#.#.#.###.###.#####.#.###.#######.#W#.#
#...#...#.......#.........#.........#.....#...#.........#.....#fK...#...........#
#######################################.@.#######################################
#.......#.........#...................#.......#.........#...........#...........#
#.###.###.#.#######.#####.#.#########.#.#.###.#.#####.#.#.#########.#.#######.#.#
#.#...#...#.........#...#.#.#.......#...#...#.#.#...#.#.#.#.#.....#.#.......#.#.#
#.#.###.#############.#.###.#.#####.###.###.###.#.#.#.###.#.#.#.###.#####.###.#.#
#.#...#.#.........#...#...#.#.....#...#.#...#...#.#.#.....#...#...#...#...#...#.#
#.#####.#########.#.#####.#.#####.#.###.#.#.#.#####.#############.###.#.###.###.#
#.......#...#...#.#.....#.#...#...#.#...#.#.#...#.........#.....#.#...#...#...#.#
#.#######.#.#.#.#.#####.#.#.#.#.###.#.###.#.###.#.#######.#.###.#.#.#####.###.###
#...#.....#...#.....#...#.#.#.#.#...#...#.#.#.#.#...#.....#...#...#.#.......#...#
###.#.#.#########.###.###.###.#.#.#####.#.#.#.#.###.#####.###.#####.#.#########.#
#.#.#.#.#.....#...#...#.#.....#.#...#...#.#...#...#..m..#...#.....#.#.....#...#.#
#.#.###.#.###.#####.###.#######.#####.###.#######.#####.###.#####.#.#.#####.#.#.#
#.#..q..#.#.#.#.....#...............#...#.......#.....#...#.#.....#.#.#...#.#...#
#.#.#####.#.#.#.###.#######.#######.###.#.#####.#####.#.#.#.#.###.#.#.#.#.#.###.#
#...#.....#.....#...#.....#.#.....#.....#...#.#.H.#...#.#.#...#...#.#.#.#...#.#.#
#.###.#.#########.###.###.###.###.#########.#.###.#.#####.#####.###.#.#.#####.#.#
#.#.#.#.#...#...#...#.#.......#.#.#.....#.#.#...#.........#.....#...#.#.#.....#.#
#.#.#.###.#.#.#.###.#.#########.#.#.###.#.#.#.###################.###.#.###.#.#.#
#...#.....#...#.#.#.#...#.......#...#.#.#.#.#.......#.....#.....#.#...#...#.#.#.#
###.###########.#.#.###.#.#####.#####.#.#.#.#######.#.###.#.###.#.#######.###.#.#
#...#.........#.#...#...#.#...#.......#.#...#.....#.#.#.#...#...#.....#...#...#.#
#.###.#######.#.###########.#.#.#.###.#.#.###.###.#.#.#.#############.#.###.#.#.#
#.#...#.#.......#.........#.#.#.#.#...#.#.#.....#...#...#.........#...#...#.#.#.#
#.#.###.#.#####.#.###.###.#.#.###.#####.#.#####.#######.#.###.###.#.###.#.#.###.#
#.#.#.#...#...#.#.#.#.#.....#...#.#.....#.......#.......#...#.#...#...#.#.#.....#
###.#.#.###.#.###.#.#.#########.#.#.###########.#.###########.#.#####.#.#.#####.#
#...#...#...#.....#.#.........#...#.#...#.....#.#.....#.......#.#.....#.#.....#.#
#.###.###.#########.#########.#####.###.#####.#.#####.###.#####.#.#####.#####R#J#
#.#.#...#.#.......#.....#...#o......#...#.....#.E...#.....#...#...#.....#.#...#.#
#.#.#.###.#.###.#.#.###.###.#########.###.#########.#########.#########.#.#.#####
#.#...#...#...#.#.#...#...........#.....#.#.......#...#.....#.........#.#.#.....#
#.#####.#####.#.#.#.#.###########.#.###.#.#.#.#.#####.#.###.#.#.#####.#.#.#####.#
#.#.....#.....#.#.#.#.#......a....#...#.#...#.#.#...#.#...#.#.#...#...#.....#...#
#.#.###########.#.###.#.###############.#.###.#.#.#.#.###.#.#####.###.#######.#.#
#...#u......#...#.....#...#.......#...#.#...#.#.#.#.#.#...#.#...#...#.B...#...#.#
#.#######.#.#.###########.#.#####.#.#.#.###.#.###.#.#.#.###.#.#.###.#####.#.###.#
#.#.....#.#.#...#...#...#x#...#.#.#.#...#.#.#.....#.#.#.#.#.#.#...#..d#...#.V.#.#
#.###.#.#.#.###.#.#.#.#.#.###.#.#.#S###.#.#.#######.#.#.#.#.#.###.###.#.#####.#.#
#.....#...#.....#.#...#.......#.....#..y#.........#.....#n....#.......#.......#.#
#################################################################################
"""

INPUT = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""


class Maze:
    """Represents the grid and tracks its state after each door gets unlocked"""

    def __init__(self, str_input: str) -> None:
        self.str_input = str_input
        self.build_graph()

    def build_graph(self) -> None:
        """Builds the initial maze"""
        self.grid = np.array(
            [rs for row in self.str_input.splitlines() if (rs := list(row.strip()))]
        )
        self.graph = nx.Graph()  # undirected, unweighted
        self.walls_doors = "#" + ascii_uppercase
        self.nb_rows, self.nb_cols = self.grid.shape
        self.keys_ = {}
        self.doors = {}
        for row_ind in range(1, self.nb_rows - 1):
            for col_ind in range(1, self.nb_cols - 1):
                current_pos = (row_ind, col_ind)
                current_type: str = self.grid[current_pos]
                if current_type == "@":
                    self.start_pos = current_pos
                if current_type in ascii_lowercase:
                    self.keys_[current_type] = current_pos
                if current_type in ascii_uppercase:
                    self.doors[current_type] = current_pos
                if current_type in self.walls_doors:
                    continue
                if self.grid[row_ind, col_ind - 1] not in self.walls_doors:
                    self.graph.add_edge(current_pos, (row_ind, col_ind - 1))
                if self.grid[row_ind, col_ind + 1] not in self.walls_doors:
                    self.graph.add_edge(current_pos, (row_ind, col_ind + 1))
                if self.grid[row_ind - 1, col_ind] not in self.walls_doors:
                    self.graph.add_edge(current_pos, (row_ind - 1, col_ind))
                if self.grid[row_ind + 1, col_ind] not in self.walls_doors:
                    self.graph.add_edge(current_pos, (row_ind + 1, col_ind))
        self.all_keys_coords = set(self.keys_.values())
        self.nb_keys = len(self.all_keys_coords)
        self.reachable_keys = set()
        self.reached_keys = set()
        self.current_pos = self.start_pos
        self.key_door_locations = {
            self.keys_[k]: self.doors[door]
            for k in self.keys_
            if (door := k.upper())
            in self.doors  # the if is because some keys don't have doors
        }

    def open_door(self, door: tuple[int, int]) -> None:
        door_row, door_col = door
        for node_row, node_col in self.graph.nodes:
            if (
                abs(node_row - door_row) + abs(node_col - door_col) == 1
            ):  # neighbour node
                self.graph.add_edge(
                    (node_row, node_col), door
                )  # link the opened door to its neighbouring nodes

    def update_reachable_keys(self) -> None:
        for k in self.all_keys_coords.difference(
            self.reachable_keys.difference(self.reached_keys)
        ):
            if nx.has_path(self.graph, self.current_pos, k):
                self.reachable_keys.add(k)


# define a global variable shared across all recursive traversal functions, that'll get updated with the min path length
shortest_path_length = float("inf")


maze = Maze(INPUT)
maze.build_graph()


current_pos = maze.start_pos
current_path = []

# compute the shortest path length for all couples of key locations regardless of locked doors, for later lookup
NO_CONSTRAINTS_GRAPH = nx.Graph()  # undirected, unweighted
for row_ind in range(1, maze.nb_rows - 1):
    for col_ind in range(1, maze.nb_cols - 1):
        current_pos = (row_ind, col_ind)
        current_type: str = maze.grid[current_pos]
        if current_type == "#":
            continue
        if maze.grid[row_ind, col_ind - 1] != "#":
            NO_CONSTRAINTS_GRAPH.add_edge(current_pos, (row_ind, col_ind - 1))
        if maze.grid[row_ind, col_ind + 1] != "#":
            NO_CONSTRAINTS_GRAPH.add_edge(current_pos, (row_ind, col_ind + 1))
        if maze.grid[row_ind - 1, col_ind] != "#":
            NO_CONSTRAINTS_GRAPH.add_edge(current_pos, (row_ind - 1, col_ind))
        if maze.grid[row_ind + 1, col_ind] != "#":
            NO_CONSTRAINTS_GRAPH.add_edge(current_pos, (row_ind + 1, col_ind))

shortest_paths = {}
for start, end in combinations(maze.all_keys_coords, 2):
    shortest_paths[(start, end)] = (
        sp := nx.shortest_path(NO_CONSTRAINTS_GRAPH, start, end)
    )[
        1:
    ]  # do not count the start pos as a move
    shortest_paths[(end, start)] = sp[::-1][1:]

maze.shortest_paths = shortest_paths  # create an attribute to store the shortest paths between all key locations

print(dir(maze))
# main function
# def solve(
#     G: nx.Graph,
#     current_pos: tuple[int, int],
#     reached_keys: set,
#     reachable_keys: set,
#     current_path: list,
# ):
#     global shortest_path_length
#     if (
#         lcp := len(current_path)
#     ) >= shortest_path_length:  # not worth continuing this path
#         return
#     if len(reached_keys) == nb_keys:  # base case
#         if lcp < shortest_path_length:
#             shortest_path_length = lcp
#         return
#     reachable_keys = update_reachable_keys(
#         G, current_pos, reachable_keys
#     )  # explore possibilities
#     for k in reachable_keys:
#         your_graph = Maze(G)
#         your_graph.open_door(k)
#         solve(
#             your_graph,
#             k,
#         )


print("part 1:", shortest_path_length)
# part 2
