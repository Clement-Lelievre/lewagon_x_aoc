import pandas as pd
import networkx as nx
from networkx.exception import (
    NetworkXNoPath,
)  # because by default, when no path is found, an error is raised

FAVORITE_NB = 1364  # my input
START_LOCATION = (1, 1)
END_LOCATION = (39, 31)  # (4,7) # given as 7,4 in the text
# beware: grid is 0-indexed but the root node is located at (1,1)

# step 1: build the maze
def get_location_type(
    coord: tuple[int, int], favorite_nb: int = FAVORITE_NB, view: bool = True
) -> str:
    y, x = coord
    if x < 0 or y < 0:
        return
    bin_nb = bin(x * x + 3 * x + 2 * x * y + y + y * y + favorite_nb)
    return ("." if view else 1) if bin_nb.count("1") % 2 == 0 else ("#" if view else 0)
    # FYI, to count the number of 1s there's also this neat possibility (https://dev.to/anurag629/the-power-of-bit-manipulation-how-to-solve-problems-efficiently-3p1h):
    # x = 0b01010101  # The number 85 in binary
    # count = 0
    # while x:
    #     count += 1
    #     x &= (x - 1)
    # print(count)  # The output is 4


solved = False
nb_rows, nb_cols = 100, 100  # somewhat arbitrary initialization

while not solved:
    try:
        print(f"trying {nb_rows=}, {nb_cols=}")
        df = pd.DataFrame(
            {f"{y}": [(x, y) for x in range(nb_rows)] for y in range(nb_cols)}
        ).applymap(get_location_type)
        # step 2: find the shortest route to reach location 31,39 (meaning row 39, col 31)
        grid = df.to_numpy()
        assert grid[END_LOCATION] == ".", "end location should be an open space"
        G = nx.Graph()  # undirected, unweighted graph
        for row_ind in range(
            nb_rows
        ):  # should be optimized instead of rebuilding the whole maze from scratch every iteration
            for col_ind in range(nb_cols):
                current_pos = (row_ind, col_ind)
                current_type = grid[current_pos]
                if current_type == ".":
                    if col_ind > 0 and grid[row_ind, col_ind - 1] == ".":
                        G.add_edge(current_pos, (row_ind, col_ind - 1))
                    if col_ind < nb_cols - 1 and grid[row_ind, col_ind + 1] == ".":
                        G.add_edge(current_pos, (row_ind, col_ind + 1))
                    if row_ind > 0 and grid[row_ind - 1, col_ind] == ".":
                        G.add_edge(current_pos, (row_ind - 1, col_ind))
                    if row_ind < nb_rows - 1 and grid[row_ind + 1, col_ind] == ".":
                        G.add_edge(current_pos, (row_ind + 1, col_ind))

        shortest = nx.shortest_path_length(G, START_LOCATION, END_LOCATION)
    except NetworkXNoPath:
        print(
            "Path not found, either because it is impossible or the grid is not extended enough"
        )
        nb_rows += 500
        nb_cols += 500
    else:
        solved = True
    finally:
        print(shortest)

# my map was not tricky so a 100x100 grid was sufficient. It could have required a much bigger map if long detours had been needed
# part 2

# How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?
answer = len(
    [v for v in nx.shortest_path_length(G=G, source=START_LOCATION).values() if v <= 50]
)  # I found out in the docstring that not specifying a target square allows to call the function in all target nodes
print(answer)

# I feel lucky because:
# 1) the grid was nice in the sense that arbitrarily setting its size to 100*100 was enough to get both stars, without having to expand it
# 2) leveraging the powerful networkx package yields potent results, and the heavy lifting is done for me

# Now that I've solved this challenge I feel like coding DFS/BFS by myself
