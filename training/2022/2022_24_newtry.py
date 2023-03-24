"A grid problem, involving blizzard moving"
import logging
from collections import deque
from queue import PriorityQueue

logging.basicConfig(level=logging.INFO)

INPUT_TEST = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

INPUT = """
#.########################################################################################################################
#>v^<>^^>.v<v^<>><>^v<>^.<v><>^<>^><><>v><^v>>><.<<<<^v.^<><^v>>^v^>v>.<^<^>^^^>^v>v><.v<v^>v<<.^^.<>vv<<.<>^^>vv^<<v>^v>#
#<<<v^>.><v^>.>^vv<<^^<><<<^^<v^<^<>^^.v..^<v^><^v.^<>vv<<.<<v>v^^v^^<v.<<^^>vv<>vvv^>^>.<<.vv<>^^><v>>v^^^<<^.^<>^.v><v<#
#>^v.>v<^^>^>v<<<<><>>vv<<>>v^>.<^v.>^>^^vv^<<v<^^vv><<v^<^v<^>>^.^v^^v^<<<^v>^<>^^^v.^>>>^^>>^<<.<<<<.><<><^.<.v.^v><vv<#
#<>>vvv^^v><<<vv.><.<>>><^<v.>v>v^v^>^^<>v><^>><v>^v<>>>v>^<<vvv^<v<^^<<v^>.^..<v<<<v>><vvvv<>.<^^.v^^<<<>><><>.vv><^>vv<#
#<v<v<vv>>><v<><<^>.><><v^^v>>vv><><v<v^v^<^^.>>>^>.^<<v^>>><^.<^<.><<vv^>^<vv>>^<>^v<^v^v^<>v<<^<.<><vv<.<v>^>v<^<v<^.v<#
#.^<v^>^v.^^><.vvv^^^>v<^v>.><v^>.>^^<^<^vv<<.<v<^<v^<<><<^vv^<<v<.>^.<<^v<>.<^<vv.>>v>>^v^>vvv<v<>v><>^^^v^>>.^vv<<.^v^>#
#.>^v^<>v<>>><<<^<^<v^<>.>^>v>v^^v<>^^v<>^<v^^^v.v^vvv^v<<v>v<>^^vv^v>><<.^>>v^^>^v>^v<<>.<^v<<^<<<.<<v^v<^v.v><>><<v<v<<#
#<><<<<><.^>v<^>><>^.>^^v^v^vvv><.v^<v<^vv^><<<^<>..>^^.v>^^^>>^>>><>vv>^.<<^^^^.vv>v.>v>v>>^v<<>><<v<<^>>^>^.<<v.>^v^<^<#
#<v^.^<><.^^>^<<<>^><>>^vv>>v.<^^..^^.v.><><>v<v<^<><>v^>>v>v<><v<v<<.>v^..^<>.>>>v>v^<><<v^v^>^>><<v^vvv>><.<>>^v.^.vvv>#
#>^.^v>.v^v<v>^v<>^v<<<^v^<<<><><>>.v^v>>^.v.v>><<<v>.>^>.><vv^vvv<vv>>>.<v^^>^vv..^v^.v>v>.>.<vv>>>><^^^>.^v>^<vv.v><<><#
#<^^<>>.<vv>.<^v^v^><^v>><vvv^^^<>>^v^>v^<.><v>^^v>^<.v><^<vv<^>>^^><v>^>v<>^<<><>><>v.^>vv^^<v.v>.>v>v<.>v><<<<.^^<<^^.>#
#<<>>^vv><<<<v<>^<^<^v.>v^<^.>>v^><><v.>>v^v<<<^vv^v><^v<^^>v<^v.>><v^^vv^>vv>^v^<.<>^>>vv><<v^vvv<v<v.v^<<^>^>>>vv<^^^><#
#<^><^>^^<<v^^>.>v^^><v<v<^vvv^>v><^v.^<^^<<v<^>v>^^v<.>^.vv<^v.>>v^.<^^>v>^>^^<^v^>..><>vv.v>>>vv.vv>>v<<<<^>>>v<^>v>>^<#
#.^>vv^vv<>v<<v.^^<.>><v><^v>^.^v><vv<<<^><v.<v<v<.>>>v^v<>>>>^v>^<<v<^<>v.vv.^vv^v><^^>vv><^v^v<<>>v<^v<v>.v^v<vv.^vvv^<#
#<v>>><>v>>v>>^vv<..^>.^>^^<v<><>><^<^><v<^<>^<<<^<..<v^v>^>^>>vvv><><^^>.>v<.^.^>v<<>v.><^.<>.<>^^v<>^^>^.>v.v>^>.v<^<v<#
#<v^vv>>v.><<>^^^v<>.>vv>^.v.^^^^^>^><^^.>><<>.<.<>^><<v>^^.vv.v><>>.v>vvv<v^<><>>vvv^.<<>><><>v>v>>>.^v>>v^v^><>>>>v<v.>#
#>^<vvvv^^v>v>^v^>.<v.v^v<>.v>^v.^.<<^>^<v^^.v.^.v<v>>^<<vv><>v^>vv^<^<>^v<v.v<v^>^^><v^^^^<>>v<^vv^^^<>><<>>.>>>^v<>^>v<#
#>^v>>><<vv.><v>><><^<.<v<^v<^<^^>vv^^^<^>v<v<v^>v<.<^..<.>.><^<<<>v>>.<>.>v.vv<<^^v^v>.v><>>^^>^<^^.^.^>^v.><v>>v<v>vv^<#
#>>^<^vv<>^^^><v<v><>.^><v^>>>><<<>>^>^.<.^^<^.^.^>>>^^<^>>v.v<<v^><^^<^^>vv<><>v>>><^vv.><.<>><vv<^>>>^<^>^vvvvv.vv^v.>>#
#<<v.^>v^<>><v^<>.vv^v^><>><v>><<<>><^^v^<^.<<><^<<vv<.>^>v><^v>v^v><^<>v^^<v>v>v^<^>v>^.<v^><<v<v.v<><^^v><<.>v><v<v<<>>#
#>v^<><<^>v^.^^.v^>>v>^v<<<<>vv^v.>^v.>>^vvv^><<v><^<>v.v<vv>^<..>>^^>^v>^>^^<^<v^<vv^<vvv.v<>><>^<^^>^<^^<.^vvv.^.<<<<^<#
#>.v<vv<v^^<v^^<<.^^v><>^>>>^.v^>^<>^.<<><<^v>^><vv<<>>^v<>v>>.^>>^>.vv<>^<><.<vv<v^..v.><v>^^.vv^.^^<v>><vv>^v>.^>^v><v>#
#<v^<>^^^^<<^^>v.><>^>v.>>^^<>v<><.^.v..>>^v^v>^^>.^v>><v>.^v^<v<><v>v>v<v.v><<<>v>.<>>^<^vv>^v>>vv>^v>vv><<>^^<^<^vv>.^>#
#<^<<><>vv<^^v.^<<^.v<v<v^.>^>^^vv^^v^>^^vv>^>^v^^.vvvv<vv>^>^v^><.>^>><v^v<<.v.v<>v><>^.^^<>>v>v.^<<.<v.>.vvv><<<<v..><.#
#<<<>^^^>^^.v.^><<vv.><><v>>v<>^^v<>^v.<^^^^^<v>>>v>^v>vv^^>^.v>>^^^.><v<v^vvvvvv^^.<>v>>>>v>>^^v<^.>>v.>v><v.v.vv^^^v>^<#
########################################################################################################################.#
"""


class BlizzardProblem:
    "Simulates the blizzard motion"

    def __init__(self, input_) -> None:
        self.input_ = input_
        self.process_input()
        self.start_square = min(loc for loc, val in self.grid.items() if not val)
        self.end_square = max(loc for loc, val in self.grid.items() if not val)
        logging.info(
            f"Start square is {self.start_square}, end square is {self.end_square}"
        )
        self.get_blizzard_states()
        self.get_dist_to_target()  # heuristic (taxicab distance) used to speed up the queue

    def process_input(self) -> None:
        rows = [row for row in self.input_.splitlines() if row.strip()]
        self.nb_rows, self.nb_cols = len(rows), len(rows[0])
        self.grid = {}
        for ind, row in enumerate(rows):
            for col_nb in range(self.nb_cols):
                self.grid[(ind, col_nb)] = [val] if (val := row[col_nb]) != "." else []
        logging.info("Processed the grid")

    def get_blizzard_states(self) -> None:
        """Blizzard states will eventually repeat, so instead of
        always recomputing them, let's store the possible states"""
        i = 0
        self.blizzard_states = {i: self.grid}
        temp = self.grid
        while True:
            new_grid = {loc: [] if val != ["#"] else val for loc, val in temp.items()}
            for loc, contents in temp.items():
                if contents in (["#"], []):
                    continue
                for arrow in contents:
                    x, y = loc
                    if arrow == "<":
                        neigh = (x, self.nb_cols - 2 if y - 1 == 0 else y - 1)
                    elif arrow == ">":
                        neigh = (x, 1 if y + 1 == self.nb_cols - 1 else y + 1)
                    elif arrow == "^":
                        neigh = (
                            self.nb_rows - 2
                            if x - 1 == 0 and y != self.start_square[1]
                            else x - 1,
                            y,
                        )
                    else:
                        neigh = (
                            1
                            if x + 1 == self.nb_rows - 1 and y != self.end_square[1]
                            else x + 1,
                            y,
                        )
                    new_grid[neigh].append(arrow)
            if new_grid in self.blizzard_states.values():
                break
            i += 1
            self.blizzard_states[i] = new_grid
            temp = new_grid
        self.nb_blizzard_states = i + 1
        logging.info(f"There are {self.nb_blizzard_states} blizzard states")

    def traverse_fifo(self) -> int:
        queue: deque = deque()
        seen = set()
        queue.append(
            (self.start_square, 0, 0)
        )  # current location, current distance, current blizzard state index
        while queue:
            curr_pos, nb_minutes, blizzard_ind = queue.popleft()
            if curr_pos == self.end_square:
                logging.info(f"Part 1: {nb_minutes}")
                break
            if (
                immutable_grid := map(
                    frozenset, self.blizzard_states[blizzard_ind].values()
                )
                in seen
            ):
                continue
            seen.add(immutable_grid)
            # append legal neighbour states to the queue
            x, y = curr_pos
            new_blizzard_ind = (blizzard_ind + 1) % self.nb_blizzard_states
            queue.extend(
                (neigh, nb_minutes + 1, new_blizzard_ind)
                for neigh in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x, y))
                if self.blizzard_states[new_blizzard_ind].get(neigh) == []
            )
        else:
            raise Exception("Unreachable")
        return nb_minutes

    def get_dist_to_target(self):
        self.dist_to_target = {
            loc: abs(loc[0] - self.end_square[0]) + abs(loc[1] - self.end_square[1])
            for loc in self.grid
        }

    def traverse_pqueue(self) -> int:
        """BFS is too slow, so let us the taxicab disatnce as heuristic and
        speed up the search by popping out the states closest where the expedition is
        closest to the destination square"""
        queue: PriorityQueue = PriorityQueue()
        # seen = set()
        queue.put(
            (self.dist_to_target[self.start_square], self.start_square, 0, 0)
        )  # distance to target (heuristic), current location, current nb of minutes, current blizzard state index
        while not queue.empty():
            _, curr_pos, nb_minutes, blizzard_ind = queue.get()
            if curr_pos == self.end_square:
                logging.info(f"Part 1: {nb_minutes}")
                break
            # if (
            #     immutable_grid := map(
            #         frozenset, self.blizzard_states[blizzard_ind].values()
            #     )
            #     in seen
            # ):
            #     pass#continue
            # seen.add(immutable_grid)
            # append legal neighbour states to the queue
            x, y = curr_pos
            new_blizzard_ind = (blizzard_ind + 1) % self.nb_blizzard_states
            for neigh in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x, y)):
                if self.blizzard_states[new_blizzard_ind].get(neigh) == []:
                    queue.put(
                        (
                            self.dist_to_target[neigh],
                            neigh,
                            nb_minutes + 1,
                            new_blizzard_ind,
                        )
                    )
        else:
            raise Exception("Unreachable")
        return nb_minutes

    def print_grid(self) -> None:
        "Used for debugging"
        printed_grid = [["#" for _ in range(self.nb_cols)] for _ in range(self.nb_rows)]
        for (x, y), arrows in self.grid.items():
            printed_grid[x][y] = (
                arrows[0] if len(arrows) == 1 else ("." if not arrows else len(arrows))
            )
        for row in printed_grid:
            print(*row)
        print("\n")


# part 2

if __name__ == "__main__":
    test = BlizzardProblem(INPUT_TEST)
    # for _ in range(2):
    #     t.move_blizzard(); t.print_grid()
    assert test.traverse_pqueue() == 18
    actual = BlizzardProblem(INPUT)
    actual.traverse_pqueue()
    # def find_neighbour_cells(self) -> None:
    #     self.neighbors = defaultdict(set)
    #     for (x, y) in self.grid:
    #         for neigh in (
    #             (
    #                 1
    #                 if x + 1 == self.nb_rows - 1 and y != self.end_square[1]
    #                 else x + 1,
    #                 y,
    #             ),
    #             (
    #                 self.nb_rows - 2
    #                 if x - 1 == 0 and y != self.start_square[1]
    #                 else x - 1,
    #                 y,
    #             ),
    #             (x, 1 if y + 1 == self.nb_cols - 1 else y + 1),
    #             (x, self.nb_cols - 2 if y - 1 == 0 else y - 1),
    #         ):
    #             if neigh in self.grid:
    #                 self.neighbors[(x, y)].add(neigh)
    #     logging.info(f"Neighbours are {self.neighbors}")
