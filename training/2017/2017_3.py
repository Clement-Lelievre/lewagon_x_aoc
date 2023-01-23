import numpy as np

INPUT = 361527

# instead of building the whole grid let's try come up with a more efficient solution

# 2 utility functions
def find_n(input_: int) -> tuple[int, bool] | None:
    # could implement faster search like binary search to go faster, but this scales well to the input size already
    for nb in range(1, 1_000, 2):  # odd numbers
        if input_ == nb**2:
            return nb + 2, True  # input_ is a square
        if input_ < nb**2:
            return nb, False  # input_ is not a square


manhattan_dist = lambda x, y: abs(x) + abs(y)

# main function


def nb_steps(input_: int, verbose: bool = True) -> int | None:
    if (res := find_n(input_)) is not None:
        n, is_a_square = res
    mapping_odd_nbs = dict(
        zip((2 * k + 1 for k in range(1, n // 2 + 1)), range(1, n + 1))
    )
    if is_a_square:  # edge case: the input is the square of an odd number
        return manhattan_dist(*(mapping_odd_nbs[n - 2], -mapping_odd_nbs[n - 2]))
    coord = [
        mapping_odd_nbs[n - 2] + 1,
        -mapping_odd_nbs[n - 2],
    ]  # placing the cursor on the edge of the spiral (on the right edge)
    current_nb = (n - 2) ** 2 + 1
    # the below could be refactored, but like this it is very intuitive
    if verbose:
        print("Going up")
    for _ in range(n - 2):  # going up the spiral, on the rigth edge
        coord[1] += 1
        current_nb += 1
        if current_nb == input_:
            return manhattan_dist(*coord)
    if verbose:
        print("Going left")
    for _ in range(n - 1):  # going to the left, on the top edge
        coord[0] -= 1
        current_nb += 1
        if current_nb == input_:
            return manhattan_dist(*coord)
    if verbose:
        print("Going down")
    for _ in range(n - 1):  # going down, on the left edge
        coord[1] -= 1
        current_nb += 1
        if current_nb == input_:
            return manhattan_dist(*coord)
    if verbose:
        print("Going right")
    for _ in range(n - 1):  # going right, on the bottom edge
        coord[0] += 1
        current_nb += 1
        if current_nb == input_:
            return manhattan_dist(*coord)


# print(nb_steps(INPUT))

# part 2
# this time we'll build the full grid till we write the first number that exceeds our input number

mapping_odd_nbs = dict(
    zip(range(1, 10_000 + 1), (2 * k - 1 for k in range(1, 10_000 // 2 + 1)))
)


def make_outside_square(
    grid: np.array, from_square: tuple[int], input_=INPUT
) -> int | tuple[int, int]:
    """Writes inplace the memory values on an outside square, starting from the square `from_square`

    Args:
        grid (np.array): the grid
    Returns:
        int | tuple[int, int]: a tuple of coordinates of the latest square processed, if the decisive value hasn't been reached yet, else the decisive value (the one that is greater than the input)"""
    x, y = from_square
    y += 1  # move one step to the right to initiate a new spiral
    grid[x, y] = grid[x - 1 : x + 2, y - 1].sum()
    nb_iter = mapping_odd_nbs[y - grid.shape[1] // 2]
    for _ in range(1, nb_iter + 1):  # moving up
        x -= 1
        grid[x, y] = (s := grid[x - 1 : x + 2, y - 1].sum() + grid[x + 1, y])
        if s > input_:
            return s
    for _ in range(1, nb_iter + 2):  # moving left
        y -= 1
        grid[x, y] = (s := grid[x + 1, y - 1 : y + 2].sum() + grid[x, y + 1])
        if s > input_:
            return s
    for _ in range(1, nb_iter + 2):  # moving down
        x += 1
        grid[x, y] = (s := grid[x - 1 : x + 2, y + 1].sum() + grid[x - 1, y])
        if s > input_:
            return s
    for _ in range(1, nb_iter + 2):  # moving right, closing the spiral
        y += 1
        grid[x, y] = (s := grid[x - 1, y - 1 : y + 2].sum() + grid[x, y - 1])
        if s > input_:
            return s
    return (
        x,
        y,
    )  # if no value has been returned, it means we haven't written a value larger than the input yet, and we return x, y which will be the starting point of the next iteration


GRID_SIZE = (
    1_001,
    1_001,
)  # an arbitrary size. Judging by the growth rate from the example grid provided, it should be enough

grid = np.zeros(GRID_SIZE, dtype=np.int32)
center_point = grid.shape[0] // 2, grid.shape[1] // 2
grid[center_point] = 1  # assign central value
start_from = center_point

while isinstance(
    (compute := make_outside_square(grid, start_from, input_=INPUT)), tuple
):
    start_from = compute

print(compute)
