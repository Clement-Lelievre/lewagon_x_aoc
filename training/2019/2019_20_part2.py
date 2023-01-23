"""2019 day 20: path finding, recursion, Breadth-First Search, using a queue,
some Numpy manipulation etc."""
from collections import defaultdict, deque
from string import ascii_uppercase
import numpy as np

# the 2 provided examples this time no longer have a solution, so Eric Wastl
# provides a new one

INPUT = """
                                   G           R   U       E         Z S       S                                       
                                   W           N   C       K         Z G       D                                       
  #################################.###########.###.#######.#########.#.#######.#####################################  
  #.#.......#.#.........#.#.#.....#.#.....#.#.#...#.....#.........#.....#...#.#...........#.......#.....#.....#.#...#  
  #.#####.###.###.###.#.#.#.###.###.#.###.#.#.###.#.###.###.#####.#.###.###.#.###.#########.###.###.#######.###.#.###  
  #.#.#.#...#...#.#.#.#.................#.#...#...#.#.#...#.#.....#.#.#.#.....................#.#.......#.........#.#  
  #.#.#.#.###.#####.#########.###########.#.#.#.###.#.#######.###.#.#.#####.###.#.###.#.###.#.###.#######.#######.#.#  
  #...#...#.#.#.#.........#...#...#.......#.#...#.......#.....#.#.#.....#.....#.#...#.#.#...#.#...#.#.........#.#.#.#  
  #.#.###.#.#.#.#####.#.#.#######.#.#######.###.#.###.#####.###.#####.#.###.#########.#.#.#######.#.#####.#####.#.#.#  
  #.#...#.#.#.#.#.....#.#.................#.#...#.#.#.....#...#.#.#...#...#.#.....#.#.#.#...#.#.#...........#.#.....#  
  ###.###.#.#.#.#.#.#####.#.###.#########.#.#######.#.#####.###.#.#.#.#####.#.#.###.#.#######.#.#.###.#######.###.#.#  
  #...#.......#...#.#.#.#.#...#.#.........#.....#.......#.#.......#.#...#.....#.....#.#...#.........#...#.#.#.#.#.#.#  
  ###.#######.#######.#.###########.#.#####.###.#####.###.#.#####.#.###.#.#.###.#.#######.###.#####.#####.#.#.#.#####  
  #.......#.#...#.......#.........#.#.#...#.#.#.#.....#.....#...#.#...#.#.#.#...#...#...#...#...#.#.#...........#.#.#  
  #.#.###.#.#.#########.#########.#.###.###.#.#####.#.###.#.#.#.#.#.###########.#.###.###.###.###.###.###.#.#####.#.#  
  #.#...#.....#.#...#.#.#.#.#.............#.....#...#...#.#.#.#...#...#.#.#.....#.........#...#.......#...#...#...#.#  
  ###########.#.#.###.#.#.#.#######.#####.#.#####.#.#######.#####.###.#.#.#####.#.#.###.#####.###.#############.#.#.#  
  #.#.#.#.#.....#.#.....#.#.#.#.....#...#.#.....#.#.....#...#.#.#...#...#.#.#...#.#...#...#...#...#...#.#.......#.#.#  
  #.#.#.#.###.###.#####.#.#.#.#####.#.###.#.#########.#######.#.#.###.###.#.#.###.###.#####.#####.#.###.#####.#####.#  
  #.#...#.#...#.#.#...#...#.#.....#.#.....#.#...#.....#.......#.#.#...#.....#.#.#.#.......#.......#...#.#.#...#.#...#  
  #.#.#.#.###.#.#.###.#.###.#.#####.#.###.#.###.###.###.#.#.###.#.#.###.#.#.###.#.###.#####.#.#####.###.#.###.#.###.#  
  #.#.#.#.#...#.#...#...#.#.#...#...#...#.#.#.....#.#...#.#.#.....#.#...#.#.#.......#.......#...#.#.....#.........#.#  
  #.#.###.###.#.#.#####.#.#.#.###.#.#####.#.#.###.#.###.#.###.#.###.#.###.#####.#####.#####.#####.###.#########.#.#.#  
  #.....#...#.......#.#.#.......#.#.#...#.#...#.#.#.....#...#.#...#...#.#...#.......#...#.#...#...#...#.#.#.#.#.#.#.#  
  ###.###.#######.###.#.#.#.#.#########.#.#####.#.#.#####.#######.#####.#.#####.#.#.###.#.#######.###.#.#.#.#.#.###.#  
  #.....#...#.#.#.......#.#.#.#.#.......#...#.....#.#.....#.......#.......#.#...#.#.#.#...#.....#.#.....#.#.#...#.#.#  
  ###.###.###.#.#######.#.#####.#####.#.#.###.#########.#.###.#.#####.#####.###.#####.#######.###.###.###.#.#.###.#.#  
  #.....#.......#...#...#...#.#.#.#.#.#.#.#.......#.#...#.#.#.#...#.......#...#.......#...#.....#...#.#.........#...#  
  #.#####.#######.###.#.#.###.#.#.#.#.#.#.###.#.###.#.#####.#####.#####.#####.###.#######.###.###.###.#########.#.###  
  #...#...#...#.#.#...#.#.#.#.........#.....#.#.....#.......#.......#...#.............#...#...#.#.........#...#.#...#  
  #.###.###.###.#.#####.#.#.#.#####.#############.#######.#####.#####.#######.###########.###.#.###.#######.###.#.###  
  #...#...#...#...#.#...#...#.#    S             L       B     V     G       R          #.#.#.#.....#.#.......#.#...#  
  #.###.#.#.#####.#.###.#.###.#    D             M       E     H     X       Q          #.#.#.#####.#.###.#####.#.###  
  #.....#.#.................#.#                                                         #.........................#.#  
  #.###.###.#####.#.#.#.###.###                                                         #.#.#.###.#######.###.#.#.#.#  
  #.#.#.....#.#...#.#.#.#.....#                                                       RZ..#.#...#.....#.#...#.#.#.#..BE
  #.#.#####.#.#####.#.#####.###                                                         #######.#####.#.#.#######.#.#  
  #.....#.#.....#.#.#.....#.#.#                                                         #.#.#.#.#.#...#.......#...#.#  
  ###.###.###.#.#.#.#.###.#.#.#                                                         #.#.#.###.#####.#.#######.#.#  
RI....#.....#.#.#...#.#.#.#....UW                                                       #.#.......#...#.#.#.#...#...#  
  #####.###############.###.###                                                         #.###.#####.#.#####.#.#.#####  
  #.....#.#.#...#.#.....#.#...#                                                       GW..........#.#.........#.#...#  
  #.###.#.#.#.###.###.###.#####                                                         #.###.#.#.###.#######.###.###  
  #...#...#.....#.#.......#....FM                                                       #.#...#.#.....#...#.........#  
  ###.###.#.#.#.#.#.#########.#                                                         ###.#######.###.###########.#  
AJ..#...#...#.#...#...#.....#.#                                                         #...#.#.#...#...#.#...#.#.#..GX
  #.#.#########.#.#.#######.#.#                                                         #####.#.#######.#.###.#.#.###  
  #.....#.#.#.#.#.............#                                                         #...............#...#........DD
  #######.#.#.###########.###.#                                                         ###.#######.###.#.#.#.#.###.#  
  #.....................#.#...#                                                         #.......#.....#...#.#.#.#...#  
  ###.###.#.#.###.#####.#######                                                         #####.#########.###.#.###.###  
GP..#...#.#.#.#.....#.#...#...#                                                       SG..#...#.....#...#.#.....#...#  
  #.###.#####.#.#.#.#.###.###.#                                                         #.#.###.#.#######.#######.###  
  #.#.....#.#.#.#.#.#.....#...#                                                         #.....#.#.#.#...#.#.#...#.#.#  
  #.#.#####.#########.#######.#                                                         #########.#.###.#.#.#.#####.#  
  #.....#...#..................SI                                                     DD....#........................UW
  #.#######.#####.###.###.#####                                                         #.###.#####.#.###.#.###.#####  
  #.#.#...#...#.....#.#.#.#.#..AJ                                                       #.........#.#.#.#.#.#.....#.#  
  ###.#.###.#.#########.###.#.#                                                         #.#####.###.#.#.#######.###.#  
  #.........#.#...#.....#.#.#.#                                                         #...#.....#.#...#.#.#.#.#....LM
  #########.#.###.#.###.#.#.#.#                                                         #########.#.#.###.#.#.#####.#  
AA......#.#.#.....#.#...#.....#                                                         #.#.#.#.#.#.#.#...#.#.#.....#  
  #.#####.#.#.###.#.#.###.#.###                                                         #.#.#.#.#########.#.#.#####.#  
JO..........#...#...#.....#...#                                                         #.#.......#.#.............#.#  
  #####.###############.###.#.#                                                         #.#.#.#####.###.###.#.###.#.#  
  #.#.#...#.........#.#.#.#.#.#                                                       TX....#.............#.#...#...#  
  #.#.#######.#.#.#.#.###.###.#                                                         #.###.#.###.#####.###########  
VH......#.....#.#.#.....#...#.#                                                         #.#...#.#...#...#.#.....#...#  
  #####.#.###########.###.#####                                                         #############.#####.###.#.#.#  
  #.....#.....#.#.......#.....#                                                         #.#...#...#.#.......#.#.#.#..RZ
  #.#.#######.#.#######.#.#####                                                         #.###.###.#.###.#.###.#.#.###  
  #.#...........#.#............FW                                                     RN..#.....#...#.#.#.#.....#...#  
  #########.###.#.#.###########                                                         #.#.#.###.###.###.#.#####.###  
  #...#...#.#.....#.#.........#                                                         #...#.............#.......#.#  
  #.#.#.#################.#.#.#                                                         ###############.###########.#  
AX..#...#.#...#.#...#...#.#.#..HR                                                     JO............#.#.#...........#  
  #.#.###.###.#.#.#####.###.#.#                                                         #.#.#####.#.#.###.#.#.#####.#  
TX..#...#.......#...#.....#.#..EK                                                       #.#...#.#.#.......#.#...#.#..MM
  ###.#.###.#.#.#.#.###.#.#.###                                                         #.###.#.#######.#.###.###.#.#  
  #...#.....#.#...#.....#.....#                                                         #.#.#.....#.#...#...#.#.....#  
  #####.#.#.#####.###.#######.#        R     Y   G           U     A           M S      #.#.#.#.###.#####.#.#.###.#.#  
  #.....#.#...#.....#.....#...#        I     Q   P           C     X           M Y      #...#.#.#.....#...#.#...#.#.#  
  #####.#########.###.#####.###########.#####.###.###########.#####.###########.#.#######.#.###.#.#########.#.#####.#  
  #...#...#.#.......#.....#...#...#.....#.....#.....#.#.....#...#...........#...#...#...#.#.#.....#.#.......#.#.....#  
  #.#.#.###.###.#.#.#######.#####.###.###.###.#####.#.###.#.#.#########.#####.#####.#.#########.###.###.#####.###.#.#  
  #.#.......#...#.#.#.......#.....#.#.#.....#.#.....#...#.#.......#.#.#...#.......#.#.......#.#.#.#.....#.......#.#.#  
  #.#.#.#.#####.###########.#####.#.#.#.#.#.#####.###.###.#########.#.#.#######.###.#.#######.###.###.#.###.#.#.#.#.#  
  #.#.#.#...#.......#.......#.........#.#.#.....#.#.....#.........#.........#.#.#.....#.......#.......#.#.#.#.#.#.#.#  
  #######.#.#.#.#####.#.#########.#############.#.#.###.#######.#####.#.#####.#.#.#######.#####.#.#.###.#.#.#######.#  
  #.......#.#.#...#...#.#.........#.......#...#.#.....#.#.......#.....#...#.....#...........#.#.#.#.#.....#...#.....#  
  #.#.#.#####.#.#.#####.#.#######.#.###.###.###.#.###.#.#.###.#.#.#.###.#.#####.#.###.#.#.###.###.#.#.#.#####.#####.#  
  #.#.#.#.....#.#.#.....#...#.#.....#...#.......#.#...#.#...#.#.#.#...#.#.#.....#.#...#.#.......#.#.#.#...#.#.#.....#  
  #.###.###.#.###.###.#.#.###.#.#.#.#.###.###.#.#######.###.#.###.#######.#.#.#.#####.#.#.#.#############.#.#####.###  
  #.#.#.#.#.#...#.#...#.#.#.....#.#.#...#...#.#...#.....#...#...#...#.....#.#.#.....#.#.#.#.#.....#.#.#.......#...#.#  
  ###.#.#.#.#.###.#####.#############.#.#.#.#.#######.###.###.###.#############.#####.#####.###.###.#.#.#####.###.#.#  
  #.......#.#.#.....#...#.#.......#...#.#.#.#.#.#.#.#...#...#.#.....#.#.#...#.....#.#.#...#...#.......#.....#...#...#  
  ###.###.#.###.#########.#######.#####.#.#####.#.#.#.###.#######.###.#.#.#####.###.#.#.###.###.#####.#.#.###.###.###  
  #.....#.#.#.....#.....#.#.......#.#.#.#...#.......#.#.......#...#.....#.......#.........#.#.#.....#.#.#.#...#.....#  
  #.#####.#.###.#.#####.#.#######.#.#.#.#.#######.#.#.###.#####.#.###.#.###.#.#####.###.#####.#.#######.###.#.#.#.###  
  #.#.....#.#...#...#.......#.#.....#...#.#.#.....#...#.......#.#.....#.#...#...#.#...#...#.#.#.....#.#.#.#.#.#.#...#  
  #####.#.#.###.#######.#.###.###.#.#.###.#.#####.#######.#######.#.#####.###.###.###.#####.#.#.#####.###.#######.#.#  
  #.#.#.#.#.#.#.#...#...#...#.#.#.#...#.......#.#.....#.#.#...#...#.....#.#.......#.........#.#...#.#.........#.#.#.#  
  #.#.#######.#####.#####.###.#.#.#########.###.#####.#.#.#.#######.#########.#.###.#########.###.#.#.#########.#.#.#  
  #...#.#.#.#.....#.#...................#...#...#...#...#.....#...#.#...#...#.#.#.....#.#.......#.#.#.#.#.#.#...#.#.#  
  ###.#.#.#.#.###.#.#####.#############.###.#.#.#.#.###.#.#.#####.#.#.#####.###.#.###.#.#####.###.#.#.#.#.#.###.#.###  
  #...........#.#.#...#...#.#.......#.#...#...#.#.#...#.#.#...#.#.......#.....#.#...#.#.#.#.#.....#.....#.#.....#...#  
  #####.#.#.#.#.###.#####.#.#.#.###.#.#.#######.#.###.#.#.###.#.#####.###.###.#.#.###.#.#.#.#.#####.###.#.#.#########  
  #.#...#.#.#.............#...#...#...#.....#...#...#...#.#.#.#...#...#...#.#...#.#...................#.............#  
  #.#####.#######.#.###.###.#.#.#####.#.#######.###.#####.#.###.#.#.#####.#.###.#.#.#####.###.#####.###.#.###.#.#####  
  #.......#.......#...#...#.#.#.#.........#.....#.....#.......#.#.......#.....#.#.#.....#...#.....#...#.#...#.#.....#  
  ###################################.#######.###.#########.#######.#########.#######.###############################  
                                     Y       S   R         S       F         F       H                                 
                                     Q       Y   Q         I       M         W       R                                 """

# INPUT = """
#              Z L X W       C
#              Z P Q B       K
#   ###########.#.#.#.#######.###############
#   #...#.......#.#.......#.#.......#.#.#...#
#   ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###
#   #.#...#.#.#...#.#.#...#...#...#.#.......#
#   #.###.#######.###.###.#.###.###.#.#######
#   #...#.......#.#...#...#.............#...#
#   #.#########.#######.#.#######.#######.###
#   #...#.#    F       R I       Z    #.#.#.#
#   #.###.#    D       E C       H    #.#.#.#
#   #.#...#                           #...#.#
#   #.###.#                           #.###.#
#   #.#....OA                       WB..#.#..ZH
#   #.###.#                           #.#.#.#
# CJ......#                           #.....#
#   #######                           #######
#   #.#....CK                         #......IC
#   #.###.#                           #.###.#
#   #.....#                           #...#.#
#   ###.###                           #.#.#.#
# XF....#.#                         RF..#.#.#
#   #####.#                           #######
#   #......CJ                       NM..#...#
#   ###.#.#                           #.###.#
# RE....#.#                           #......RF
#   ###.###        X   X       L      #.#.#.#
#   #.....#        F   Q       P      #.#.#.#
#   ###.###########.###.#######.#########.###
#   #.....#...#.....#.......#...#.....#.#...#
#   #####.#.###.#######.#######.###.###.#.#.#
#   #.......#.......#.#.#.#.#...#...#...#.#.#
#   #####.###.#####.#.#.#.#.###.###.#.###.###
#   #.......#.....#.#...#...............#...#
#   #############.#.#.###.###################
#                A O F   N
#                A A D   M                     """

# process the input grid
donut = np.array([list(row) for row in INPUT.splitlines() if row.strip()])
nb_rows, nb_cols = donut.shape
print(f"{donut.shape=}")
# print the grid
for row in donut:
    print(*row)

possible_gates = tuple(
    [
        "".join((letter1, letter2))
        for letter1 in ascii_uppercase
        for letter2 in ascii_uppercase
    ]
)  # using a tuple is not mandatory, it's done to express better the intent: this is immutable
outer_gates = defaultdict(set)
# find and store the start and end positions, and collect outer gates names and locations
for i in range(nb_cols):
    if (seq := "".join(donut[:2, i])) == "AA":
        start_pos = (2, i)
        print(f"{start_pos=}")
    elif seq == "ZZ":
        end_pos = (2, i)
        print(f"{end_pos=}")
    elif seq in possible_gates:
        outer_gates[seq].add((2, i))
for i in range(nb_cols):
    if (seq := "".join(donut[-2:, i])) == "AA":
        start_pos = (nb_rows - 3, i)
        print(f"{start_pos=}")
    elif seq == "ZZ":
        end_pos = (nb_rows - 3, i)
        print(f"{end_pos=}")
    elif seq in possible_gates:
        outer_gates[seq].add((nb_rows - 3, i))
for i in range(nb_rows):
    if (seq := "".join(donut[i, :2])) == "AA":
        start_pos = (i, 2)
        print(f"{start_pos=}")
    elif seq == "ZZ":
        end_pos = (i, 2)
        print(f"{end_pos=}")
    elif seq in possible_gates:
        outer_gates[seq].add((i, 2))
for i in range(nb_rows):
    if (seq := "".join(donut[i, -2:])) == "AA":
        start_pos = (i, nb_cols - 3)
        print(f"{start_pos=}")
    elif seq == "ZZ":
        end_pos = (i, nb_cols - 3)
        print(f"{end_pos=}")
    elif seq in possible_gates:
        outer_gates[seq].add((i, nb_cols - 3))

# build the graph
neighbours = defaultdict(set)
# add the 'regular' neighbours (. to . connection)
for row in range(1, nb_rows - 1):
    for col in range(1, nb_cols - 1):
        if donut[row, col] != ".":
            continue
        if donut[row - 1, col] == ".":
            neighbours[(row, col)].add((row - 1, col))
        if donut[row + 1, col] == ".":
            neighbours[(row, col)].add((row + 1, col))
        if donut[row, col - 1] == ".":
            neighbours[(row, col)].add((row, col - 1))
        if donut[row, col + 1] == ".":
            neighbours[(row, col)].add((row, col + 1))

# collect inner gates written top to bottom
inner_gates = defaultdict(set)
for row in range(2, nb_rows - 2):
    for col in range(2, nb_cols - 2):
        if (seq := "".join(donut[row : row + 2, col])) in outer_gates:
            inner_gates[seq].add(
                (row - 1, col) if donut[row - 1, col] == "." else (row + 2, col)
            )

# collect inner gates written left to right
for row in range(2, nb_rows - 2):
    for col in range(2, nb_cols - 2):
        if (seq := "".join(donut[row, col : col + 2])) in outer_gates:
            inner_gates[seq].add(
                (row, col - 1) if donut[row, col - 1] == "." else (row, col + 2)
            )

# add the spacetime gates neighbours
all_gates = {
    gate_label: outer_gates[gate_label] | inner_gates[gate_label]
    for gate_label in inner_gates
}
for gate in all_gates:
    assert len((gg := all_gates[gate])) == 2
    assert gate not in ("AA", "ZZ")
    gate1, gate2 = tuple(gg)
    neighbours[gate1].add(gate2)
    neighbours[gate2].add(gate1)


# Now I need to add a few things to my part 1 code, namely:
# - tracking the current level (0 is outermost and then 1, 2, 3 etc. are inner levels)
# - define a maze for the 2 level types (outermost vs inner) as the gates change
# - adapt the recursion/BFS stopping criterion to: being at the ZZ gate AND at level 0

# perform the search with a recursive function
shortest_path_length = float("inf")
visited = set()
start_end_gates = frozenset({start_pos, end_pos})  # AA and ZZ gates
outer_gates_ = set()
for gate in outer_gates:
    outer_gates_ |= outer_gates[gate]
inner_gates_ = set()
for gate in inner_gates:
    inner_gates_ |= inner_gates[gate]
# AA and ZZ are NOT included in the set named outer_gates_


def recurse_part2(
    current_pos: tuple[int, int], current_path_length: int = 0, current_level: int = 0
) -> None:
    """Traverses the donut-shaped grids accounting for possible 'recursion' as defined in the text

    Args:
        current_pos (tuple[int, int]): the location of the current position
        current_path_length (int): the nb of steps of the current path
        current_level (int): defaults to 0. The current layer (0 is outermost, else it is an inner layer)
    """
    global shortest_path_length
    if (
        min(
            (
                dist
                for loc, dist, level in visited
                if loc == current_pos and level == current_level
            ),
            default=float("inf"),
        )
        <= current_path_length
    ):
        return
    if current_pos == end_pos and current_level == 0:
        if current_path_length < shortest_path_length:
            shortest_path_length = current_path_length
        return
    visited.add((current_pos, current_path_length, current_level))
    assert current_level >= 0
    if current_level == 0:
        for neigh in neighbours[current_pos]:
            if neigh in outer_gates_:
                continue  # it's a wall at this level
            if neigh in inner_gates_:
                recurse_part2(neigh, current_path_length + 1, current_level + 1)
            else:
                recurse_part2(neigh, current_path_length + 1, current_level)
    else:
        for neigh in neighbours[current_pos]:
            if neigh in start_end_gates:
                continue  # it's a wall at this level
            if neigh in inner_gates_:
                recurse_part2(neigh, current_path_length + 1, current_level + 1)
            elif neigh in outer_gates_:
                recurse_part2(neigh, current_path_length + 1, current_level - 1)
            else:
                recurse_part2(neigh, current_path_length + 1, current_level)


try:
    # import sys

    # sys.setrecursionlimit(10_000) # dangerous
    recurse_part2(start_pos)
    print(f"part 2: {shortest_path_length=}")
except RecursionError:
    print(
        "The maze is too large and triggers a RecursionError, let us switch to a BFS\n"
    )


# perform the search with a BFS
class Node:
    """A node in the graph for part 2, where one can walk"""

    def __init__(self, location: tuple[int, int], layer: int) -> None:
        self.distance = float("inf")
        self.visited = False
        self.location = location
        self.neighbours = neighbours[self.location]
        self.layer = layer

    def __repr__(self) -> str:
        return f"Node({self.__dict__})"


queue = deque()  # more efficient than a Python list ( O(1) popping vs O(n) for a list)
nodes = {0: {pos: Node(pos, 0) for pos in neighbours}}
all_gates_ = inner_gates_ | outer_gates_
st = nodes[0][start_pos]
st.distance = 0
queue.append(st)
while queue:  # takes several min to run
    current_node: Node = queue.popleft()
    if current_node.distance > 11_008:
        raise ValueError("something is wrong")
    # assert current_node.visited is False
    # if current_node.visited:
    #     continue  # i don't understand why this can happen
    # for gate_label in inner_gates:
    #     if current_node.location in inner_gates[gate_label]:
    #         print(f"Inner gate {gate_label}, {current_node.__dict__}")
    #         break
    #     if current_node.location in outer_gates[gate_label]:
    #         print(f"Outer gate {gate_label}, {current_node.__dict__}")
    #         break
    if current_node.location == end_pos and current_node.layer == 0:
        print(f"Part 2 with BFS: {current_node.distance}")
        break
    # assert current_node.layer >= 0
    if current_node.layer == 0:
        for cand in nodes[current_node.layer].values():
            if any(
                (
                    (current_node.location in outer_gates_)
                    and (cand.location in inner_gates_),
                    cand.location not in current_node.neighbours,
                    cand.visited,
                )
            ):
                continue
            if (
                (current_node.location not in inner_gates_)
                or (cand.location not in outer_gates_)
                and cand not in queue
            ):
                cand.distance = current_node.distance + 1
                queue.append(cand)
            else:
                next_ = nodes.setdefault(
                    current_node.layer + 1,
                    {pos: Node(pos, current_node.layer + 1) for pos in neighbours},
                )[cand.location]

                # assert next_.layer == current_node.layer + 1
                if not next_.visited and next_ not in queue:
                    next_.distance = current_node.distance + 1
                    queue.append(next_)
    else:
        for cand in nodes[current_node.layer].values():
            if any(
                (
                    cand.location in start_end_gates,
                    cand.location not in current_node.neighbours,
                )
            ):
                continue
            if current_node.location in inner_gates_ and cand.location in outer_gates_:
                next_ = nodes.setdefault(
                    current_node.layer + 1,
                    {pos: Node(pos, current_node.layer + 1) for pos in neighbours},
                )[cand.location]
                # assert isinstance(next_, Node) and next_.layer == current_node.layer + 1
                if not next_.visited and next_ not in queue:
                    next_.distance = current_node.distance + 1
                    queue.append(next_)
            elif (
                current_node.location in outer_gates_ and cand.location in inner_gates_
            ):
                next_ = nodes.setdefault(
                    current_node.layer - 1,
                    {pos: Node(pos, current_node.layer - 1) for pos in neighbours},
                )[cand.location]
                # assert next_.layer == current_node.layer - 1 and isinstance(next_, Node)
                if not next_.visited and next_ not in queue:
                    next_.distance = current_node.distance + 1
                    queue.append(next_)
            elif not cand.visited and cand not in queue:  # staying at the same level
                cand.distance = current_node.distance + 1
                queue.append(cand)
    current_node.visited = True


else:
    raise ValueError("Queue exhausted, this is impossible to solve")

# 6300
