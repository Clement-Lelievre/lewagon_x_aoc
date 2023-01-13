import hashlib

# i'll try and go for a recursive exploration of the grid

# stop criteria for the recursive function are:
# - being in the vault room (then print the path taken)
# - being stuck, with all doors closed
# - being in a previously visited state (meaning same room and same set of open doors)
PASSCODE = "hijkl"
md5 = hashlib.md5(PASSCODE.encode())
visited = set()
current_hash = md5.hexdigest()


def explore(room: tuple[int, int], current_path: str = PASSCODE) -> None:
    if room == (3, 3):
        print(f"Found the vault room after {current_path}")
        return
