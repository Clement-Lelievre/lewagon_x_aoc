import hashlib

# i'll try and go for a recursive exploration of the grid

# stop criteria for the recursive function are:
# - being in the vault room (then print the path taken)
# - being stuck, with all doors closed
# - being in a previously visited state (meaning same room and same set of open doors)
PASSCODE = "pvhmgsws"

# cache all "next rooms" locations and label
next_rooms = {
    (x, y): {
        elem: v
        for elem, v in dict(
            zip(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)), ("U", "D", "L", "R"))
        ).items()
        if 0 <= elem[0] <= 3 and 0 <= elem[1] <= 3
    }
    for x in range(4)
    for y in range(4)
}

len_shortest_path = float("inf")
shortest_path = ""


def get_open_doors(current_room: tuple[int, int], current_hash: str) -> dict:
    opened = [
        direction
        for direction, letter in zip("UDLR", current_hash)
        if letter in "bcdef"
    ]
    return {k: v for k, v in next_rooms[current_room].items() if v in opened}


# note: initially I wanted to track visited states (see snippet below this comment)
# but this approach is wrong because the current path keeps changing and so might lead to a new set of open doors
# visited = set()
# if (state := (room, frozenset(open_doors))) in visited: # O(1) lookup
#     return


def explore(
    room: tuple[int, int] = (0, 0),
    current_path: str = PASSCODE,
    verbose: bool = False,
) -> None | str:
    global shortest_path, len_shortest_path
    if not any(
        letter in current_path for letter in "UDLR"
    ):  # reset globals if new game
        len_shortest_path = float("inf")
        if verbose:
            print("reset the globals")
    if room == (3, 3):
        if len((lcp := current_path[len(PASSCODE) :])) < len_shortest_path:
            if verbose:
                print(f"Part 1 : found the vault with {lcp}")
            shortest_path = lcp
            len_shortest_path = len(shortest_path)
        return
    current_hash = hashlib.md5(current_path.encode()).hexdigest()[:4]
    if verbose:
        print(f"{room=} - {current_hash=} - {current_path=}")
    if not (
        open_doors := get_open_doors(
            room, current_hash
        )  # looks like {(1,2): 'U', (2,1): 'L'} etc.
    ):  # stuck, all doors closed
        if verbose:
            print(f"Stuck in {room} with path {current_path}")
        return
    for next_room, direction in open_doors.items():
        if verbose:
            print(f'going from {room} to {next_room} with direction "{direction}"\n')
        explore(next_room, current_path + direction, verbose=verbose)


test_cases = (
    ("kglvqrro", "DDUDRLRRUDRD"),
    ("ihgpwlah", "DDRRRD"),
    ("ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"),
)
for inp, out in test_cases:
    explore(current_path=inp)
    assert shortest_path == out

explore()
print(f"Part 1: {shortest_path}")
# oddly, my code works for my actual input as well as the first test case but not the other two :S

# part 2
longest_path = 0


def explore2(
    room: tuple[int, int] = (0, 0),
    current_path: str = PASSCODE,
    verbose: bool = False,
) -> None | str:
    global longest_path
    if not any(letter in current_path for letter in "UDLR"):
        longest_path = 0  # reset if new game
    if room == (3, 3):
        if (current_length := len(current_path) - len(PASSCODE)) > longest_path:
            if verbose:
                print(f"Found the vault room after {current_length} steps")
            longest_path = current_length
            return current_length
        return
    current_hash = hashlib.md5(current_path.encode()).hexdigest()[:4]
    if verbose:
        print(f"{room=} - {current_hash=} - {current_path=}")
    if not (
        open_doors := get_open_doors(
            room, current_hash
        )  # looks like {(1,2): 'U', (2,1): 'L'} etc.
    ):  # stuck, all doors closed
        if verbose:
            print(f"Stuck in {room} with path {current_path}")
        return
    for next_room, direction in open_doors.items():
        if verbose:
            print(f'going from {room} to {next_room} with direction "{direction}"\n')
        explore2(next_room, current_path + direction)


# a bunch of tests
test_cases = (
    ("ihgpwlah", 370),
    ("kglvqrro", 492),
    ("ulqzkmiv", 830),
)
for inp, out in test_cases:
    explore2(current_path=inp)
    assert longest_path == out

explore2()
print("Part 2:", longest_path)
