"""AoC 2023 day 12: https://adventofcode.com/2023/day/12

Usage: python day12.py <input_filepath>
"""
import argparse
import re
from itertools import combinations


TEST_DATA = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def main_p1(text: str) -> int:
    lines = [
        stripped_line for line in text.splitlines() if (stripped_line := line.strip())
    ]
    answer = 0
    for line in lines:
        seq, nbs = line.split()
        nbs = [int(nb) for nb in nbs.split(",")]
        total_nb_damaged = sum(nbs)
        nb_damaged_to_place = total_nb_damaged - seq.count("#")
        indices_question_mark = [m.start() for m in re.finditer(r"\?", seq)]
        for comb in combinations(indices_question_mark, nb_damaged_to_place):
            new_seq = list(seq)
            for index in comb:
                new_seq[index] = "#"
            new_seq = "".join(new_seq).replace("?", ".").split(".")
            groups_lens = [len(group) for group in new_seq if group]
            if groups_lens == nbs:
                answer += 1
    print(f"Answer part 1: {answer}")
    return answer


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 21
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
