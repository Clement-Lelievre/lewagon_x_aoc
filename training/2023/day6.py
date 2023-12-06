"""AoC 2023 day 6: https://adventofcode.com/2023/day/6
"""
from functools import reduce
from tqdm import tqdm
ACTUAL_DATA = {46: 358, 68: 1054, 98: 1807, 66: 1080}
TEST_DATA = {7: 9, 15: 40, 30: 200}
TEST_DATA_P2 = {71530: 940200}

ACTUAL_DATA_P2 = {46_689_866: 358_105_418_071_080}


def main_p1(race_data: dict[int, int]) -> int:
    nb_times = []
    for time_, record_dist in race_data.items():
        nb = 0
        for press_time in range(1, time_):
            achieved_dist = (time_ - press_time) * press_time
            if achieved_dist > record_dist:
                nb += 1
        if nb:
            nb_times.append(nb)
    answer = reduce(lambda x, y: x * y, nb_times)
    print(f"part1: {answer=}")
    return answer


def main_p2(race_data: dict[int, int]) -> int:
    nb_times = []
    for time_, record_dist in race_data.items():
        nb = 0
        for press_time in tqdm(range(1, time_)):
            achieved_dist = (time_ - press_time) * press_time
            if achieved_dist > record_dist:
                nb += 1
        if nb:
            nb_times.append(nb)
    answer = reduce(lambda x, y: x * y, nb_times)
    print(f"part2: {answer=}")
    return answer


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 288, "should be 288 for the test input p1"
    main_p1(ACTUAL_DATA)
    assert main_p2(TEST_DATA_P2) == 71503, "should be 71503 for the test input p2"
    main_p2(ACTUAL_DATA_P2)
