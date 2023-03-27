from collections import defaultdict
import numpy as np

INPUT = """.#..####.........##...##...#.#.#.##..##.....##.##.##...#..##..#.###...
..######..####..##.#...####.#...#..####..#.#....#..#.#...#........#.#.
.#####.###.#...##....##..........##.###.#....#.##.####..#.#..#.##..#.#
#.#..#.###.##.#..##.#####...##...####..#.....###.##..#....##.#......#.
##.##.##....###....####.##.#....##.##.###..##..##...#.#...#..#.###.##.
....#.######....#..#....#.##.#.##..##.#.##...###..####....#.####.####.
.#..#..#.#.##.#...#.###...##..##...##...#.##...##..#.#..##.#..#...##.#
.###.#...#.#..#...####..#.##....#.####.##..##.#..###..###..#...####..#
..##....#....#..##...###..#.#..####...#..####.....#.###...###..##..#..
.#######.#.#.##.##.##.###.#.#.#.#.####.#..#..##...#.##.##.##..#.....#.
..##.##....#####.#.#######....#...###...#...#######.#..##....#..#####.
##.#.#.#.###.#.#..##...#..###.######..##.##.#..##....#.##.#...#.####..
.##.....#.####.##...#.########.##.###.##.....#.####.....##.......#.###
#.....##...#####.#.##..#######...###.####....#.#..##..####......#..#.#
#####....#..####..######...#..####.#..#.##...#######..#.#..###....##.#
.##.###..#.##...###..#..#.####.....##...#####.....##..#..#.#....###..#
..##...####.##.######.....#....##...##.#...#.##.#.......##.#..#####.#.
...##.#.###..#...#########.##.#..####.#.#.#.###.#.#.#..#.#.##.#..#.#..
.#.##..#.#.###.###.#...#.#..##.#.##.##...###....#######......#..##...#
##...##.#..#...#..#...###.##......##..#.###.......#..######.##...##.#.
.#..#.########..#...##..###..#.....##.##...#..###.##..#..##.....##..##
...#.###...#.#...#.#..#.##.##.##....#..#..#.#.##...#..#..#.###...##.##
.##....###.#.#..#.#.###.#..#..#.......###.###....#######.....####...##
.#..####..###..##.##.#.#..#.....#.....###.######..##....###########..#
..####..###.#..#...###.#.###....#..#.#..##......####.##..#..####.#....
##.##.##.#..#.##...#......##.##..#..#.#..#.##....#.#..#.#...#.#.#.#...
...#..####.#.#..#....#.#.##....##.##..#....#..##..#.#.#.###.##.#.##...
....#.#.#.#..###.....###.#..###.#####.###.#...#..######...#...##.#..#.
#...########.#..##...##..#.##...#..#.##.....##..##.##.#.####.##..#..##
#.#####..##.##.##.###.#.###..#.#.##.###.#.#..###.#.#...#.###.#..#...#.
.#..######.####...##..###.####.#.###.#.....######.#..##..#.###.#..####
##.#..####...#.......####.##.#.######.#...#..#.####.#.......#......###
..##...####...#.#######..####.##..##.........#.##.#..##...##..##.....#
.#..#####.#...#.#..##.###....##.##...##......#..#.##..#.#.#..#.##.####
.#.####.#.##.#####...#..##...###.#.#..#...#..#.##.......###...#...##..
....#....###..##....####.##...##.#.##.#.##.##.#.......#..#.##.####.##.
###.###.#.###.##.......##.###....#...##.....#.#......##.#.###.#....#.#
#...#...#..#.##.##.#..#..####..##.......#.#.#######.##..###..###.#.#..
...###.###..###.##.#.##.#.####.#..#.##..#####..##...####.#.#.#.#...#..
..#...##.#.....####.##....#...#.#..#.#..##..##..#####..##.###...#.###.
#.#...#...#.#..####..####...#....##...#.........##...#####.#.####.###.
#..###.....##..#..##......#.##...####..###...####...#.#....#....#....#
.#...##.##..#.#...#.#.#.##.####.#....#####..#...#####.#.....###..#.##.
###..#....##..##....##..#..##...##...#.##.####.####..#..#....#...###.#
.#.#.##..###.#..###..####..######.#...#####.#...####.#..##.##.......##
..#..##....##.#.###.#..##..#.#####...###...#.#.##.#.###..##.######..##
###.##.#.#....#..#..##.#.#.##..###..##...#...###..#..#######..#.##.#.#
#.#..#...#..###.##.##.#####...####.#.#....#...#....#.###.#..###.##....
##..###.#..#.##.######..##.#.#.....###.#..#..##...#.#..####.##.#.###.#
#.#..##.#.#.#####.###.###.#.#.##.###.....###.#.#..####.##.##..#.##..#.
###.#####..######..###.##.#.#.####....#..#..#.#.#..#.#..##.......##.#.
#..#....#.#..###.#.##.##..#..#.#.#.###..#...##..###.#....###..#....#..
.#.##.#.####...##...#.####..##.#.##.#...####.##...#....##.#..##.....##
#...###....######.##.....####.#.#.#..#..##..#..###.#####..###...#...#.
#.##...#.###.##.##.####.##.###..##..#...##....#.#..###..##....#####.##
#...########..##.#.##.##.####..#.###..##...##.#.#...#.####.#..###.#..#
.#.#....###...####.####.....###.##.#.#...#..#.#.#.##.....#.###......##
.###....#....#.#.##..#....#.##......#.#.##....##.##...###.#.#.##.....#
.........#..#.#..###..##...###.....###..##....###..#.#...##..#.###..#.
#.####.##....#...#.#.##.####.#.#.#....##....#.########.....##...#.##..
.#....#.###...###..#..#..#......##.##..#.###.#.######...##.##....#....
#..##.##..#.#.#.##.#..###.#..#######.#.#..#...##....#..###.#....##.##.
#.#..####..#.###..####....###.###..#.###.##...##...#.####..####...#.#.
#.##.###.###.##.##.#....#..#.##.#..##.#.##..##.###..#.#.####.#..###...
#.#####.#...##.#..##.###.####..####.#..##.#.......#......#.#.##..#.##.
##.##..#..###.#.##....#..###..###.##.####.###.####.#..###..#..####.###
#..##.####.#..#######..#..#....#..#####..#.#......#.####.#..#...#..##.
.##.#####....#.#.#..###.##..##.#..#.###..##....#....####...#.####.#..#
#.#..##.##..#####...##.#.#####..#.###..#...##..##.##.####.##.##.###.#.
#.####..#...#.###.#...#.######..###.####.#....##..#..##.###.#..#......
"""


def process_input(input_: str) -> np.array:
    mapping = str.maketrans(".#", "01")
    grid = np.array([list(row) for row in input_.translate(mapping).split()], dtype=int)
    grid = np.pad(grid, pad_width=100)  # adjust padding if necessary
    return grid


def elf_stops_moving(coord: tuple[int, int], grid: np.array) -> bool:
    assert grid[coord] == 1
    row, col = coord
    return grid[row - 1 : row + 2, col - 1 : col + 2].sum() == 1


def locate_elves(grid: np.array):
    elves = np.nonzero(grid)
    return zip(elves[0], elves[1])


def process_is_finished(grid: np.array) -> bool:
    # If no other Elves are in one of the eight positions around them, the Elf does not do anything during this round
    return all(elf_stops_moving(elf_coord, grid) for elf_coord in locate_elves(grid))


def move_is_possible(
    grid: np.array, elf_coord: tuple[int, int], direction: str
) -> bool:
    row, col = elf_coord
    if direction == "N":
        return grid[row - 1, col - 1 : col + 2].sum() == 0
    elif direction == "E":
        return grid[row - 1 : row + 2, col + 1].sum() == 0
    elif direction == "S":
        return grid[row + 1, col - 1 : col + 2].sum() == 0
    elif direction == "W":
        return grid[row - 1 : row + 2, col - 1].sum() == 0
    else:
        raise ValueError("Bad direction")


def update_directions(directions: list[str]) -> list[str]:
    return directions[1:] + directions[:1]


def update_grid(candidates_dict: dict[tuple : list[tuple[int, int]]]) -> None:
    for target_square, elf_squares in candidates_dict.items():
        if (
            len(elf_squares) == 1
        ):  # elves wanting the same target square do not move at all
            grid[elf_squares[0]] = 0
            grid[target_square] = 1


def get_smallest_rectangle(grid: np.array) -> np.array:
    """Returns the smallest rectangle that contains every Elf"""
    elves = np.nonzero(grid)
    upper_row_ind = elves[0].min()
    lower_row_ind = elves[0].max()
    left_col_ind = elves[1].min()
    right_col_ind = elves[1].max()
    return grid[upper_row_ind : lower_row_ind + 1, left_col_ind : right_col_ind + 1]


def compute_nb_empty_tiles(grid: np.array) -> int:
    return grid.size - grid.sum()


grid = process_input(INPUT)
directions = ["N", "S", "W", "E"]
for _ in range(10):
    # proceed to round
    candidates_to_move = [
        elf_coord
        for elf_coord in list(locate_elves(grid))
        if not elf_stops_moving(elf_coord, grid)
    ]
    candidates_dict = defaultdict(list)
    for elf_coord in candidates_to_move:
        for direction in directions:
            if move_is_possible(grid, elf_coord, direction):
                row, col = elf_coord
                target_square = row + (
                    1 if direction == "S" else (-1 if direction == "N" else 0)
                ), col + (1 if direction == "E" else (-1 if direction == "W" else 0))
                candidates_dict[target_square].append(elf_coord)
                break
    update_grid(candidates_dict)
    # update the grid
    directions = update_directions(directions)

print(compute_nb_empty_tiles(get_smallest_rectangle(grid)))
# part 2

grid = process_input(INPUT)
directions = ["N", "S", "W", "E"]
nb_rounds = 0
while not process_is_finished(grid):
    # proceed to round
    candidates_to_move = [
        elf_coord
        for elf_coord in list(locate_elves(grid))
        if not elf_stops_moving(elf_coord, grid)
    ]
    candidates_dict = defaultdict(list)
    for elf_coord in candidates_to_move:
        for direction in directions:
            if move_is_possible(grid, elf_coord, direction):
                row, col = elf_coord
                target_square = row + (
                    1 if direction == "S" else (-1 if direction == "N" else 0)
                ), col + (1 if direction == "E" else (-1 if direction == "W" else 0))
                candidates_dict[target_square].append(elf_coord)
                break
    update_grid(candidates_dict)
    # update the grid
    directions = update_directions(directions)
    nb_rounds += 1

print(nb_rounds + 1)
