"This challenge reminds me of 2016 day 24, with more constraints though"
from string import ascii_lowercase, ascii_uppercase
from itertools import combinations
from copy import deepcopy
import numpy as np
import networkx as nx


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

# INPUT = """
# ########################
# #f.D.E.e.C.b.A.@.a.B.c.#
# ######################.#
# #d.....................#
# ########################""" # shortest = 86 SOLVED

# INPUT = '''
# ########################
# #...............b.C.D.f#
# #.######################
# #.....@.a.B.c.d.A.e.F.g#
# ########################''' # shortest = 132 SOLVED

# INPUT = '''
# ########################
# #@..............ac.GI.b#
# ###d#e#f################
# ###A#B#C################
# ###g#h#i################
# ########################''' # shortest = 81 SOLVED

# INPUT = """
# #################
# #i.G..c...e..H.p#
# ########.########
# #j.A..b...f..D.o#
# ########@########
# #k.E..a...g..B.n#
# ########.########
# #l.F..d...h..C.m#
# #################"""  # shortest paths = 136 # SOLVED but pretty slowly


class Maze:
    """Represents the grid and tracks its state after each door gets unlocked"""

    def __init__(self, str_input: str) -> None:
        self.str_input = str_input
        self.current_path = []
        self.reachable_keys = set()
        self.reached_keys = set()
        self.shortest_path_length = float("inf")
        self.drop_uppercase_mapping = str.maketrans(
            ascii_uppercase, "." * len(ascii_uppercase)
        )
        self._build_graph()
        if self.doors:
            self.get_shortest_paths()

    def _build_graph(self) -> None:
        """Builds the initial maze"""
        self.grid = np.array(
            [
                stripped
                for row in self.str_input.splitlines()
                if (stripped := list(row.strip()))
            ]
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
                elif current_type in ascii_lowercase:
                    self.keys_[current_type] = current_pos
                elif current_type in ascii_uppercase:
                    self.doors[current_type] = current_pos
                if current_type in self.walls_doors:
                    continue
                if current_type in "." + ascii_lowercase:
                    self.graph.add_node(
                        current_pos
                    )  # abit redundant with the below block but necessary for . surrounded by doors
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
        self.current_pos = self.start_pos
        self.key_door_locations = {
            self.keys_[k]: self.doors[door]
            for k in self.keys_
            if (door := k.upper())
            in self.doors  # the if is because some keys don't have doors
        }

    def open_door(self, door: tuple[int, int]) -> None:
        """Opens a door by creating the appropriate edges in the graph

        Args:
            door (tuple[int, int]): the location of the door to open
        """
        door_row, door_col = door
        current_nodes = deepcopy(self.graph.nodes)
        for node_row, node_col in current_nodes:
            if (
                abs(node_row - door_row) + abs(node_col - door_col) == 1
            ):  # neighbour node
                self.graph.add_edge(
                    (node_row, node_col), door
                )  # link the opened door to its neighbouring nodes
                # print(f'opened {door}')

    def update_reachable_keys(self) -> None:
        """scans the grid to find potential new keys within reach"""
        for k in self.all_keys_coords.difference(
            self.reachable_keys.union(self.reached_keys)
        ):
            if nx.has_path(self.graph, self.current_pos, k):
                self.reachable_keys.add(k)

    def get_shortest_paths(self) -> None:
        """compute the shortest path length for all couples of key locations, regardless of locked doors, for later lookup"""
        maze_no_doors = Maze(self.str_input.translate(self.drop_uppercase_mapping))
        self.shortest_paths = {}
        for start, end in combinations(
            list(self.all_keys_coords) + [self.start_pos], 2
        ):
            self.shortest_paths[(start, end)] = (
                sp := nx.shortest_path(maze_no_doors.graph, start, end)
            )[
                1:
            ]  # do not count the start pos as a move
            self.shortest_paths[(end, start)] = sp[::-1][
                1:
            ]  # do not count the start pos as a move

    def reach_key(self, key_: tuple[int, int]) -> None:
        """Collects a given key and make the necessary updates (path, current position etc.)

        Args:
            key_ (tuple[int, int]): the location of the key to collect
        """
        self.current_path.extend(
            (latest_walk := self.shortest_paths[(self.current_pos, key_)])
        )  # register the path made towards the key
        self.current_pos = key_  # update current position
        # maybe I've collected other keys on my way
        for key_ in self.all_keys_coords.intersection(set(latest_walk)):
            self.reached_keys.add(key_)  # collect key
            # print(f'just got {key_}')
            self.reachable_keys.discard(key_)  # drop key from target keys
            if key_ in self.key_door_locations:
                self.open_door(self.key_door_locations[key_])


shortest_path_length = float("inf")
all_situations = (
    {}
)  # will store all the (current_pos, self.reached_keys) couples as keys,
# path_length as values, to avoid duplicated calcs


def solve(maze: Maze) -> None:
    """Recursively explores all possible ways to collect the keys


    Args:
        maze (Maze): a maze object
    """
    global shortest_path_length
    if (
        lcp := len(maze.current_path)
    ) >= shortest_path_length:  # not worth continuing this path
        return
    if len(maze.reached_keys) == maze.nb_keys:  # base case
        if lcp < shortest_path_length:
            shortest_path_length = lcp
            print(shortest_path_length)
        return
    maze.update_reachable_keys()  # explore possibilities
    # assert maze.reachable_keys
    for k in maze.reachable_keys:
        # this is the cross-roads where I need copies (not new instances) of Mazes
        # assert k != maze.current_pos
        new_maze = deepcopy(maze)
        new_maze.reach_key(k)
        lncp = len(new_maze.current_path)
        if (
            all_situations.get(
                (
                    situation := (
                        new_maze.current_pos,
                        tuple(sorted(new_maze.reached_keys)),
                    )
                ),
                float("inf"),
            )
            <= lncp
        ):
            return  # not worth continuing this path
        all_situations[situation] = lncp
        solve(new_maze)


maze = Maze(INPUT)
solve(maze)
print("part 1:", shortest_path_length)
# part 2
