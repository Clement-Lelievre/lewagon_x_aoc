"""AoC 2023 day 24
https://adventofcode.com/2023/day/24"""
import argparse
from itertools import combinations

# in part 1 we ignore the z axis
# parse the input, storing x,y (positions) and vx, vy (velocities)
# compute a and b coeefs in the equation y = ax + b
# iterate over all pairs of ax +b, solving for x in ax + b = cx + d => x = (d - b)/(a - c)

TEST_DATA = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def parse_input(text: str):
    xys, velocities = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        x, y = [int(nb) for nb in line.split("@")[0].split(",")[:2]]
        xys.append((x, y))
        vx, vy = x, y = [int(nb) for nb in line.split("@")[1].split(",")[:2]]
        velocities.append((vx, vy))
    return xys, velocities


def compute_coeffs(x: int, y: int, vx: int, vy: int) -> tuple[int]:
    """From 2 couples of points, compute the coefficients of the line equation a and b in y = ax + b

    Args:
        x (int): _description_
        y (int): _description_
        vx (int): _description_
        vy (int): _description_

    Returns:
        tuple[int]: _description_
    """
    x1, y1 = x, y
    x2, y2 = x + vx, y + vy
    return (y2 - y1) / (x2 - x1), (x2 * y1 - x1 * y2) / (x2 - x1), x1, vx


def solve_p1(data: str, min_: int, max_: int) -> int:
    answer = 0
    xys, velocities = parse_input(data)
    a_and_bs = [
        compute_coeffs(x, y, vx, vy) for (x, y), (vx, vy) in zip(xys, velocities)
    ]
    for pair in combinations(a_and_bs, 2):
        a1, b1, x1, vx1 = pair[0]
        a2, b2, x2, vx2 = pair[1]
        if a1 == a2:
            continue
        x = (b2 - b1) / (a1 - a2)
        y = a1 * x + b1
        if (
            min_ <= x <= max_
            and min_ <= y <= max_
            and (x >= x1 if vx1 >= 0 else x < x1)
            and (x >= x2 if vx2 >= 0 else x < x2)
        ):
            answer += 1
    print(f"{answer=}")
    return answer


if __name__ == "__main__":
    assert solve_p1(TEST_DATA, 7, 27) == 2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path) as f:
        text = f.read()
    solve_p1(text, 200_000_000_000_000, 400_000_000_000_000)
