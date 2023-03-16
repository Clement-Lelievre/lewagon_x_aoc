"""BFS to solve this optimization problem. I thought about A* but it may not be
so obvious to find a good heuristic function as there can be tricky cases
that seem close to the target but are not"""

import logging
import math
from collections import deque
from itertools import chain, combinations
from queue import PriorityQueue
from time import time
from typing import Generator

logging.basicConfig(level=logging.INFO)

INPUT_TEST = """The first floor contains a hydrogen-compatible microchip and a
lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""

INPUT = """The first floor contains a thulium generator, a thulium-compatible
microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a
strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible
microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.
"""

INPUT_P2 = """The first floor contains a thulium generator, a thulium-compatible 
microchip, a plutonium generator, a strontium generator, An elerium generator, 
An elerium-compatible microchip, A dilithium generator, A dilithium-compatible microchip.
The second floor contains a plutonium-compatible microchip and a 
strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible 
microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.
"""  # I built this one manually, from INPUT

# I will encode states like so: the elevator as 0, chips as odd integers,
# their respective generators as the even integers directly above their chip
# (e.g. chip 1 and generator 2, chip 3 and generator 4 etc.)
# If too inefficient, I'll think about a better way


class GeneratorLab:
    """Emulates the process described in the challenge desc"""

    State = tuple[frozenset[int], ...]
    NB_FLOORS: int = 4
    ALL_FLOORS: set[int] = set(range(NB_FLOORS))

    def __init__(self, input_: str) -> None:
        self.input_: str = input_
        self.find_nb_generators()
        self.TARGET: GeneratorLab.State = (
            frozenset(),
            frozenset(),
            frozenset(),
            frozenset(range(2 * self.nb_gen + 1)),
        )

    def find_nb_generators(self) -> int:
        """Parses the input, detects the word 'generator', and returns the number of unique
        generator (and therefore microchips)

        Args:
            input_ (str): the input provided

        Returns:
            int: the number of unique generator (and therefore microchips)
        """
        words = self.input_.split()
        self.nb_gen = len(
            set(words[i - 1] for i in range(1, len(words)) if "generator" in words[i])
        )
        return self.nb_gen

    def state_is_valid(self, state: State | frozenset[int]) -> bool:
        """Checks that a given state is valid, that is no chip is going to be fried

        Args:
            state (tuple): a tuple of frozensets containing integers representing chips, the elevator, or generators

        Returns:
            bool: whether `state` is valid
        """
        if isinstance(state, frozenset):  # the data for just one floor was provided
            state = (state,)
        for floor in state:  # a full state was provided (all four floors in a tuple)
            chips = {elem for elem in floor if elem % 2}
            generators = floor - chips - {0}  # discard the elevator
            if any(chip + 1 not in generators and generators for chip in chips):
                return False
        return True

    def make_neighbor_states(
        self, state: State
    ) -> Generator[tuple[int, State], None, None]:
        """Generates all legal neighboring states, as well as the elevator distance
        required to reach them

        Args:
            state (State): the starting state

        Yields:
            Generator[tuple[int, State], None, None]: tuples of elevator dist, neighboring state
        """
        # locate the elevator
        for i, floor in enumerate(state):
            if 0 in floor:
                elev_floor = i
                break
        # take any combination of 1 and 2 items
        items_excl_elevator = [elem for elem in state[elev_floor] if elem]
        # send it to any other floor
        for new_floor in self.ALL_FLOORS - set([elev_floor]):
            for comb in chain(
                combinations(items_excl_elevator, 1),
                combinations(items_excl_elevator, 2),
            ):
                to_move = frozenset([0, *comb])
                if not self.state_is_valid(state[elev_floor] - to_move):
                    continue
                # before yielding a neighbor state, make sure it is legal to do so (at each intermediate floor)
                for traversed_floor in set(
                    range(min(new_floor, elev_floor), max(new_floor, elev_floor) + 1)
                ) - set([elev_floor]):
                    if not self.state_is_valid(state[traversed_floor] | to_move):
                        break
                else:
                    elevator_dist = abs(new_floor - elev_floor)
                    new_state = list(state)  # I have to make it mutable
                    new_state[elev_floor] -= to_move
                    new_state[new_floor] |= to_move
                    yield elevator_dist, tuple(
                        new_state
                    )  # make it hashable again, for storage purposes

    def heuristic(self, state: State) -> int:
        """An estimate of the number of moves needed to move everything to top
        legally, from `state`"""
        total = sum(
            (
                len(floor) if 0 not in floor else len(floor) - 1
            )  # discard the elevator (0)
            * (self.NB_FLOORS - i - 1)
            for i, floor in enumerate(state)
        )
        return math.ceil(total / 2)  # Can move two items in one move

    def reconstruct_path(self, came_from: dict[State, State]) -> list[State]:
        """Reconstructs the full path from a list of 'came from' info

        Args:
            came_from (dict[State, State]): a dict storing the came from info

        Returns:
            list[State]: the nodes in a list
        """
        current = self.TARGET
        path = [current]
        while (prev := came_from[current]) is not None:
            path.append(prev)
            current = prev
        path.reverse()
        return path

    def solve_fifo(self, initial_state: State) -> int:
        """I decided not to code the REGEX-based parser and function that builds the initial state from the text,
        so somewhat artificially ths function expects the initial_state manually built, and the input text
        to detect the number of generators. Obviously this could be optimized and detected direclty from the `initial_state`
        This method solves the problem using a FIFO queue

        Args:
            initial_state (tuple): a tuple of frozensets containing chips, the elevator, and generators
            input_ (str): the text input

        Raises:
            Exception: if no path reaches the target state

        Returns:
            int: the minimum number of steps (= elevator moves) to reach the target state
        """
        starttime = time()
        seen = set()
        queue = deque([(0, initial_state)])
        while queue:
            dist, current_state = queue.popleft()  # FIFO
            if current_state in seen or not self.state_is_valid(current_state):
                continue
            if current_state == self.TARGET:
                logging.info(
                    f"{dist} solved in {round(time() - starttime, 1)} seconds with a queue (FIFO)"
                )
                break
            seen.add(current_state)
            #  add neighbours to the queue
            queue.extend(
                (dist + elevator_dist, neigh)
                for elevator_dist, neigh in self.make_neighbor_states(current_state)
            )
        else:
            raise Exception("Unreachable")
        return dist

    def solve_pqueue(self, initial_state: State, verbose: bool = False) -> int:
        """I decided not to code the REGEX-based parser and function that builds the initial state from the text,
        so somewhat artificially ths function expects the initial_state manually built, and the input text
        to detect the number of generators. Obviously this could be optimized and detected direclty from the `initial_state`
        Uses a priority queue (A*)

        Args:
            initial_state (tuple): a tuple of frozensets containing chips, the elevator, and generators
            input_ (str): the text input

        Raises:
            Exception: if no path reaches the target state

        Returns:
            int: the minimum number of steps (= elevator moves) to reach the target state
        """
        starttime = time()
        seen = set()
        came_from: dict = {}
        came_from[initial_state] = None
        queue: PriorityQueue = PriorityQueue()
        queue.put(
            (0, 0, initial_state)
        )  # (estimated remaining nb of moves, distance, floor states)
        while not queue.empty():
            _, dist, current_state = queue.get()
            if current_state == self.TARGET:
                logging.info(
                    f"{dist} solved in {round(time() - starttime, 1)} seconds with a priority queue"
                )
                if verbose:
                    logging.info("Here is the path taken:")
                    for step in self.reconstruct_path(came_from):
                        logging.info(step)
                break
            seen.add(current_state)
            #  add neighbours to the queue
            for elevator_dist, neigh in self.make_neighbor_states(current_state):
                if neigh in seen:
                    continue
                came_from[neigh] = current_state
                queue.put((self.heuristic(neigh), dist + elevator_dist, neigh))
        else:
            raise Exception("Unreachable")
        return dist


if __name__ == "__main__":
    # part 1
    # test
    GLTEST = GeneratorLab(INPUT_TEST)
    assert GLTEST.find_nb_generators() == 2
    INITIAL_STATE_TEST: GeneratorLab.State = (
        frozenset([0, 1, 3]),
        frozenset([2]),
        frozenset([4]),
        frozenset(),
    )
    assert GLTEST.state_is_valid(INITIAL_STATE_TEST)
    assert GLTEST.solve_fifo(INITIAL_STATE_TEST) == 11
    assert GLTEST.solve_pqueue(INITIAL_STATE_TEST) == 11

    # my actual input
    GL = GeneratorLab(INPUT)
    assert GL.find_nb_generators() == 5
    INITIAL_STATE: GeneratorLab.State = (
        frozenset([0, 2, 1, 4, 6]),
        frozenset([3, 5]),
        frozenset([8, 7, 10, 9]),
        frozenset(),
    )
    assert GL.state_is_valid(INITIAL_STATE)
    GL.solve_pqueue(INITIAL_STATE)

    # part 2
    # my actual input
    GL_P2 = GeneratorLab(INPUT_P2)
    assert GL_P2.find_nb_generators() == 7
    INITIAL_STATE_P2: GeneratorLab.State = (
        frozenset([0, 2, 1, 4, 6, 11, 12, 13, 14]),
        frozenset([3, 5]),
        frozenset([8, 7, 10, 9]),
        frozenset(),
    )
    assert GL_P2.state_is_valid(INITIAL_STATE_P2)
    GL_P2.solve_pqueue(INITIAL_STATE_P2)
