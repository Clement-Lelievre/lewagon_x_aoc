# https://adventofcode.com/2016/day/1

INPUT = """L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, 
R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, 
R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, 
R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, 
R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, 
R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4
"""

########################################################### 
# PART 1

coord = [0, 0]  # initial spot
exposure = "N"  # initial exposure is North
directions = INPUT.replace("\n", "").split(", ")


def new_exposure(direction: str, exposure: str) -> str:
    """computes and returns new exposure

    Args:
        direction (str): _description_
        exposure (str): _description_

    Returns:
        str: _description_
    """
    if direction == "R":
        if exposure == "N":
            return "E"
        elif exposure == "E":
            return "S"
        elif exposure == "S":
            return "W"
        return "N"
    # the else block
    if exposure == "N": 
        return "W"
    elif exposure == "W":
        return "S"
    elif exposure == "S":
        return "E"
    return "N"


def new_coord(coord: list[int], exposure: str, move: str) -> list[int]:
    """computes and returns the new coordinates

    Args:
        coord (list[int]): current coord
        exposure (str): current exposure
        move (str): move (direction + distance)

    Returns:
        list[int]: new coord
    """
    em = exposure + move[0]
    if em in ("NL", "SR"):
        coord[0] -= int(move[1:])
    elif em in ("NR", "SL"):
        coord[0] += int(move[1:])
    elif em in ("EL", "WR"):
        coord[1] += int(move[1:])
    else:
        coord[1] -= int(move[1:])
    return coord


# for move in directions:
#     coord = new_coord(coord, exposure, move)
#     exposure = new_exposure(move[0], exposure)

# print(sum(list(map(abs, coord))))

########################################################### 
# PART 2

def passed_through_coords(coord: list[int], exposure: str, move: str) -> list[int]:
    """computes and returns the new coordinates, ALL the coordinates which we go through, 
    not only destination spots

    Args:
        coord (list[int]): current coord
        exposure (str): current exposure
        move (str): move (direction + distance)

    Returns:
        list[int]: new coord
    """
    new_coords = []
    em = exposure + move[0]
    if em in ("NL", "SR"):
        for i in range(1, int(move[1:])+1):
            new = coord.copy()
            new[0] -= i
            new_coords.append(new)
    elif em in ("NR", "SL"):
        for i in range(1, int(move[1:])+1):
            new = coord.copy()
            new[0] += i
            new_coords.append(new)
    elif em in ("EL", "WR"):
        for i in range(1, int(move[1:])+1):
            new = coord.copy()
            new[1] += i
            new_coords.append(new)
    else:
        for i in range(1, int(move[1:])+1):
            new = coord.copy()
            new[1] -= i
            new_coords.append(new)
    return new_coords
    

coord = [0,0]
all_coords = [[0,0]]
exposure = "N"  # initial exposure is North
directions = INPUT.replace("\n", "").split(", ")
found = False
i = 0
while not found:
    move = directions[i]
    new_coords = passed_through_coords(coord, exposure, move)
    coord = new_coords[-1]
    for item in new_coords:
        if item in all_coords:
            print(sum(list(map(abs, item))))
            found = True
        else:
            all_coords.append(item)
    exposure = new_exposure(move[0], exposure)
    i += 1

