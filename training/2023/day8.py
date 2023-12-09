"""AoC 2023 day 8: https://adventofcode.com/2023/day/8
"""
import argparse

TEST_DATA_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST_DATA_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def main_p1(text: str) -> int:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    directions = [0 if char == "L" else 1 for char in lines[0]]
    direction_ind = 0
    current_label = "AAA"
    nb_steps = 0
    labels_dict: dict[str, list[str]] = {
        line[:3]: [line[7:10], line[12:15]] for line in lines[1:]
    }
    while current_label != "ZZZ":
        current_label = labels_dict[current_label][directions[direction_ind]]
        direction_ind = (direction_ind + 1) % len(directions)
        nb_steps += 1
    print(f"part 1: {nb_steps=}")
    return nb_steps


if __name__ == "__main__":
    assert main_p1(TEST_DATA_1) == 2, "should be 2 for the test input p1"
    assert main_p1(TEST_DATA_2) == 6, "should be 6 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    # assert main_p2(TEST_DATA) == 46, "should be 46 for the test input p2"
    # main_p2(text)
