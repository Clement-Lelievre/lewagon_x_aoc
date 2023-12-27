"""AoC 2023 day 19"""

import argparse
import re
from collections import defaultdict
from math import prod

# for part 2, I need to be able to:

# - work on ranges instead of sets due to the high number of elements
# - perform operations on sets (when applying the tests)
# - adding only new points (when adding to the answer)

TEST_DATA = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

MINI_TEST_DATA = """px{a<2:qkq,R}
qkq{A}
in{s>3999:px,R}
"""

MINI_TEST_DATA_2 = """px{a<2:qkq,R}
qkq{A}
t{x<2:A,R}
in{s>3999:px,m<2:t,R}
"""

MINI_TEST_DATA_3 = """px{a<2:qkq,R}
qkq{A}
t{x<2:A,R}
in{s>3999:px,m<2:t,v}
v{x>3999:A,R}
"""


class PartProcessor:
    def __init__(self, data: str) -> None:
        self.data = data
        self.workflows = None
        self.ops = {
            "<": int.__lt__,
            ">": int.__gt__,
        }  # maps signs to int operations
        self.categories = ["x", "m", "a", "s"]
        self.valid_ranges = set()
        self.initial_ranges = (
            range(1, 4001),
            range(1, 4001),
            range(1, 4001),
            range(1, 4001),
        )
        self.process_input()

    def process_input(self) -> None:
        lines = self.data.strip().split()
        self.workflows = defaultdict(
            list
        )  # {workflow_name: [(test1, workflow1), (test2, workflow2), ...]}
        for line in lines:
            if not line.strip():
                continue
            workflow_name = line[: line.index("{")]
            tests = line[line.index("{") + 1 : -1].split(",")
            for test in tests:
                if ":" in test:
                    self.workflows[workflow_name].append(
                        (test[: test.index(":")], test[test.index(":") + 1 :])
                    )
                else:
                    self.workflows[workflow_name].append((True, test))

    def solve_p2(self) -> int:
        self.enter_workflow(ranges=self.initial_ranges)
        answer = self.compute_answer()
        print(f"{answer=}")
        return answer

    def enter_workflow(
        self, *, ranges: tuple[range], wf_name: str = "in", ind: int = 0
    ):
        test, next_wf = self.workflows[wf_name][ind]
        # print(f"{wf_name=} {test=} {next_wf=} {ind=} {ranges=}")
        # narrow ranges by applying test, and go into workflow
        range_test_applied = self.apply_test(test=test, ranges=ranges)
        # if next_wf == "R":
        #     return
        if next_wf == "A":
            self.valid_ranges.add(range_test_applied)
        #     return
        if next_wf not in {"R", "A"}:
            self.enter_workflow(wf_name=next_wf, ind=0, ranges=range_test_applied)
        # narrow ranges by applying complimentary test, and go to next item of current workflow
        range_test_not_applied = self.apply_test(
            test=test, ranges=ranges, negative=True
        )
        if len(self.workflows[wf_name]) > ind + 1:
            self.enter_workflow(
                wf_name=wf_name, ind=ind + 1, ranges=range_test_not_applied
            )

    def apply_test(
        self, *, test: str | bool, ranges: tuple[range], negative: bool = False
    ) -> tuple[range]:
        if test is True:
            return ranges
        # TODO: refacto to simplify
        _, val = test.split("<" if "<" in test else ">")
        val = int(val)
        if negative is False:  # apply the test
            if "<" in test:
                if "a" in test:
                    if ranges[2].start >= val:
                        return (
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                        )
                    return (
                        ranges[0],
                        ranges[1],
                        range(ranges[2].start, min(ranges[2].stop, val)),
                        ranges[3],
                    )
                if "x" in test:
                    if ranges[0].start >= val:
                        return (
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                        )
                    return (
                        range(ranges[0].start, min(ranges[0].stop, val)),
                        ranges[1],
                        ranges[2],
                        ranges[3],
                    )
                if "m" in test:
                    if ranges[1].start >= val:
                        return (
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                        )
                    return (
                        ranges[0],
                        range(ranges[1].start, min(ranges[1].stop, val)),
                        ranges[2],
                        ranges[3],
                    )
                if "s" in test:
                    if ranges[3].start >= val:
                        return (
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                        )
                    return (
                        ranges[0],
                        ranges[1],
                        ranges[2],
                        range(ranges[3].start, min(ranges[3].stop, val)),
                    )
                raise
            if ">" in test:
                if "a" in test:
                    if ranges[2].stop <= val:
                        return (
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                        )
                    return (
                        ranges[0],
                        ranges[1],
                        range(max(ranges[2].start, val + 1), ranges[2].stop),
                        ranges[3],
                    )
                if "x" in test:
                    if ranges[0].stop <= val:
                        return (
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                        )
                    return (
                        range(max(ranges[0].start, val + 1), ranges[0].stop),
                        ranges[1],
                        ranges[2],
                        ranges[3],
                    )
                if "m" in test:
                    if ranges[1].stop <= val:
                        return (
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                        )
                    return (
                        ranges[0],
                        range(max(ranges[1].start, val + 1), ranges[1].stop),
                        ranges[2],
                        ranges[3],
                    )
                if "s" in test:
                    if ranges[3].stop <= val:
                        return (
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                            range(-1, -1),
                        )
                    return (
                        ranges[0],
                        ranges[1],
                        ranges[2],
                        range(max(ranges[3].start, val + 1), ranges[3].stop),
                    )
            raise

        # apply the complementary test
        if "<" in test:  # test becomes >=
            if "a" in test:
                if ranges[2].stop < val:
                    return (range(-1, -1), range(-1, -1), range(-1, -1), range(-1, -1))
                return (
                    ranges[0],
                    ranges[1],
                    range(max(ranges[2].start, val), ranges[2].stop),
                    ranges[3],
                )
            if "x" in test:
                if ranges[0].stop < val:
                    return (range(-1, -1), range(-1, -1), range(-1, -1), range(-1, -1))
                return (
                    range(max(ranges[0].start, val), ranges[0].stop),
                    ranges[1],
                    ranges[2],
                    ranges[3],
                )
            if "m" in test:
                if ranges[1].stop < val:
                    return (range(-1, -1), range(-1, -1), range(-1, -1), range(-1, -1))
                return (
                    ranges[0],
                    range(max(ranges[1].start, val), ranges[1].stop),
                    ranges[2],
                    ranges[3],
                )
            if "s" in test:
                if ranges[3].stop < val:
                    return (range(-1, -1), range(-1, -1), range(-1, -1), range(-1, -1))
                return (
                    ranges[0],
                    ranges[1],
                    ranges[2],
                    range(max(ranges[3].start, val), ranges[3].stop),
                )
        # test becomes <=
        if "a" in test:
            if ranges[2].start > val:
                return (range(-1, -1), range(-1, -1), range(-1, -1), range(-1, -1))
            return (
                ranges[0],
                ranges[1],
                range(ranges[2].start, min(ranges[2].stop, val + 1)),
                ranges[3],
            )
        if "x" in test:
            if ranges[0].start > val:
                return (range(-1, -1), range(-1, -1), range(-1, -1), range(-1, -1))
            return (
                range(ranges[0].start, min(ranges[0].stop, val + 1)),
                ranges[1],
                ranges[2],
                ranges[3],
            )
        if "m" in test:
            if ranges[1].start > val:
                return (range(-1, -1), range(-1, -1), range(-1, -1), range(-1, -1))
            return (
                ranges[0],
                range(ranges[1].start, min(ranges[1].stop, val + 1)),
                ranges[2],
                ranges[3],
            )
        if "s" in test:
            if ranges[3].start > val:
                return (range(-1, -1), range(-1, -1), range(-1, -1), range(-1, -1))
            return (
                ranges[0],
                ranges[1],
                ranges[2],
                range(ranges[3].start, min(ranges[3].stop, val + 1)),
            )
        raise

    def compute_answer(self) -> int:
        return sum(prod(map(len, ranges)) for ranges in self.valid_ranges)


if __name__ == "__main__":
    test_pp = PartProcessor(MINI_TEST_DATA)
    assert (
        attempt := test_pp.solve_p2()
    ) == 4000**2, f"Should be {4000**2}, found {attempt}"
    test_pp_2 = PartProcessor(MINI_TEST_DATA_2)
    assert (
        attempt := test_pp_2.solve_p2()
    ) == 4000**2 + 4000 * 3999, f"Should be {4000**2+4000*3999}, found {attempt}"
    test_pp_3 = PartProcessor(MINI_TEST_DATA_3)
    assert (
        attempt := test_pp_3.solve_p2()
    ) == 4000**2 + 3999 * 4000 + 3999 * 3999 * 4000, f"Should be {4000**2+3999*4000+3999*3999*4000}, found {attempt} (diff: {attempt - (4000**2+3999*4000+3999*3999*3999)})"
    test_pp = PartProcessor(TEST_DATA)
    assert (
        attempt := test_pp.solve_p2()
    ) == 167409079868000, f"Should be 167409079868000, found {attempt}"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_file", type=str, help="Path to the input file")
    args = parser.parse_args()
    with open(args.input_file, "r") as f:
        data = f.read()
    pp = PartProcessor(data)
    pp.solve_p2()
