"""Reproducing Peter Norvig's solution for 2016 day 11 from https://github.com/norvig/pytudes/blob/main/ipynb/Advent%20of%20Code.ipynb
in order to check the run time on my machine, as I am stunned to read that for part 2 his solution took
around 14 min when line takes around 1 second!"""
from collections import namedtuple
from itertools import chain, combinations
import math, time
from heapq import heappop, heappush

# utils

Ø = frozenset()  # Empty set


def Path(previous, s):
    "Return a list of states that lead to state s, according to the previous dict."
    return [] if (s is None) else Path(previous, previous[s]) + [s]


def astar_search(start, h_func, moves_func):
    "Find a shortest sequence of states from start to a goal state (a state s with h_func(s) == 0)."
    frontier = [
        (h_func(start), start)
    ]  # A priority queue, ordered by path length, f = g + h
    previous = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}  # The cost of the best path to a state.
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(previous, s)
        for s2 in moves_func(s):
            new_cost = path_cost[s] + 1
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))


# main code

State = namedtuple("State", "elevator, floors")


def fs(*items):
    return frozenset(items)


legal_floors = {0, 1, 2, 3}


def combos(things):
    "All subsets of 1 or 2 things."
    for s in chain(combinations(things, 1), combinations(things, 2)):
        yield fs(*s)


def moves(state):
    "All legal states that can be reached in one move from this state"
    L, floors = state
    for L2 in {L + 1, L - 1} & legal_floors:
        for stuff in combos(floors[L]):
            newfloors = tuple(
                (s | stuff if i == L2 else s - stuff if i == state.elevator else s)
                for (i, s) in enumerate(state.floors)
            )
            if legal_floor(newfloors[L]) and legal_floor(newfloors[L2]):
                yield State(L2, newfloors)


def legal_floor(floor):
    "Floor is legal if no RTG, or every chip has its corresponding RTG."
    rtgs = any(r.endswith("G") for r in floor)
    chips = [c for c in floor if c.endswith("M")]
    return not rtgs or all(generator_for(c) in floor for c in chips)


def generator_for(chip):
    return chip[0] + "G"


def h_to_top(state):
    "An estimate of the number of moves needed to move everything to top."
    total = sum(len(floor) * i for (i, floor) in enumerate(reversed(state.floors)))
    return math.ceil(total / 2)  # Can move two items in one move.


part1 = State(
    0, (fs("TG", "TM", "PG", "SG"), fs("PM", "SM"), fs("pM", "pG", "RM", "RG"), Ø)
)
starttime = time.time()
answer = len(astar_search(part1, h_to_top, moves)) - 1
total_time = time.time() - starttime
print(f"{answer} in {total_time}")  # 16 sec
