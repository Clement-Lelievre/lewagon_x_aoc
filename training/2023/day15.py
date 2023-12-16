"""AoC 2023 day 15: https://adventofcode.com/2023/day/15

Usage: python day15.py <input_filepath>
"""
import argparse


def aoc_hash(seq: str) -> int:
    """Return hash of sequence."""
    val = 0
    for char in seq:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def solve_p1(text: str) -> int:
    """Solve part 1."""
    answer = sum(map(aoc_hash, text.split(",")))
    print(f"answer part 1: {answer}")
    return answer


if __name__ == "__main__":
    assert solve_p1("HASH") == 52
    assert solve_p1("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7") == 1320
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path) as f:
        text = f.read()
    solve_p1(text)
