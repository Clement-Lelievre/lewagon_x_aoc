import re
from copy import deepcopy

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

INPUT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


# Notes:
# in terms of graph theory, the graph is undirected and unweighted (unit weight everywhere)
# a state is the combination of: time, position, and which valves opened
# pruning the tree: I can safely discard a state if it's inferior to a visited state
# how many states to visit? my input has 59 valves, but only 44 of them have flow rate = 0 so at best I just go through these rooms

# from the text it appears that I can only look at paths that are 14 units long, not 15, because the 15th valve won't have time to work anyway
# but the thing is, just because you enter a valve room doesn't imply it's optimal to open the valve; it may only be on your way to a more
# rewarding valve so maybe the path will be longer than 14 units

# extract valve info; a dict of dicts looks suitable to store it
valve_data_pattern = re.compile("^Valve (\w+).*?(\d+).*?valves? (.*?)$", re.IGNORECASE)
valves = [row for v in INPUT.splitlines() if (row := v.strip())]
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
best_path = None


def explore_slow(
    current_room: str,
    time_left: int,
    opened_valves: dict,
    total_pressure_released: int,
    current_path: list,
) -> None:
    """Slow version, because it also prints out the best path"""
    global max_pressure_released, best_path
    # assert time_left >= 0
    if (current_state := (current_room, time_left, total_pressure_released)) in visited:
        return
    # if is_dominated(current_state):
    #     return
    visited.add(current_state)
    current_path.append(current_state)
    if time_left == 0 or len(opened_valves) == len(valves_of_interest):
        if total_pressure_released > max_pressure_released:
            best_path = current_path
            max_pressure_released = total_pressure_released
        return
    if current_room in valves_of_interest and current_room not in opened_valves:
        time_left -= 1
        opened_valves[current_room] = time_left
        total_pressure_released += time_left * valves_of_interest[current_room]
        visited.add(current_state)
        current_path.append((current_room, time_left, total_pressure_released))
        if time_left == 0 or len(opened_valves) == len(valves_of_interest):
            if total_pressure_released > max_pressure_released:
                best_path = current_path
                max_pressure_released = total_pressure_released
            return
    for next_room in valve_dict[current_room]["connections"]:
        explore(
            next_room,
            time_left - 1,
            deepcopy(opened_valves),
            total_pressure_released,
            deepcopy(current_path),
        )


def explore(
    current_room: str,
    time_left: int,
    opened_valves: dict[str, int],
    total_pressure_released: int,
) -> None:
    global max_pressure_released, best_path
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


explore("AA", 30, dict(), 0)
print(max_pressure_released)  # 2077

# my solution above works on every actual input I've come across (including mine of course), but not on the example input!
# I think that's because I wrongly rule out some paths at the beginning of the function
# so only half credit

# part 2
