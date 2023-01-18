import re
from copy import deepcopy
from collections import deque
from itertools import combinations, product

# instructive remark by Peter Norvig: (https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2022.ipynb)
# "Conceptually this is a simple search problem: we move from room to room for 30 minutes,
# opening valves as we go, trying to find the sequence of actions that maximizes the total flow.
# Practically, I'm concerned about the size of the search state space.
# With 30 minutes, 56 rooms, and 56 valves that can be either open or not,
# there are 30 × 56 × 256 ≈ 10^20 states to consider. We're going to need some way of directing the search."

INPUT = """Valve QE has flow rate=3; tunnels lead to valves OU, ME, UX, AX, TW
Valve TN has flow rate=16; tunnels lead to valves UW, CG, WB
Valve UX has flow rate=0; tunnels lead to valves AA, QE
Valve HK has flow rate=5; tunnels lead to valves HT, QU, TW, WV, OK
Valve SK has flow rate=14; tunnels lead to valves GH, GA, XM
Valve HY has flow rate=0; tunnels lead to valves LG, AA
Valve BK has flow rate=0; tunnels lead to valves SZ, AA
Valve BY has flow rate=11; tunnels lead to valves SP, HS, DN, KD, TK
Valve GR has flow rate=0; tunnels lead to valves FE, OK
Valve OH has flow rate=0; tunnels lead to valves BM, KE
Valve DC has flow rate=0; tunnels lead to valves AX, XH
Valve YS has flow rate=0; tunnels lead to valves XH, EU
Valve KP has flow rate=0; tunnels lead to valves KI, OF
Valve LG has flow rate=0; tunnels lead to valves FE, HY
Valve FE has flow rate=4; tunnels lead to valves RU, GR, YI, LG, ME
Valve NK has flow rate=0; tunnels lead to valves SD, BM
Valve EU has flow rate=0; tunnels lead to valves NS, YS
Valve OF has flow rate=0; tunnels lead to valves CJ, KP
Valve TW has flow rate=0; tunnels lead to valves HK, QE
Valve GL has flow rate=0; tunnels lead to valves AF, CQ
Valve OU has flow rate=0; tunnels lead to valves KN, QE
Valve BM has flow rate=24; tunnels lead to valves GH, NK, YH, OH
Valve GA has flow rate=0; tunnels lead to valves SK, SZ
Valve EI has flow rate=17; tunnels lead to valves ZX, AF
Valve QN has flow rate=25; tunnel leads to valve SD
Valve ZX has flow rate=0; tunnels lead to valves EI, WB
Valve ME has flow rate=0; tunnels lead to valves QE, FE
Valve CJ has flow rate=21; tunnels lead to valves OF, YI, KD
Valve AX has flow rate=0; tunnels lead to valves DC, QE
Valve LW has flow rate=0; tunnels lead to valves AA, HT
Valve CQ has flow rate=18; tunnels lead to valves GL, XM
Valve KN has flow rate=0; tunnels lead to valves SZ, OU
Valve HS has flow rate=0; tunnels lead to valves UZ, BY
Valve RU has flow rate=0; tunnels lead to valves TK, FE
Valve SZ has flow rate=6; tunnels lead to valves WV, GA, BK, KE, KN
Valve AF has flow rate=0; tunnels lead to valves GL, EI
Valve YI has flow rate=0; tunnels lead to valves FE, CJ
Valve HT has flow rate=0; tunnels lead to valves LW, HK
Valve WV has flow rate=0; tunnels lead to valves SZ, HK
Valve TK has flow rate=0; tunnels lead to valves BY, RU
Valve GH has flow rate=0; tunnels lead to valves BM, SK
Valve CG has flow rate=0; tunnels lead to valves TN, SP
Valve AA has flow rate=0; tunnels lead to valves HY, UX, VQ, LW, BK
Valve SP has flow rate=0; tunnels lead to valves BY, CG
Valve XM has flow rate=0; tunnels lead to valves SK, CQ
Valve DN has flow rate=0; tunnels lead to valves NS, BY
Valve XH has flow rate=22; tunnels lead to valves YS, QU, UZ, DC
Valve KI has flow rate=20; tunnels lead to valves UW, KP
Valve OK has flow rate=0; tunnels lead to valves HK, GR
Valve YH has flow rate=0; tunnels lead to valves VQ, BM
Valve UZ has flow rate=0; tunnels lead to valves XH, HS
Valve KE has flow rate=0; tunnels lead to valves OH, SZ
Valve VQ has flow rate=0; tunnels lead to valves AA, YH
Valve QU has flow rate=0; tunnels lead to valves HK, XH
Valve WB has flow rate=0; tunnels lead to valves TN, ZX
Valve UW has flow rate=0; tunnels lead to valves KI, TN
Valve SD has flow rate=0; tunnels lead to valves NK, QN
Valve NS has flow rate=23; tunnels lead to valves EU, DN
Valve KD has flow rate=0; tunnels lead to valves BY, CJ
"""

# INPUT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II"""


# Notes:
# in terms of graph theory, the graph is undirected and unweighted (unit weight everywhere)
# a state is the combination of: time, position, and which valves opened
# pruning the tree: I can safely discard a state if it's inferior to a visited state
# how many states to visit? my input has 59 valves, but only 44 of them have flow rate = 0 so at best I just go through these rooms

# from the text it appears that I can only look at paths that are 14 units long, not 15, because the 15th valve won't have time to work anyway
# but the thing is, just because you enter a valve room doesn't imply it's optimal to open the valve; it may only be on your way to a more
# rewarding valve so maybe the path will be longer than 14 units

# extract valve info; a dict of dicts looks suitable to store it
valve_data_pattern = re.compile(r"^Valve (\w+).*?(\d+).*?valves? (.*?)$", re.IGNORECASE)
valves = (row for v in INPUT.splitlines() if (row := v.strip()))
valve_dict = {}
for valve in valves:
    valve_name, valve_power, valve_connections = (
        (regex_search := valve_data_pattern.search(valve)).group(1),
        regex_search.group(2),
        tuple(map(str.strip, regex_search.group(3).split(","))),
    )
    valve_dict[valve_name] = {
        "flow rate": int(valve_power),
        "connections": valve_connections,
    }

# implement search algo
valves_of_interest = {k: fr for k, v in valve_dict.items() if (fr := v["flow rate"])}
max_pressure_released = 0
visited = set()


def explore(
    current_room: str,
    time_left: int,
    opened_valves: dict[str, int],
    total_pressure_released: int,
) -> None:
    global max_pressure_released
    # assert time_left >= 0
    if (current_state := (current_room, time_left, total_pressure_released)) in visited:
        return  # actually it could be that this isn't even enough to tell a state from a different one!
    visited.add(current_state)
    if time_left == 0 or len(opened_valves) == len(valves_of_interest):
        if total_pressure_released > max_pressure_released:
            max_pressure_released = total_pressure_released
        return
    if current_room in valves_of_interest and current_room not in opened_valves:
        time_left -= 1
        opened_valves[current_room] = time_left
        total_pressure_released += time_left * valves_of_interest[current_room]
        visited.add(current_state)
        if time_left == 0 or len(opened_valves) == len(valves_of_interest):
            if total_pressure_released > max_pressure_released:
                max_pressure_released = total_pressure_released
            return
    for next_room in valve_dict[current_room]["connections"]:
        explore(
            next_room, time_left - 1, deepcopy(opened_valves), total_pressure_released
        )


# uncomment the next two lines if you want to see the recursive version in action
explore("AA", 30, {}, 0)
print(
    f"Part 1 (with recursion): {max_pressure_released}"
)  # 2077 on my input, 1651 on the test provided

# my solution above works on every actual input I've come across (including mine of course), but not on the example input!
# I think that's because I wrongly rule out some paths at the beginning of the function
# so only half credit

# redoing part 1, this time implementing a BFS


class VolcanoMaze:
    """Simulates the volcano maze described in the challenge.
    Note: for part 2, while with 2 people it is important to take into account the fact
    that opening twice the same valve should be prevented, I'll consider that both the elf and
    the elephant may be inside the same room or tunnel at the same time, as this is not
    specified in the text"""

    def __init__(self, input_: str) -> None:
        self.input_ = input_
        self.valve_data_pattern = re.compile(
            r"^Valve (\w+).*?(\d+).*?valves? (.*?)$", re.IGNORECASE
        )
        self.get_data()
        self.valves_of_interest = {
            k: fr for k, v in self.valve_dict.items() if (fr := v["flow rate"])
        }

    def get_data(self) -> None:
        valves = (row for v in self.input_.splitlines() if (row := v.strip()))
        valve_dict = {}
        for valve in valves:
            valve_name, valve_power, valve_connections = (
                (regex_search := self.valve_data_pattern.search(valve)).group(1),
                regex_search.group(2),
                tuple(map(str.strip, regex_search.group(3).split(","))),
            )
            valve_dict[valve_name] = {
                "flow rate": int(valve_power),
                "connections": valve_connections,
            }
        self.valve_dict = valve_dict

    def max_pressure_one_visitor(self) -> int:
        total_pressures_released = set()
        visited = set()
        queue = (
            deque()
        )  # will store states as (room, time, total pressure released, valves opened)
        # {'BB': 13, 'CC': 2, 'DD': 20, 'EE': 3, 'HH': 22, 'JJ': 21}
        queue.append(("AA", 30, 0, set()))
        while queue:
            room, time_left, tpr, valves_opened = queue.popleft()
            if any(
                room == seen_room and time_left <= seen_time_left and tpr <= seen_tpr
                for seen_room, seen_time_left, seen_tpr, _ in visited
            ):
                continue  # dominated state
            if valves_opened == set(valves_of_interest) or time_left in (0, 1):
                total_pressures_released.add(tpr)
                continue  # we don't break as we want to explore every path
            visited.add((room, time_left, tpr, frozenset(valves_opened)))
            if (
                room in self.valves_of_interest and room not in valves_opened
            ):  # open the valve
                time_left -= 1  # open valve
                tpr += self.valves_of_interest[room] * time_left
                valves_opened.add(room)
                visited.add((room, time_left, tpr, frozenset(valves_opened)))
            if time_left >= 1:
                time_left -= 1  # travel to neighbouring room
                for neigh in self.valve_dict[room]["connections"]:
                    queue.append((neigh, time_left, tpr, valves_opened.copy()))
        print(
            f"Part 1 (with a BFS queue): {max(total_pressures_released, default = 0)}"
        )  # 2077 on my input, 1651 on the test provided

    def setup_to_tpr(self, path: tuple[tuple[str, int]]) -> int:
        """From the description of a path as a tuple of (room_name, time_left after opening room valve)
        computes and returns the total pressure released with that path

        Args:
            path (tuple): tuple of (room_name, time_left after opening room valve)

        Returns:
            int: the total pressure released with that path
        """
        return sum(
            time_left * self.valve_dict[room]["flow rate"] for room, time_left in path
        )

    def max_pressure_two_visitors(self, training_time: int = 4) -> int:
        all_opening_setups = set()
        visited = set()
        queue = deque()
        queue.append(("AA", 30 - training_time, 0, {}))
        while queue:
            room, time_left, tpr, valves_opened = queue.popleft()
            if any(
                room == seen_room and time_left <= seen_time_left and tpr <= seen_tpr
                for seen_room, seen_time_left, seen_tpr, _ in visited
            ):
                continue  # dominated state
            visited.add((room, time_left, tpr, tuple(valves_opened.items())))
            if set(valves_opened) == set(valves_of_interest) or time_left in (0, 1):
                all_opening_setups.add(tuple(valves_opened.items()))
                continue  # we don't break as we want to explore every path
            if room in self.valves_of_interest and room not in valves_opened:
                time_left -= 1  # open the valve
                tpr += self.valves_of_interest[room] * time_left
                valves_opened[room] = time_left
                visited.add((room, time_left, tpr, tuple(valves_opened.items())))
            if time_left >= 1:
                time_left -= 1  # travel to neighbouring room
                for neigh in self.valve_dict[room]["connections"]:
                    queue.append((neigh, time_left, tpr, valves_opened.copy()))
        # combine all couples of paths, accounting for common valves, and display the best score
        max_tpr = 0
        for path1, path2 in combinations(all_opening_setups, 2):
            s1 = set(elem[0] for elem in path1)
            s2 = set(
                elem[0] for elem in path2
            )  # set of valves opened in the first and second paths
            common_valves = s1 & s2
            if not common_valves:
                tpr = self.setup_to_tpr(path1) + self.setup_to_tpr(path2)
            else:
                for dispatch in product((0, 1), repeat=len(common_valves)):
                    d1, d2 = dict(path1), dict(path2)
                    comm = common_valves.copy()
                    for digit in dispatch:
                        current_common_valve = comm.pop()
                        if digit == 0:  # keep in d1
                            timeleft = d2[current_common_valve]
                            d2.pop(current_common_valve)
                            for k in d2:
                                if d2[k] < timeleft:
                                    d2[k] += 1
                        else:  # keep in d2
                            timeleft = d1[current_common_valve]
                            d1.pop(current_common_valve)
                            for k in d1:
                                if d1[k] < timeleft:
                                    d1[k] += 1
                    assert set(d1).isdisjoint(set(d2))
                    tpr = self.setup_to_tpr(tuple(d1.items())) + self.setup_to_tpr(
                        tuple(d2.items())
                    )
            if tpr > max_tpr:
                max_tpr = tpr
        print(
            f"Part 2 (with a BFS queue): {max_tpr}"
        )  # 2741 on my input, 1707 on the test provided


V = VolcanoMaze(INPUT)
V.max_pressure_one_visitor()

# part 2
# this time we are 2 exploring the maze, each having 26 minutes
V.max_pressure_two_visitors()

# my approach works on my input, but not on the test provided
# this is likely because my approach does not try all possible paths, at least for part 2
# for part 2, I build on two best paths regardless of constraints and then remove
# common valves
# I believe in doing so I miss some paths
# this is somewhat unsatisfying, but Peter Norvig did the same
# which is quite reassuring
