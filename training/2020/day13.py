import logging

logging.basicConfig(level=logging.INFO)

TEST_INPUT = """939
7,13,x,x,59,x,31,19"""

INPUT = """1002461
29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,521,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,601,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19
"""


def process_input(input_: str):
    rows = [row for row in input_.splitlines() if row.strip()]
    return int(rows[0]), list(
        map(int, (elem for elem in rows[1].split(",") if elem.isdigit()))
    )


def solve_p1(input_: str) -> int:
    minimal_time, bus_ids = process_input(input_)

    def get_waiting_time(time_interval: int) -> int:
        return time_interval - minimal_time % time_interval

    answer = min(bus_ids, key=get_waiting_time) * min(map(get_waiting_time, bus_ids))
    logging.info(answer)
    return answer


# part 2


def process_input_p2(input_: str):
    """the first row is no longer used
    Args:
        input_ (str):comma-spearated list of ints or 'x

    Returns:
        _type_: _description_
    """
    return [
        (ind, int(val)) for ind, val in enumerate(input_.split(",")) if val.isdigit()
    ]


def solve_p2_naive(input_: str) -> int:
    """naive implementation, incrementing by the first bus id each iteration;
    too slow for my input"""
    bus_data = process_input_p2(input_)
    first_bus_id = bus_data[0][1]
    nb = first_bus_id
    while True:
        if all((nb + ind) % bus_id == 0 for ind, bus_id in bus_data):
            break
        nb += first_bus_id
    logging.info(nb)
    return nb


def solve_p2(input_: str) -> int:
    "this time we increment the step much more whenever we can"
    bus_data = process_input_p2(input_)
    step = t = 1
    for delay, bus_id in bus_data:
        while (t + delay) % bus_id:
            t += step
        step *= bus_id
    logging.info(f"{input_}: {t}")
    return t


if __name__ == "__main__":
    # part 1
    assert solve_p1(TEST_INPUT) == 295
    solve_p1(INPUT)
    # part 2
    # for part 2 I have to thanks Peter Norvig for his reasoning, that helped me a lot!
    assert solve_p2_naive("7,13,x,x,59,x,31,19") == 1068781
    assert solve_p2_naive("17,x,13,19") == 3417
    assert solve_p2_naive("67,7,59,61") == 754018
    assert solve_p2_naive("67,x,7,59,61") == 779210
    assert solve_p2_naive("1789,37,47,1889") == 1202161486

    assert solve_p2("7,13,x,x,59,x,31,19") == 1068781
    assert solve_p2("17,x,13,19") == 3417
    assert solve_p2("67,7,59,61") == 754018
    assert solve_p2("67,x,7,59,61") == 779210
    assert solve_p2("1789,37,47,1889") == 1202161486

    solve_p2(INPUT.splitlines()[1])
