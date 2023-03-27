import numpy as np
import pandas as pd
from tqdm import tqdm

JETS = ">>><<<<><<><<<>>>><>>>><<><<<<>>>><<<<>><<>><<<>><<>>>><<<>>>><<<<>>><>><<<<>>><<<<>>>><<<>>>><<<>><<><><<>>><<<<>>>><<<><<<<>>><<<<>>>><><<<<><<<>>>><<<<>>><<><<<<>>>><<<>>>><<<><<<<>>><<<<>>><<<<>><<<<>>>><<><<<>><<<><<<>>>><<<<>><>><<><<<<><<<>>>><<<>><<<>>>><>><<<>>>><<>>><>>>><>>><<<<><<<>>><<<>>><<<<>>>><<<><<<<><>><<<>>>><>><>><>><>><<>><<<>>>><<><>><<<<>><>><<>><<<<>>><<<>><>>><>><<>>><>><<<<>><<<<><<<<>><<<>><<<>><<>><>>><<<<><<<>>><>>><>>>><<>><<<<><<<<>><<<>>>><<<<><<<>>><<<>>><<<>>>><<><<<>>>><>>><>>><<<<>>><<<<>>>><>>><<<<>><<>><<<<><><<<><>>><<<<>>><<><><<<<>>><<>>>><>>><>><<>>>><<>><<>>><>><<<><>>><<>>>><<><><<<>><<<<>><><<<<>><<>>>><<>>><>>><>>><>><<<>>>><<<<>><<><<<>><>>><<<>>><<<>>><<<<>>>><<<>>><<<<>>><<<><<>>>><<<<>>><<<<>><<<>>><<>>>><<<<><<<<>><<><<<<>>><<<<><<<><<<>><>>><<<>>><>><<<><<<<>><<<>>>><>>>><<<><<<>>><>>><<<>>><<<><>>><>><<<<>>><<>>><<>>>><><<<<>>><>><>>>><>>><<<<><<<>>><<>>>><>><<<>>>><<<>><><<<><<<>><<<><>>><><<<<>><<>>>><><<<>>>><>>>><<<>>>><<<<>>>><<<<>>><<<><<<>>>><>>>><<<<>><<<<>>>><<>><>><<<<>><<><<<>><<<<>>>><>><<<<><<<>><>>><<<<>><>>>><>>>><><<><<<<>><<<>><<>>><<<>>><<<<>>>><<<>>>><<<>><<<<>><<<<><>>><><<<<><<><<<><<>>>><<<><<><<>>>><<>>>><>>>><>><<<<>>>><<<<><>><<>>><><<<<>>>><<>><><<>>><<<<>>><<<>>><<<>><>>><<<<>>>><>>>><>>><<<>>>><<>>><>>>><<>>>><<<<><>>>><<>><<<><>>><<<>>><>>>><<<>>>><>><<<>>>><>><><<<<>>><<<<>><<<>>>><>>>><<<<>><<<>>>><<><<<><<<>>><<<<>>>><<<><<>><>>><<<<>>><<<>>>><>>>><<<<>>>><<>>><<<>><>>>><<<<>><<<<><>>><<<<>>><>>>><<<<>>><>>>><<><<>>>><<>>><<<<>>>><<<<>><<<<><<<>>><<<<><<<><>>>><>>><<>><<<<>><><>><<>>><>>>><><<<>>>><<>><<<>>>><<>><<><<>>>><<<<>>>><<<<>>><<<<>>><>><<<>>><<<>>><<<<>><<><>>>><<<>>><<>>>><<>>><<>>><<<<>>>><<<<>>>><>><<<>><<<<>>>><<<>>>><><><<<<>>><<<>>><<<<>>><<<><<<<>><<<>>><<<>><<>>>><<>>><<>>>><<<><<>>>><<><<<><<<>>><<<<>>><>>><<<<>>><>>><<<>>>><>>><<<><<><>>><<>>><<>>>><<<<>><<<<><><<<<>>>><<<<>><<<><<<>><<<>>>><<>><<>>>><<><<>>><<<<><<<>><<<>>><>><<>><<<<>>>><<>>>><<<><>>><<<><<>>><<<<>>>><<<>>><<>>>><<<<>>>><<<>>>><<<>><<<>><<<<><<<<><<>>><<<<>><<<>>><>><>><><<<>>>><<>>><>>><<><>>>><<>>><<>>><<><><<<<>><<<>><<<<>>>><>>>><>>><<<<>><<<><<<>>><<<<><<><>>>><<<>>><<<><<>>>><<<>><<<<>>><>><<<<>><<<>><><<<<><<<<>><>><<<>>>><<<>>><<<>>><>>><<<>><<>>>><<<>>><<<<>><>>><<>>>><>><<<<>>>><>><<<>>>><>>><<<<>>><><<<>><<<>>><>><<<<><<<><<<>>>><>>>><<<<><>>>><<>>>><>>><<>>><>>><<<<>>><<<><>>>><>><<>>><<<<>><<<><<<><>>>><<<<>><<>><<<<>>>><>>>><><<<<>><<<>>>><<<>>>><<<>>>><<>>>><<<><>>>><<<>>>><<<<><<<>><<<<><><<<>><<>><<>><<><<<<><<>><<<<>>>><<<>>><<<><>><<>>>><<>>><>><<><<<><>>><<><>><<<><>><<<><<<>><<>>><<<>>>><<<<>><<<>>><>>><<<<>>><><<<<>>><<<<>>>><>><<>>>><<<<>>><<<>>><><>>><><<<<>>>><<<>>>><<<<>><<><<<<>>>><<><>>><<<>>><<>>><<<><<>>>><<<<>>><<<>>>><<<<>><<<>>>><<<>><<>><><<<>><<<<>>>><>><<<<>><<><<<<>>>><>><<>>>><>>>><><<<<>>>><<>><>>>><<>>>><<><<<<><>>>><>>><<>>><<<><<>>><<>>>><>>>><>>><>>>><<<>><<<<>>><<>>><<<<>>><><<>><<>><<<>><<>><<<>>>><<>>>><<<<>>><<<>>>><<<>>>><><<<<>><<>><<<<><<<>>><<<>><<<<>><<<<>>>><<<<>><<<>><<>>>><<<<>>>><<<<>>><<<<>>>><<>>><<>>>><<>><<<>>><<>><><<<>><>>>><<<>>><>>><<<>>>><<<<><>><<<<>><<>>>><<>><<<<>>>><<<><<><>>>><>>>><<><<<>>>><<>><<<<>>>><<<<><>><<<>><>>><<<<><>>>><<><<>>>><<<<>>>><<<<><<<>><<>><<>><>>><<<><<<<>>>><<>><<>>>><>>>><<<><>>>><<<<>>>><<<<>>>><<>>><<<<>>><<<>><>>>><<<><<>>><<>>>><><<<>><>>>><<<><<>><<>><<<>>><>><>><<>>>><>>><<><<>><<<><>>>><<<<>>><<<>><<<><<<<>><<<><>><<<><<>>><<<>>><>><>><<<>>>><<<><>>>><>>><<>>>><<<>><<<<>>>><<<>><>>>><<><<<>><>>><<<>>><<>>>><><>><<<>>>><<<><>>>><<<>>><<<>><<>>><>><>>>><<<<>>>><<><><<<<>>><>><<<<><>><<<>>>><<<<>>><<<<>>><<>><><<<<>><<<<>>>><<<<>>><<<>>>><<<<>>><<<<>>><<<>><>><<>>><<<>><>>><<><<<>>><>>><<<><<>>><>><<<<><<<>>><>><<<<>>><><>>>><<>>>><<<>><<<>>>><<<<><<>><>><>>>><><<<<><<><<><<<>>><><<<<>><<>><<<>>>><<>>><<<>><>><>>>><<>>>><>>>><>><>>>><>>><>><<<<>><<<<>>>><<<><<<><<<<>><>>><<>><<<<>><<<<>>><<<<>>><<<>>>><<<<>><<<>><<<><<<><<<<>>>><<<><<>>><<<>>><<><<<<>><<>>><><<<<>><><<<>>>><<<>>>><<<<>>>><><<>>><><><<>><>><>><<<>>><>><<<>><<<<><<<<>>>><<<>>><>>><>>>><<><<>>>><>>><><>><<>>>><<<>><<<<>><>>>><>>><<<<>>><<>>>><><<<>>><>>><>>><<<<>>>><<>><<<>>>><<>><>>>><<>><<>>><<<<>>>><>>><>>>><<<<>>><<<<>><>>>><<<>><><<<<>>>><<>>><<><<><><<<>>>><<>>>><<>>><>>><<<>>><>>><<<>>>><<<>><<<<>><<>>>><<><<<><<<>><<<<>>>><<<>><<>>><<<<>>><<<>>><<<<><<><>>>><<<<>><><<><<<>><<<<><<<>><<<>>><<>><<<<>>><<<><<<<>><<<<>>><><<<>>><<<<>>><<>>><>>>><<>>><<>><<<><<<<>><<>>>><<<<>>><<<<>>>><<<>><<<<>>>><<<<>>><<<>>><>><<><<<<><<<<>>>><<<><<><<<<><<<<>><>><<<>><<><<<><<><<<>><<<<><>>>><<<>>>><>><<>>>><>>>><>>>><<<>><<<>><<<<>>>><>>>><<<>>><<>>>><<<>>><<>>>><<<<>>>><><>>><><<>>><<<<>>>><>>>><<<>>>><<>>><<>><<<>>><<<<>><<<<>><<>><<<>><<>>>><>>><><<<<><><>>>><<<>>>><<<<>>><<>><>><<<<><>>><<<<>>>><<<<>><>>><<<>>><>>>><><>><>>><><>>>><><>>><<>><<><<<<>><<<<><<<<><<>><<<<><<<>><<<>>>><><<<<>>><<><<<<>>>><>>>><>>><<<>>><<<>>>><<>>><<><>>><<<><>><<<<><<<<><><<<>><><<>>>><<<>><<><<<<>><<>>><>><<>>><>><<<><>>><<>>>><<<<>><>>>><<<>>><<<>>><<>>>><<<>>><<<><>><<>>>><<>><>><<<<>><<<>>>><><<<<>>><>>><<>>><<<<>><<<>>><<>>>><<<>>>><><<<>><<>>>><<<>>><<<<><<<<>><<<<>><<<<>><<>>><<<>><<<>>>><<<<>>><<>>><<<<>>><<<>><<<<><><>><<>>>><<>>><<<<><<<><<<<><<<><><<<>>><>>>><<<<>>>><<><<<>>>><<><<<><><<>><<<<>>><<<><<<>><<<>>><>>><<<<>>><>><<>>>><<<<><<<>><<><>>><<<<>>>><><<>><>>>><<<>>>><<<<>>>><<<>>>><>>><<<>>><<<<><<<<>>>><<<<>>><<><<<>><<<<>><<<>>>><<<<>><<>>><>>><<<<><><<<>><>><>><<<>><<<<>>>><<>><>><<<>>><><<<<>><<>><<<><<>>>><><<<><<>><>><<>>>><<<<>><>>><<<<><<<><<>><<<<>><<<<>>>><<>>><<<<>>><<<>>>><<>>><<<><>>>><<<<>><<<<>><<>>>><<<>>>><<>><<<>>><>><<<<>>>><>><<<<><<<>><<<<>><>><>>>><<<>>>><><><>>>><<<<>>><<<>>><<<<><<>><<><<>>>><<<><<<<>>>><<>>>><<>>><<>><<<<>><<<<>>><>>><>>>><>><<<>>>><<>><<<><<<<><<<>>><<<>>>><<<><<>><<>>><><<<<>><<><<<<><<<>>>><<<<>><<>><<><<<>>><<<<>><<>>><<<>>><<<>><<<>>>><>>>><<>>><<<<>>><>>>><<<><<<>>><<<>><>>><>><<<>>><>>><<<>>><<<<><<<><<<<>><<<<>><<>>><>>><<<<><<>>>><<<<><<>>>><>>>><>>><<>>>><<>>>><<<<><<>><<>><<><>><><<<<>>><>>><<>><<<<>>>><<<<>><>><<<<>><<<>>><<<<>><<>><<>>><<<>>><<<<>><<<<><>><<<<>>><>>>><>><<>>>><>>>><<<<>><<>>><<>>><<>>>><><<><<<<>><<<<><<>>><>>><<<<><<<<>>><<<<>><<<>><<>>>><<<<><<>>>><<<>>>><<<<>>>><<<<><<<<>><<<<>>>><<<>>>><>><>>><<<<>><<<>><<<>><<>><<<<><>><<>><><<<<><<<<>>><<><<<<>><<<>>>><<<><<<<><<>>>><>>><>>><<<>><<<>>>><>>>><<>>><<<<>>><<>><><<<>>>><<><>>>><>><>>>><<<>>>><>>><<>>><>><>>><<<<><<>><<>><>>><>>><<<>><<><<>><><<>>><<>><<>><<<>><<<>>>><>>>><><<<<>>>><<<><<<>>><>><<<<><<<<>>><>>>><<>>>><<>>><>>>><>>>><<<<>>>><<>>><<<<>>><<<>><>>><<<<>>><>><<>>>><<>><<>><><><<<>>>><><<<>>><<<>><<>>>><<>>>><<>>><<>>><<>>><<<><<<<>><<<<>><<<<>><<><<<<>>>><<><<<<>>>><<<<>><<<>>>><<<>><<<<><<<<>>>><<<>><>>>><><>>>><<<<>><<<>>>><<<><<<>>>><<<<><<<>><><<>>><<<<><<>><<<<>>><<<<><<<<>><<<<><<><<<<>><><<<>>><>>>><<<<>><<<>>><<>><<<><>>>><>>><<<<>><>>>><<<><<>>>><<<<>>><<<>>><<><<<<>>>><<<>>><<>>><>>>><<<>>>><>>><<<<><>>>><<>>><<<><>>>><>>>><<<><<><<>><<<<><>>><><<<>>><<>>>><<<<>>><>><<<>><<<>>><<>>><<>>><<<>><<<<>><<<>>><<<>><<<><<<<>>><>>><<<<><<<><<<>>><>>><<><<<<>><<<<><<>><<>>>><<<><>>>><<>>>><<<><>><><<<<><<<><>>><<<<>><>><<<><<><<<<>>><>>><<<>><<<>><>>><<><<<<>>>><<>>>><><><>>>><<>>><<>>><<<<>><<><<<<>><>>><><<<<>>><<<<><<<<>>><<<>>><<<<>>>><<>>>><<<<>><<<>>>><<>>><<<<>><<><<<<><<<><<<><<<<>>><<<<>>>><<>>><<<<>><>><<>><<>>>><>>><<<<><<<<>>><<<>><<><<>>><>>><<<><>>><>>><><>><<<>>>><<<<>>><>><<<><<<>>>><<><<<<>>><<<>>>><<<><<>>>><<<<>>><<><<>>><<>><<>>>><<>>>><<<>>><<<<>><<>><<<<><<<>>><>>>><<>>><>>><<>>><<<>>>><>>>><>>>><<<><>>><<<<>><<<>>><<<>>>><<<<>>>><>>><<<<>>>><<<>>>><>>><<>><<<>>>><<<>><<<>>>><><><>>><<><>>><>>>><>>>><<<<>>><<<><<>>>><<<>>>><<<><>><>>><<<>>>><>><<>><>><<<>>>><<<<>>><<<<><<<<>>>><<<<>>><<>>>><<<<>>>><<<<>><<<>><><<<>>><<<<>>><>>>><<<<>><<>><>><<>>><>>>><<<<><<<><<>>><<<>><<<<>>><<>>><<<>>><<<<><<<>>>><<<>>>><<<>>><>>>><<>>>><<>><<><<>>><><<>><<<<>>>><<<><>>>><<<>><<<<>>>><>>><<<><>>><<<<>>><><<>>>><<<<><<<<>><>>><<<><>>>><<<<>><>>>><<<><<<>>>><<<>>><<<><<<>><<<<>>>><<<>><<<<><<<><<><<<<>>><<<<>>>><<><<<<>>>><><<<<>>>><<<>>><<<>>><<<<><>><<<<>><<<><<<<>>><<><<<<><<>>><<<><<<<><>>><<<<><<<>>>><<<<>>>><<>>>><>><<<<>>><><<<<>>>><<<<>><<<>><<<><<>>><<>>>><>>><<>><<<>><<>>><>>>><<>>>><>>><<<<>><><>>>><<><<<<>>>><<<<>>>><<>><>>><<<>>><<>>>><>>>><>>>><<<<>><<<<>><<<<><<<>>>><>>>><<<<>>>><>><<>>>><<<<>>><<<>>><>><<><<<>>>><>>><<>><<<><>><<<<>><<><>>><<<<><<<>><>>><<<>>>><<>>>><<<<>>><<>><>>><<<<>><<>><<<<>>><><<>>><<><<<<><<<<>><>>><<><<<><<<<>><>>><<>>>><<<>><<<>><<<>>><<<>>>><>>>><<>>><<<>>><>><>>>><>>>><<<>><>>><<<>><<>><>><<<<>>><>>><<<><<<>>>><<<>><<<>>><>>><<<><>>>><<<<><>><<>><<<<><<<>><<>>><<<><>>><<<><<<<><<<<><>><<>>>><<<<>>><<<<>><<<<>>><<<<><<><<<>>><><<>><<>>>><<>>><><<<<><<<<>>><><<<>>>><<<<>>>><<<<>>>><<>><<>><<>><<<>><>>><>><<<<>><<><<<>>><>>><><>>><<<>>>><<>>><>><<<>>>><<<>><<><><<<><>><<<<>>><<<<>><<<<>><<<>>><<<<>>><<<<>>>><<<>>><<<<>><<<<><><<<>>><<<><<><<><<<>><<>>><<>><<><<>>>><>><<<<>>>><>>>><<<<>>><<<<>>><>><<<><<<>>>><<<<>><<<<><<><<<<>>>><<<<>><<<<>>>><<<<>><<<>><<>><<<<>><>><<>>>><<<<><<<><>>><>><<<>>>><><<<><>>>><<<>>><<<>><<<><<<>><<><>>>><<><>>><>><<<>>><<<<>><<><<>><<<<>><<<<><<<>>>><<<<>><<<>>>><>>><<<>><<>>>><<><><<<<><<<<>>>><<<>><<<<>><>>>><<><><<>>>><<<><<<<>><>><>>><<><<<<>>>><<>><<<<><<>>><<<>>><<<>>><<<>>>><>><<<>>>><<<>>>><><<<<>>>><>><<<<>><<<<>>>><<>>><<<>>>><<>><<><<<>>><<>>>><<<<>><<<<>>><>>>><<<>>><<>>>><<>>><><>><<<<>><<<>>>><<>><<<>><<<>>><<<>><>><><<<<>>><<<><<>>>><<>>>><<>><<<><<<><<<<><<><>>>><<<>>>><<<<>>><>><<>>>><>><<<>>>><<<>><<>>>><<<<>>><<<><><<>>><<>><<<>>><<<<>><<>>>><<<><<<<><<>>>><<>>><<<<><<<<><<<>>><<>>><>><<><<><<>>><><>>>><<<>><<>>>><>>>><<<<>><><<<<>><<<<>>>><<>>>><<<<><<<>>><<>>><<><<<<>><>><<><<><<><<<><<<<><>><<<>>>><<<<>>>><<<><>>>><<>>><><>>><<<>>><<<><<>>><<><><<><<<<><<<<>>>><><><<<<>>><>><<>>>><<<<>>>><<<>>><<<><<><<<<><<<<>>><<<<>>>><<<>><<<<>>>><<><<<>><><>>>><<<>>>><<<>>>><<><<<>><>>>><<<><>><<<<><<<<>>><<<<>>>><<><<<>>>><><><<<<><<<<><>><<><>>>><<<>><<>><"
# JETS = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
assert set(JETS) == set(["<", ">"]), "bad character among the jets"
jet_index = 0
shape_ind = 0
NB_JETS = len(JETS)
CHAMBER_WIDTH = 7
chamber = np.ones(shape=(1, CHAMBER_WIDTH), dtype=int)  # build the floor

shapes = [
    """
          ..####.
          .......
          .......
          .......""",
    """
          ...#...
          ..###..
          ...#...
          .......
          .......
          .......""",
    """
          ....#..
          ....#..
          ..###..
          .......
          .......
          .......""",
    """
          ..#....
          ..#....
          ..#....
          ..#....
          .......
          .......
          .......""",
    """
          ..##...
          ..##...
          .......
          .......
          .......""",
]

str_to_bin_trans = str.maketrans(".#", "01")
shapes_clean = [
    [
        stripped.translate(str_to_bin_trans)
        for row in shape_str.splitlines()
        if (stripped := row.strip())
    ]
    for shape_str in shapes
]
shapes_binary = [[list(map(int, row)) for row in shape] for shape in shapes_clean]
shapes_to_append = dict(enumerate(map(np.array, shapes_binary)))
nb_shapes = len(shapes_to_append)
shapes_coord = [
    list(zip(np.where(shape)[0], np.where(shape)[1]))
    for shape in shapes_to_append.values()
]  # provides the indices of the 1s in the 5 unique shapes (used to track shape position and move shape) in their starting position


def find_highest_rock() -> int:
    """Finds and returns the row number of the highest rock in the chamber (or the floor if no rock is found)"""
    for i in range(chamber.shape[0]):
        if chamber[i].sum():
            return i


def jet_effect() -> None:
    """Implements the behaviour of the hot gas jet, and when possible moves the current shape to the right or left

    Args:
        shape (list[tuple[int, int]]): a list of tuples describing the coordinates of each rock of the current shape
    """
    global chamber, jet_index, shape
    if JETS[jet_index] == "<":
        leftmost_rocks = find_leftmost_rocks(shape)
        if all(
            1 <= coord[1] and chamber[coord[0], coord[1] - 1] == 0
            for coord in leftmost_rocks
        ):
            shape = sorted(
                shape, key=lambda x: x[1]
            )  # I need to sort the coordinates so that I move the blocks in the correct order
            for coord in shape:
                chamber[coord[0], coord[1] - 1] = 1  # move rock to the left
                chamber[coord] = 0  # update previous rock position
            shape = [(coord[0], coord[1] - 1) for coord in shape]
    else:
        rightmost_rocks = find_rightmost_rocks(shape)
        if all(
            coord[1] <= CHAMBER_WIDTH - 2 and chamber[coord[0], coord[1] + 1] == 0
            for coord in rightmost_rocks
        ):
            shape = sorted(
                shape, key=lambda x: x[1], reverse=True
            )  # I need to sort the coordinates so that I move the blocks in the correct order
            for coord in shape:
                chamber[coord[0], coord[1] + 1] = 1  # move rock to the right
                chamber[coord] = 0  # update previous rock position
            shape = [(coord[0], coord[1] + 1) for coord in shape]
    jet_index = (
        jet_index + 1
    ) % NB_JETS  # increment the jet index regardless of whether it actually moved the shape


def find_downmost_rocks(shape: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """A utility function that retrieves the rocks of a shape that are relevant when testing if the shape can move down
    These relevant rocks are the lowest rocks of each column occupied by the shape

    Args:
        shape (list[tuple[int, int]]): the coords of each rock of the shape

    Returns:
        list[tuple[int, int]]: the relevant rocks
    """
    df = pd.DataFrame(
        {"x": [elem[0] for elem in shape], "y": [elem[1] for elem in shape]}
    )
    df = df.sort_values(by="x", ascending=False).drop_duplicates(subset=["y"])
    df["coord"] = df.apply(lambda row: (row.x, row.y), axis=1)
    return df.coord.tolist()


def find_leftmost_rocks(shape: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """A utility function that retrieves the rocks of a shape that are relevant when testing if the shape can move left
    These relevant rocks are the leftmost rocks of each row occupied by the shape

    Args:
        shape (list[tuple[int, int]]): the coords of each rock of the shape

    Returns:
        list[tuple[int, int]]: the relevant rocks
    """
    df = pd.DataFrame(
        {"x": [elem[0] for elem in shape], "y": [elem[1] for elem in shape]}
    )
    df = df.sort_values(by="y").drop_duplicates(subset=["x"])
    df["coord"] = df.apply(lambda row: (row.x, row.y), axis=1)
    return df.coord.tolist()


def find_rightmost_rocks(shape: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """A utility function that retrieves the rocks of a shape that are relevant when testing if the shape can move right
    These relevant rocks are the rightmost rocks of each row occupied by the shape

    Args:
        shape (list[tuple[int, int]]): the coords of each rock of the shape

    Returns:
        list[tuple[int, int]]: the relevant rocks
    """
    df = pd.DataFrame(
        {"x": [elem[0] for elem in shape], "y": [elem[1] for elem in shape]}
    )
    df = df.sort_values(by="y", ascending=False).drop_duplicates(subset=["x"])
    df["coord"] = df.apply(lambda row: (row.x, row.y), axis=1)
    return df.coord.tolist()


def move_down() -> bool:
    global chamber, shape
    downmost_rocks = find_downmost_rocks(shape)
    if all(chamber[coord[0] + 1, coord[1]] == 0 for coord in downmost_rocks):
        shape = sorted(shape, key=lambda x: x[0], reverse=True)
        for coord in shape:
            chamber[coord[0] + 1, coord[1]] = 1  # move rock down
            chamber[coord] = 0  # update previous rock position
        shape = [(coord[0] + 1, coord[1]) for coord in shape]
        return True
    # print('REST')
    return False


def pretty_print(chamber: np.array) -> None:
    for row in chamber[:-1]:  # don't print the floor
        print(*row)
    print("\n")


def simulate_shape_fall() -> None:
    global jet_index, shape_ind, shape, chamber
    current_shape = shapes_to_append[shape_ind]
    shape = shapes_coord[shape_ind]
    shape_ind = (shape_ind + 1) % nb_shapes
    chamber = chamber[find_highest_rock() :]
    chamber = np.vstack((current_shape, chamber))
    can_move_down = True
    while can_move_down:
        jet_effect()
        # print(chamber, 'after jet effect', end='\n'*2)
        can_move_down = move_down()
        # print(chamber, 'after move down',end='\n'*2)
    # print(chamber,end='\n\n')


def simulate_shapes_falls(nb_times: int = 2022) -> None:
    for _ in tqdm(range(nb_times)):
        simulate_shape_fall()


# How many units tall will the tower of rocks be after 2022 rocks have stopped falling?
# uncomment the next 2 lines to solve part 1 (with the "naive" approach)
# simulate_shapes_falls()
# print(chamber.shape[0] - find_highest_rock() - 1)

# part 2
NB_ITERATIONS = 1_000_000_000_000
# obviously, I'm not gonna run that many simulations
# I think there should be a convergence at some point, in other words a pattern that repeats itself

# pr trouver le pattern, je dois identifier quand je m'apprête à faire tomber le même shape , que je suis
# au même jets_index, et quand x lignes en dessous, j'ai les mêmes rocks at rest (aux mêmes coords)

# je choisis x = 50 mais il serait intéressant d'étudier la vraie valeur

data = []
tower_heights = []
pattern_found = False
i = 0
while not pattern_found:
    iteration_data = (jet_index, shape_ind, chamber[:50].flatten().tolist())
    simulate_shape_fall()
    if iteration_data in data:
        print(f"found a pattern after {i} iterations: {iteration_data=}")
        break
    data.append(iteration_data)
    tower_heights.append(chamber.shape[0] - find_highest_rock() - 1)
    i += 1


init_uncomplete_tower_height = tower_heights[data.index(iteration_data) - 1]
repeated_tower_height = tower_heights[-1] - init_uncomplete_tower_height
len_uncomplete_tower = data.index(iteration_data)
print(f"{len_uncomplete_tower=}")
len_repeated_tower = len(tower_heights) - len_uncomplete_tower
print(f"{len_repeated_tower=}")
partial_answer = init_uncomplete_tower_height + repeated_tower_height * (
    (NB_ITERATIONS - len_uncomplete_tower) // len_repeated_tower
)
nb_iter_so_far = len_uncomplete_tower + len_repeated_tower * (
    (NB_ITERATIONS - len_uncomplete_tower) // len_repeated_tower
)
remaining_iter = (NB_ITERATIONS - len_uncomplete_tower) % len_repeated_tower
# we've added the 1st bit (incomplete tower) + the repeated towers, now let's add the final, incomplete tower
ending_uncomplete_tower_height = (
    tower_heights[len_uncomplete_tower - 1 + remaining_iter]
    - tower_heights[len_uncomplete_tower - 1]
)
answer = partial_answer + ending_uncomplete_tower_height

print(answer)
