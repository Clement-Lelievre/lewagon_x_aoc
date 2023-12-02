"""AoC 2023 day 2: https://adventofcode.com/2023/day/2"""
import argparse
from functools import reduce

TEST_DATA = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

BAG = {"red": 12, "green": 13, "blue": 14}


def main_p1(input_: str) -> int:
    answer = 0
    for line in input_.splitlines():
        if not line.strip():
            continue
        gid, sets = line.split(":")
        if all(
            int(items.split()[0]) <= BAG[items.split()[1]]
            for game in sets.split(";")
            for items in game.split(",")
        ):
            answer += int(gid[gid.index(" ") + 1 :])
    print(f"part 1 :{answer=}")
    return answer


def main_p2(input_: str) -> int:
    answer = 0
    for line in input_.splitlines():
        if not line.strip():
            continue
        minimum_needed = {"red": 0, "green": 0, "blue": 0}
        _, sets = line.split(":")
        for game in sets.split(";"):
            for items in game.split(","):
                nb, color = items.split()
                if int(nb) > minimum_needed[color]:
                    minimum_needed[color] = int(nb)
        game_power = reduce(lambda x, y: x * y, minimum_needed.values())
        answer += game_power
    print(f"part 2 :{answer=}")
    return answer


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 8, "should be 8 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    assert main_p2(TEST_DATA) == 2286, "should be 2286 for the test input p2"
    main_p2(text)
