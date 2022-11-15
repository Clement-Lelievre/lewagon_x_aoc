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


print(nb_steps(INPUT))
