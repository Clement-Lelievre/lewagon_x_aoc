import numpy as np

TEST_INPUT = """
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

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


def input_to_numpy(input_: str) -> np.array:
    return np.array([list(row) for row in input_.splitlines() if row.strip()])


def simulate(input_: str, n_sim: int = 10, verbose: bool = False) -> int:
    """runs the simulation ten times and returns the resource value

    Args:
        input_ (str): _description_
        n_sim (int, optional): _description_. Defaults to 10.
        verbose (bool, optional): _description_. Defaults to False.

    Returns:
        int: _description_
    """
    grid = input_to_numpy(input_)
    grid = np.pad(grid, pad_width=1, mode="constant", constant_values="")
    nb_rows, nb_cols = grid.shape
    for _ in range(n_sim):
        new_grid = np.empty_like(grid)
        for row_nb in range(1, nb_rows - 1):
            for col_nb in range(1, nb_cols - 1):
                neighbours_array = grid[
                    row_nb - 1 : row_nb + 2, col_nb - 1 : col_nb + 2
                ]
                current_cell = grid[row_nb, col_nb]
                if current_cell == ".":
                    new_grid[row_nb, col_nb] = (
                        "|"
                        if neighbours_array[neighbours_array == "|"].size >= 3
                        else "."
                    )
                elif current_cell == "|":
                    new_grid[row_nb, col_nb] = (
                        "#"
                        if neighbours_array[neighbours_array == "#"].size >= 3
                        else "|"
                    )
                else:
                    new_grid[row_nb, col_nb] = (
                        "#"
                        if (
                            neighbours_array[neighbours_array == "#"].size >= 2
                            and neighbours_array[neighbours_array == "|"].size >= 1
                        )
                        else "."
                    )
        grid = new_grid
        if verbose:
            for row in grid:
                print(*row)
            print("\n")
    return grid[grid == "|"].size * grid[grid == "#"].size


assert simulate(TEST_INPUT) == 1147
print("part 1:", simulate(INPUT))

# part 2
# given the absurdly high nb of simulations to run, I'm expecting I can find some invariant
# more specifically, that after n0 simulations the grid gets back to its initial state
# note that there is no test value provided for this part


def repeat_until(input_: str) -> int:
    grid = input_to_numpy(input_)
    grid = np.pad(grid, pad_width=1, mode="constant", constant_values="")
    initial = np.copy(grid)
    nb_rows, nb_cols = grid.shape
    n_sim = 0
    while not np.array_equal(grid, initial) or n_sim == 0:
        new_grid = np.empty_like(grid)
        for row_nb in range(1, nb_rows - 1):
            for col_nb in range(1, nb_cols - 1):
                neighbours_array = grid[
                    row_nb - 1 : row_nb + 2, col_nb - 1 : col_nb + 2
                ]
                current_cell = grid[row_nb, col_nb]
                if current_cell == ".":
                    new_grid[row_nb, col_nb] = (
                        "|"
                        if neighbours_array[neighbours_array == "|"].size >= 3
                        else "."
                    )
                elif current_cell == "|":
                    new_grid[row_nb, col_nb] = (
                        "#"
                        if neighbours_array[neighbours_array == "#"].size >= 3
                        else "|"
                    )
                else:
                    new_grid[row_nb, col_nb] = (
                        "#"
                        if (
                            neighbours_array[neighbours_array == "#"].size >= 2
                            and neighbours_array[neighbours_array == "|"].size >= 1
                        )
                        else "."
                    )
        grid = new_grid
        n_sim += 1
    print(n_sim)


# repeat_until(INPUT)


def get_neighbours(ind: int) -> list[int]:
    """returns the indices of the neighbours of a given index

    Args:
        ind (int): _description_
        list_length (int, optional): _description_. Defaults to 2_500.

    Returns:
        list[int]: _description_
    """
    if ind == 0:
        return [1, 50, 51]
    if ind == 2499:
        return [2498, 2449, 2448]
    if ind == 49:
        return [48, 99, 98]
    if ind == 2449:
        return [2399, 2450, 2400]
    if ind < 50:
        return [ind - 1, ind + 1, ind + 50, ind + 51, ind + 49]
    if ind > 2449:
        return [ind + 1, ind - 1, ind - 50, ind - 49, ind - 51]
    if ind % 50 == 0:
        return [ind - 50, ind + 50, ind + 1, ind + 51, ind - 49]
    if ind % 49 == 0:
        return [ind - 50, ind + 50, ind - 1, ind + 49, ind - 51]
    return [
        ind - 1,
        ind + 1,
        ind + 50,
        ind - 50,
        ind - 51,
        ind - 49,
        ind + 51,
        ind + 49,
    ]


def get_all_neighbours(list_length: int = 2_500) -> dict[int, list[int]]:
    """returns a dictionary with the indices as keys and the neighbours as values

    Args:
        list_length (int, optional): _description_. Defaults to 2_500.

    Returns:
        dict[int, list[int]]: _description_
    """
    return {ind: get_neighbours(ind) for ind in range(list_length)}


neighbours = get_all_neighbours()
grid = INPUT.replace("\n", "").strip()
assert isinstance(grid, str)
assert len(grid) == 2_500
assert set(grid) == {"#", "|", "."}
for _ in range(10):
    new_grid = []
    for ind in range(2_500):
        current_cell = grid[ind]
        if current_cell == ".":
            new_grid.append(
                "|"
                if sum(grid[neigh_ind] == "|" for neigh_ind in neighbours[ind]) >= 3
                else "."
            )
        elif current_cell == "|":
            new_grid.append(
                "#"
                if sum(grid[neigh_ind] == "#" for neigh_ind in neighbours[ind]) >= 3
                else "|"
            )
        else:
            new_grid.append(
                "#"
                if (
                    sum(grid[neigh_ind] == "#" for neigh_ind in neighbours[ind])
                    and sum(grid[neigh_ind] == "|" for neigh_ind in neighbours[ind])
                )
                else "."
            )
    grid = new_grid
    assert len(grid) == 2_500
print(grid.count("|") * grid.count("#"))
