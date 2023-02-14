"Marble mania: https://adventofcode.com/2018/day/9"
from collections import deque
from tqdm import tqdm

INPUT = 403, 71_920


def solve_part1(nb_players: int, last_marble_value: int) -> int:
    """Simulates the game

    Args:
        nb_players (int): nb of elves taking part
        last_marble_value (int): number of the last marble of the game

    Returns:
        int: the highest score at the end of the game
    """
    circle = [0]
    current = 0
    scores = dict(zip(range(nb_players), (0 for _ in range(nb_players))))
    current_player = 0
    for to_insert in range(1, last_marble_value + 1):
        if to_insert % 23:
            if (lc := len(circle)) >= 2:
                insertion_index = (circle.index(current) + 2) % lc
                if insertion_index:
                    circle.insert(insertion_index, to_insert)
                else:
                    circle.append(to_insert)
            elif lc == 1:
                circle.append(to_insert)
            else:
                raise ValueError
            current = to_insert
        else:
            to_drop_ind = circle.index(current) - 7
            current = circle[to_drop_ind + 1]
            scores[current_player] += to_insert + circle.pop(to_drop_ind)
        # print(f"[{current_player + 1}] ({current}) {circle}")
        current_player = (current_player + 1) % nb_players
    print(
        f"score: {max(scores.values())} player:{max(scores, key=scores.get)} last marble value:{last_marble_value}"
    )
    return max(scores.values())


tests = (
    ((9, 25), 32),
    ((10, 1618), 8317),
    ((13, 7999), 146373),
    ((17, 1104), 2764),
    ((21, 6111), 54718),
    ((30, 5807), 37305),
)

for game_data, expected_score in tests:
    print(f"testing {game_data=} -> {expected_score=}")
    assert solve_part1(*game_data) == expected_score

print("part 1:")
solve_part1(*INPUT)

# part 2
# I thought this would be a case where I need a smart way to optimize, instead of blindly looping more times
# so I started by studying so-called "simple" cases such as (9 players, 25 marbles), freezing 9 and iterating
# over the last marble value and trying to detect a pattern

# I couldn't find anything convincing enough, so I checked Peter Norvig's solution (https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2018.ipynb)
# (as usual, a functional, concise and clean solution) and found out
# it was about finding the right data structure for the problem, but
# that the solution did require to loop 100 more times!

# The key was to use a deque in order to get an O(1) pop() method, as well as get access to the rotate() method
# here is the refactoring of my code from part 1:


def solve_part2(nb_players: int, last_marble_value: int) -> int:
    """Simulates the game, more efficiently than my code from part 1 (thanks Mr Norvig!)

    Required light, but decisive, changes vs my own version above (`solve_part1()`)

    Args:
        nb_players (int): nb of elves taking part
        last_marble_value (int): number of the last marble of the game

    Returns:
        int: the highest score at the end of the game
    """
    circle = deque([0])
    scores = dict(zip(range(nb_players), (0 for _ in range(nb_players))))
    current_player = 0
    for to_insert in tqdm(range(1, last_marble_value + 1)):
        if to_insert % 23:
            circle.rotate(-1)
            circle.append(to_insert)
        else:
            circle.rotate(7)
            scores[current_player] += to_insert + circle.pop()
            circle.rotate(-1)
        current_player = (current_player + 1) % nb_players
    print(f"part 2: {(answer := max(scores.values()))}")
    return answer


solve_part2(403, 7_192_000)
