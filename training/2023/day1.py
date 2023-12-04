"""AoC day 1 2023"""
import argparse
import re

TEST_DATA = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST_DATA_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

# part 1


def main_p1(text: str) -> int:
    s = 0
    for line in text.splitlines():
        digits = [char for char in line if char.isdigit()]
        if len(digits) >= 1:
            s += int(digits[0] + digits[-1])
    print(f"Solution p1: {s}")
    return s


# part 2


def main_p2(text: str) -> int:
    s = 0
    SEQ = {str(k): str(k) for k in range(1, 10)} | {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in text.splitlines():
        lowest_ind = float("inf")
        highest_ind = -1
        for seq, dig in SEQ.items():
            matches_ind = [match_.start(0) for match_ in re.finditer(seq, line)]
            if matches_ind:
                if matches_ind[0] < lowest_ind:
                    digit_left = dig
                    lowest_ind = matches_ind[0]
                if matches_ind[-1] > highest_ind:
                    digit_right = dig
                    highest_ind = matches_ind[-1]
        s += int(digit_left + digit_right)
    print(f"Solution p2: {s}")
    return s


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 142, "should be 142 for the test input p1"
    assert main_p2(TEST_DATA_2) == 281, "should be 281 for the test input p2"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input file", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    main_p2(text)
