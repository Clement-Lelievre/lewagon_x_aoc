import re

INPUT = """initial state: #.##.#.##..#.#...##...#......##..#..###..##..#.#.....##..###...#.#..#...######...#####..##....#..###

##.## => .
##... => #
..#.# => #
#.... => .
#..#. => #
.#### => .
.#..# => .
.##.# => .
#.##. => #
####. => .
..##. => .
##..# => .
.#.## => #
.#... => .
.##.. => #
..#.. => #
#..## => #
#.#.. => #
..### => #
...#. => #
###.. => .
##.#. => #
#.#.# => #
##### => #
....# => .
#.### => .
.#.#. => #
.###. => #
...## => .
..... => .
###.# => #
#...# => ."""

INPUT_TEST = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

CAT = "".join
PAT = re.compile(r"([\.#]{5})\s=>\s([#\.])")


def process_input(input_: str):
    rules = {}
    for row in input_.splitlines():
        if vals := PAT.findall(row):
            rules[vals[0][0]] = vals[0][1]
    # assert len(rules) == 32, "all 2**5 = 32 cases are NOT covered"
    top_row = input_.splitlines()[0]
    initial_state = [".",".",".","."] + list(top_row[top_row.index(":") + 2 :]) + [".",".",".","."]
    return initial_state, rules


def solve_part1(input_: str, nb_gen: int = 20) -> int:
    state, rules = process_input(input_)
    offset = -4
    for _ in range(nb_gen):
        new_state = []
        for i in range(2, len(state) - 2):
            new_state.append(rules.get(CAT(state[i - 2 : i + 3]), "."))
        # if CAT(new_state[:2]) != "..":
        new_state = [".", "."] + new_state
        offset -= 2
        # if CAT(new_state[-2:]) != "..":
        new_state.extend([".", "."])
        state = new_state
        print(CAT(state))

    ans = 0
    for i in range(len(state)):
        if state[i] == "#":
            ans += i + offset
    print(f"part 1: {ans}")
    return ans


assert solve_part1(INPUT_TEST) == 325
solve_part1(INPUT)

# part 2
