"""AoC 2023 day 9: https://adventofcode.com/2023/day/9

Usage: python day9.py <input_filepath>
"""
import argparse

TEST_DATA = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def main_p1(text: str) -> int:
    lines = [
        stripped_line for line in text.splitlines() if (stripped_line := line.strip())
    ]
    answer = sum(map(process_one_line_p1, lines))
    print(f"Part 1 answer: {answer}")
    return answer


def process_one_line_p1(line: str) -> int:
    line = [int(nb) for nb in line.split()]
    last_line_items = [line[-1]]
    while sum(line):
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        last_line_items.append(line[-1])
    for i in range(len(last_line_items) - 2, -1, -1):
        last_line_items[i] += last_line_items[i + 1]
    return last_line_items[0]


def main_p2(text: str) -> int:
    lines = [
        stripped_line for line in text.splitlines() if (stripped_line := line.strip())
    ]
    answer = sum(map(process_one_line_p2, lines))
    print(f"Part 2 answer: {answer}")
    return answer


def process_one_line_p2(line: str) -> int:
    line = [int(nb) for nb in line.split()]
    first_line_items = [line[0]]
    while sum(line):
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        first_line_items.append(line[0])
    for i in range(len(first_line_items) - 2, -1, -1):
        first_line_items[i] -= first_line_items[i + 1]
    return first_line_items[0]


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 114, "should be 114 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    assert main_p2(TEST_DATA) == 2, "should be 2 for the test input p2"
    main_p2(text)
