"""AoC 2023 day 19"""

from collections import defaultdict, namedtuple
import re
import argparse

# parts contain four categries: x, m, a, s
# each category gets one non-null integer rating
# workflows contain one or more rules (ie tests)
# each test (except the fourth one) has a condition, and upon result sends to another workflow
# the last has no condition and thus is always executed

# eventually the goal is to send all parts through the workflows system, starting with the workflow named 'in'
# and to collect all accepted workflows, that is, those reaching an A at any point
# then make a computation on these accepted parts

# how to proceed:
# the input data is a string containing workflows, then a newline, then parts
# I'll store the workflows in dicts of dicts: {workflow1: {cond1: workflow2, cond2: workflow2, cond3:workflow3, True:workflow/A/R}, workflow2:...}
# I'll store the parts in named tuples, for dot notation access

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

Part = namedtuple("Part", ["x", "m", "a", "s"])


class PartProcessor:
    def __init__(self, data: str) -> None:
        self.data = data
        self.workflows = None
        self.parts = None
        self.ops = {
            "<": int.__lt__,
            ">": int.__gt__,
            "=": int.__eq__,
        }  # maps signs to int operations
        self.categories = ["x", "m", "a", "s"]
        self.process_input()

    def process_input(self) -> None:
        lines = self.data.strip().split()
        self.workflows, self.parts = defaultdict(dict), []
        for line in lines:
            if not line.strip():
                continue
            if line.startswith("{"):
                self.parts.append(Part(*map(int, re.findall(r"\d+", line))))
            else:
                workflow_name = line[: line.index("{")]
                tests = line[line.index("{") + 1 : -1].split(",")
                for test in tests:
                    if ":" in test:
                        self.workflows[workflow_name][test[: test.index(":")]] = test[
                            test.index(":") + 1 :
                        ]
                    else:
                        self.workflows[workflow_name][True] = test

    def solve_p1(self) -> int:
        accepted_parts = []
        for part in self.parts:
            current_workflow = "in"
            while current_workflow not in {"R", "A"}:
                for test, next_workflow in self.workflows[current_workflow].items():
                    if test is True:
                        current_workflow = next_workflow
                        break
                    inf_test, eq_test = "<" in test, "=" in test
                    if inf_test or eq_test or ">" in test:
                        category, val = test.split("<" if inf_test else "=" if eq_test else ">")
                        if self.ops["<" if inf_test else ">"](
                            part[self.categories.index(category)], int(val)
                        ):
                            current_workflow = next_workflow
                            break
                else:
                    raise NotImplementedError
            if current_workflow == "A":
                accepted_parts.append(part)
        answer = sum(sum([p.x, p.m, p.a, p.s]) for p in accepted_parts)
        print(f"Part 1: {answer}")
        return answer

    def solve_p2(self) -> int:
        answer = 0

        def recurse(
            current_workflow: str,
            x_range:range=range(1, 4001),
            m_range:range=range(1, 4001),
            a_range:range=range(1, 4001),
            s_range:range=range(1, 4001),
        ) -> None:
            nonlocal answer
            for test, workflow in self.workflows[current_workflow].items():
                if test is True and workflow == "A":
                    answer += len(x_range) * len(m_range) * len(a_range) * len(s_range)
                elif test is True and workflow == "R":
                    continue
                elif test is True:
                    recurse(workflow, x_range, m_range, a_range, s_range)
                # process test info and reduce rating range accordingly
                else:
                    inf_test, eq_test = "<" in test, "=" in test
                    category, val = test.split("<" if inf_test else "=" if eq_test else ">")
                    val = int(val)
                    if category == "a":
                        a_range=a_range and (
                            range(val, val + 1)
                            if "=" in test
                            else (range(1,val) if "<" in test else range(val + 1, 4001))
                        )
                    elif category == "m":
                        m_range=m_range and (
                            range(val, val + 1)
                            if "=" in test
                            else (range(1,val) if "<" in test else range(val + 1, 4001))
                        )
                    elif category == "x":
                        x_range=x_range and (
                            range(val, val + 1)
                            if "=" in test
                            else (range(1,val) if "<" in test else range(val + 1, 4001))
                        )
                    elif category == "s":
                        s_range=s_range and (
                            range(val, val + 1)
                            if "=" in test
                            else (range(1,val) if "<" in test else range(val + 1, 4001))
                        )
                    else:
                        raise ValueError

                    recurse(workflow, x_range, m_range, a_range, s_range)
        recurse("in")
        print(f"Part 2: {answer}")
        return answer

if __name__ == "__main__":
    test_pp = PartProcessor(TEST_DATA)
    assert test_pp.solve_p1() == 19114
    assert test_pp.solve_p2() == 167409079868000
    # parser = argparse.ArgumentParser(description=__doc__)
    # parser.add_argument("input_file", type=str, help="Path to the input file")
    # args = parser.parse_args()
    # with open(args.input_file, "r") as f:
    #     data = f.read()
    # pp = PartProcessor(data)
    # pp.solve_p1()
