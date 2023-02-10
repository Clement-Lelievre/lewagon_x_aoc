INPUT = """...#...#|....#.|..#..||....|#.#|...|...||.##......
|.#...#......##|..|..#...|.|.....|.||.|##....#||.|
........|#.....|....|....#|...#...|.....|.|.|.|||.
#.#......#.#..||#..#.||..|...|.#|..#|...|...###...
.##.|.|....#.|.|##.....|..##.....#|..#....#..#..|.
.|.......|.....#.#.||.#...##...#..#..|.##...#|.|..
.|.#.##.#...|.|..#..||#....#..||....|||##....##.|.
|..|#....####..|..#...#|#..||.|.#||#.#|.|......#||
|#...#.|...||.|...#|.|##.|.|##|...|.#|#....##..###
.##....#|.###|..|....#.....|.###.#.#.|.|....|.#...
|........|....|...#|..#....#.#.|...#..#.#.|.|||#.#
.#|.|.#.|.....|.||#......##....|.|...###.....#..#.
...||.##..##.#...#..#..#..|.#||...|.#.|#..|..|..#.
..#.##||......#.|#.|.#.#|.|.#|.#|......||....|###|
.|#.#...|...|.#...#.||.|##.||.#.##..#...#.#....|#.
.|.|#...|..#|...........#....||.|.##...#..#||..##.
........#.|##....|||#.#|..||....||##.#.#....|...||
.........|||....#|#.#...#.#...|.......|.....#||.#.
|#||#|....|#...#||..|#|.|.....#......|#....#|#.|.|
.#|..|#.....|..|...#....|.|.#.||..|#.#.|.|#.##..|.
#||#...#.#||#.|#.#.|##........#...##|.#.....|.||.#
...#.#..##|.###.#..#.||||.#..#..|.|.....|||......#
|.||......|.#.......|....|.|.|...|##.###.#||###..|
|..|..||...#....#|#....||..#.....||#|..#|.......|.
....|.#....|..#..#.....#.|..|....|.##...|.||....##
|.#.#..#..#.|..#.#.........||....|.....##.......|.
##||.|.|#|...#.|...|.#.....|||.#....|..##|....#.|#
|#|..#...#.|||#...|.||#..#.#|#|....#|#...|#.#.#.#|
#.##.#..#....|....|....#..#.#..|.#..#|.|.#.||.|..#
#.|...||#..#.....#|.##|...|.#.#....||#|...#...|.|.
|.|||#|..|||.##||...#.||#.....|...|....|..|||#..|.
..|.#.#|.|||||..#..#......|#...#|||..#..|||#...#..
.#|#|.#.#||..#|#...|.|...|.#..#..........#.......|
.#..|...|....||#|.|#.|...#.|#.#||.#..|.|..|#...#|.
....|.|##||....#|.|..##.|..#.#..##...#.||.||.|...|
....|||#......#|.........#.|.#...#.|.#.|#..#....||
|.#|.#....#.||....#..#...#..|.#|...|.#............
.||...||...#.#..|#...|..|.##.|#....|..|.||#.#.|.#.
#....|.#......#.|..##..|.|.|..#.|#.|....#..|.|.#.#
#.||#...#|#.|#..||||..#|#..#|.#.|##........|.##.|#
.#..#....###.#|........#..|..|.||||..........#.#..
.|...#..||#.#......##....#.##.#.#|...|.|##..#.|...
|..|.|.|...###.||..||||.##|##..#.|..#..||.#.......
....###.##||.||......#...#...#|..||||....|.|..#...
#.....#..|...#.|..||.||.....#.#...#|.|...#|.#.#.|.
.|...#..|.|...|#.|..#|.#..|....||.#|..|||.||..|##|
|.|##||###|.|##....#..#.|..............##....#.#||
##.......|#...#||#...|....|#...#.#....#...###|..#.
.#..||#.|#|...|....|#.|##..|||........|||#|.....||
#.#.|#||.|##.|#..##.#|#####..||..||.#...........|#"""


def find_neighbours(num: int) -> list[int]:
    """Returns the neighbours of a given number

    Args:
        num (int): the index

    Returns:
        list[int]: the neighbours indices
    """
    assert 0 <= num < 2_500
    x_index, y_index = num // 50, num % 50
    return frozenset(
        [
            i * 50 + j
            for i in range(x_index - 1, x_index + 2)
            for j in range(y_index - 1, y_index + 2)
            if (0 <= i < 50) and (0 <= j < 50) and (i != x_index or j != y_index)
        ]
    )  # frozenset is not mandatory, just for the intent


grid = INPUT.replace("\n", "").strip()
assert isinstance(grid, str)
assert len(grid) == 2_500
assert set(grid) == {"#", "|", "."}
NEIGHBOURS = {ind: find_neighbours(ind) for ind in range(len(grid))}


def next_state(grid: list[str]) -> list[str]:
    """Simulates one minute

    Args:
        grid (list[str]): the grid state at the start of the simulation

    Returns:
        list[str]: the grid state at the end of the simulation
    """
    new_grid = []
    for ind, current_cell in enumerate(grid):
        if current_cell == ".":
            new_grid.append(
                "|"
                if sum(grid[neigh_ind] == "|" for neigh_ind in NEIGHBOURS[ind]) >= 3
                else "."
            )
        elif current_cell == "|":
            new_grid.append(
                "#"
                if sum(grid[neigh_ind] == "#" for neigh_ind in NEIGHBOURS[ind]) >= 3
                else "|"
            )
        else:
            new_grid.append(
                "#"
                if (
                    sum(grid[neigh_ind] == "#" for neigh_ind in NEIGHBOURS[ind])
                    and sum(grid[neigh_ind] == "|" for neigh_ind in NEIGHBOURS[ind])
                )
                else "."
            )
    return new_grid


for _ in range(10):
    grid = next_state(grid)

print("part 1:", grid.count("|") * grid.count("#"))

# part 2
# given the absurdly high nb of simulations to run, I'm expecting I can find some invariant
# more specifically, that after n0 simulations the grid gets back to its initial state
# note that there is no test value provided for this part
TARGET_NB_ITER = 1_000_000_000
grid = list(INPUT.replace("\n", "").strip())
nb_iter = 0
states = [grid]  # usually you use a set for O(1) membership test,
# but here I'll need to retrieve the index
while True:
    grid = next_state(grid)
    nb_iter += 1
    if grid in states:
        cycle_length = nb_iter - (ind_repeat := states.index(grid))
        print(f"{cycle_length=}", f"; start of cycle at iter #{ind_repeat}")
        break
    states.append(grid)


# find how many simulations to run after I fit as many cycles as possible
nb_sims_to_run = (TARGET_NB_ITER - ind_repeat) % cycle_length

for _ in range(nb_sims_to_run):
    grid = next_state(grid)  # reusing the grid state out from the while loop
print("part 2:", grid.count("|") * grid.count("#"))
