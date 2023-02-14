"Marble mania"
INPUT = 403, 71920


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
    print(f"score: {max(scores.values())}")
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

print(solve_part1(*INPUT))

# part 2
