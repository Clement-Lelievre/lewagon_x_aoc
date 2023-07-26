"""https://adventofcode.com/2020/day/23"""

TEST_INPUT = "389125467"
REAL_INPUT = "653427918"


# The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle;
# cup spacing is adjusted as necessary to maintain the circle.
# The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
# If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't
# just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
# The crab places the cups it just picked up so that they are immediately clockwise of the destination cup.
# They keep the same order as when they were picked up.
# The crab selects a new current cup: the cup which is immediately clockwise of the current cup.


# part 1
def solve_p1(input_: str, nb_moves: int = 100) -> str:
    """Naive implementation

    Args:
        input_ (str): _description_
        nb_moves (int, optional): _description_. Defaults to 100.

    Returns:
        str: _description_
    """
    cups = [int(char) for char in input_]
    current = cups[0]
    nb_cups = len(cups)
    max_val = max(cups)
    for _ in range(nb_moves):
        to_remove = [cups[(cups.index(current) + i) % nb_cups] for i in range(1, 4)]
        destination_val = current - 1 if current - 1 else max_val
        if destination_val in to_remove:
            while destination_val in to_remove:
                destination_val = (
                    destination_val - 1 if destination_val - 1 else max_val
                )
        for val in to_remove:
            cups.remove(val)
        for ind, val in enumerate(to_remove):
            cups.insert((cups.index(destination_val) + ind + 1) % nb_cups, val)
        current = cups[(cups.index(current) + 1) % nb_cups]
    print(
        ans := "".join(map(str, cups[cups.index(1) + 1 :]))
        + "".join(map(str, cups[: cups.index(1)]))
    )
    return ans


# part 2 will likely require to find the point where a state has already been seen, and possibly some optimization
# yet unsolved


def solve_p2(input_: str, nb_moves: int = 10_000_000, nb_cups: int = 1_000_000) -> int:
    seen = set()  # tracks (ordered_cups, current, destination, to_remove)
    cups = [int(char) for char in input_]
    cups.extend(range(max(cups) + 1, nb_cups + 1))
    current = cups[0]
    max_val = max(cups)
    for i in range(nb_moves):
        to_remove = [cups[(cups.index(current) + i) % nb_cups] for i in range(1, 4)]
        destination_val = current - 1 if current - 1 else max_val
        if destination_val in to_remove:
            while destination_val in to_remove:
                destination_val = (
                    destination_val - 1 if destination_val - 1 else max_val
                )
        state = (
            tuple(cups[cups.index(1) :] + cups[(cups.index(1) + 1) % nb_cups :]),
            current,
            destination_val,
            tuple(to_remove),
        )
        if state in seen:
            print(i)
            break
        seen.add(state)
        for val in to_remove:
            cups.remove(val)
        for ind, val in enumerate(to_remove):
            cups.insert((cups.index(destination_val) + ind + 1) % nb_cups, val)
        current = cups[(cups.index(current) + 1) % nb_cups]
    else:
        print("No repetition found")
    print(
        ans := "".join(map(str, cups[cups.index(1) + 1 :]))
        + "".join(map(str, cups[: cups.index(1)]))
    )
    return ans


if __name__ == "__main__":
    assert solve_p1(TEST_INPUT, nb_moves=10) == "92658374"
    assert solve_p1(TEST_INPUT, nb_moves=100) == "67384529"
    solve_p1(REAL_INPUT)
    solve_p2(REAL_INPUT)  # yet unsolved
