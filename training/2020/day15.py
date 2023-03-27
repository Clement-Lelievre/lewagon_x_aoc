from collections import namedtuple, defaultdict
from tqdm import tqdm

INPUT = "15,12,0,14,3,1"
NB_TURNS = 2020

# I notice that 0 is in the initial set of numbers; and it is a special number in this game as it will often be spoken
# so no need to test for the mmebership of 0, that might save some run time
# also, no need to store the whole game sequence in memory: all I need is the unique list of numbers spoken and for each,
# the last turn it was spoken


def last_ind(arr: list, item: int):
    """returns the index of the rightmost element found in arr equal to item"""
    for ind in range(len(arr)):
        if arr[len(arr) - ind - 1] == item:
            return len(arr) - ind - 1


def play(nb_turns: int, starting_numbers: str, verbose: bool = True) -> int:
    """Naïve approach (storing in memory the whole game sequence + not refactored), but sufficient because the input is relatively small

    Args:
        nb_turns (int): _description_
        starting_numbers (str): _description_
        verbose (bool, optional): _description_. Defaults to True.

    Returns:
        int: _description_
    """
    inp = list(map(int, starting_numbers.strip().split(",")))
    for _ in tqdm(range(len(inp), nb_turns)):
        previous = inp[-1]
        if inp.count(previous) == 1:
            inp.append(0)
        else:
            inp.append(len(inp) - 1 - last_ind(inp[:-1], inp[-1]))
    return inp[-1]


# test suite provided
Test = namedtuple("Test", ("start_seq", "answer", "nb_turns"), defaults=[NB_TURNS])
tests = (
    ("0,3,6", 436),
    ("1,3,2", 1),
    ("2,1,3", 10),
    ("1,2,3", 27),
    ("2,3,1", 78),
    ("3,2,1", 438),
    ("3,1,2", 1836),
)

run_part_one = False
if run_part_one:
    for test in tests:
        test = Test(*test)
        print(play(test.nb_turns, test.start_seq), test.answer)
        assert play(test.nb_turns, test.start_seq) == test.answer

    # my specific input
    print(play(NB_TURNS, INPUT))

# part 2 #######################################################################################################
NB_TURNS = 30_000_000

# now, given the input size, my above solution won't scale


def play(nb_turns: int, starting_numbers: str, verbose: bool = False) -> int:
    """Simulates the game for `nb_turns`turns, starting from the given `starting_numbers` sequence.

    In this game, the players take turns saying numbers. They begin by taking turns reading from a list of starting numbers
    (your puzzle input). Then, each turn consists of considering the most recently spoken number:

    If that was the first time the number has been spoken, the current player says 0.
    Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was
    previously spoken.

    So, after the starting numbers, each turn results in that player speaking aloud either 0 (if the last number is new) or an age
    (if the last number is a repeat).

    Args:
        nb_turns (int): _description_
        starting_numbers (list[int]): _description_
        verbose (bool) : _description_

    Returns:
        (int): the number spoken on the last turn
    """
    inp = list(map(int, starting_numbers.strip().split(",")))
    assert inp  # check seq is not empty
    turns_data = defaultdict(int, {v: ind for ind, v in enumerate(inp[:-1], start=1)})
    spoken = inp[-1]
    for turn_nb in tqdm(range(len(inp), nb_turns)):
        if spoken not in turns_data:
            turns_data[spoken] = turn_nb
            spoken = 0
        else:
            former = spoken
            spoken = turn_nb - turns_data[spoken]
            turns_data[former] = turn_nb
        if verbose:
            print(turns_data, f"{spoken=}")
    return spoken


# test suite provided
Test = namedtuple("Test", ("start_seq", "answer", "nb_turns"), defaults=[NB_TURNS])
tests = (
    ("0,3,6", 175594),
    ("1,3,2", 2578),
    ("2,1,3", 3544142),
    ("1,2,3", 261214),
    ("2,3,1", 6895259),
    ("3,2,1", 18),
    ("3,1,2", 362),
)

DEV_MODE = False
if DEV_MODE:
    for test in tests:
        test = Test(*test)
        print(play(test.nb_turns, test.start_seq), test.answer)
        assert play(test.nb_turns, test.start_seq) == test.answer

# my specific input
print(play(NB_TURNS, INPUT))
