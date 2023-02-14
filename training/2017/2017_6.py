"Basic looping, divmod understanding and Python comprehensions skills are required to solve this one"
INPUT = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"
INPUT_TEST = "0 2 7 0"


def spread_blocks(banks: list[int] | tuple[int]) -> tuple[int]:
    """Shares the blocks across all banks, one by one

    Args:
        banks (list[int] | tuple[int]): _description_

    Returns:
        tuple[int]: _description_
    """
    max_nb_blocks = max(banks)
    nb_elems = len(banks)
    sharing_block_ind = banks.index(max_nb_blocks)
    nb_given, remains = divmod(max_nb_blocks, nb_elems)
    banks = [
        banks[i] + nb_given if i != sharing_block_ind else nb_given
        for i in range(nb_elems)
    ]
    j = (sharing_block_ind + 1) % nb_elems
    while remains:
        banks[j] += 1
        j = (j + 1) % nb_elems
        remains -= 1
    return tuple(banks)


def solve_part1(input_: str) -> int:
    """Loops till it finds the solutoin to part 1

    Args:
        input_ (str): _description_

    Returns:
        int: _description_
    """
    banks = tuple(map(int, input_.split()))
    seen = {banks}
    nb_iter = 0
    print(f"initial: {banks=}")
    while True:
        nb_iter += 1
        if (banks := spread_blocks(banks)) in seen:
            print(f"part 1: {nb_iter=}")
            return nb_iter
        seen.add(banks)


assert solve_part1(INPUT_TEST) == 5
solve_part1(INPUT)

# part 2
def solve_part2(input_: str) -> int:
    """Loops till it solves part 2

    Args:
        input_ (str): _description_

    Returns:
        int: _description_
    """
    banks = tuple(map(int, input_.split()))
    seen = [banks]  # membership tests will take longer but that's OK here
    nb_iter = 0
    while True:
        nb_iter += 1
        if (banks := spread_blocks(banks)) in seen:
            print(f"part 2: {nb_iter - seen.index(banks)}")
            return nb_iter - seen.index(banks)
        seen.append(banks)


assert solve_part2(INPUT_TEST) == 4
solve_part2(INPUT)
