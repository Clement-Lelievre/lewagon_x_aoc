import re
from itertools import combinations

INPUT = """<x=1, y=2, z=-9>
<x=-1, y=-9, z=-4>
<x=17, y=6, z=8>
<x=12, y=4, z=2>"""

TEST_INPUT = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""


NB_PAT = re.compile(r"(-?\d+)")
ROWS = INPUT.splitlines()
positions = {i: list(map(int, NB_PAT.findall(ROWS[i]))) for i in range(len(ROWS))}
velocities = {i: [0, 0, 0] for i in positions}

NB_STEPS = 1_000

for _ in range(NB_STEPS):
    # update gravity
    for ind1, ind2 in combinations(velocities, 2):
        for i in range(3):
            if (pos1 := positions[ind1][i]) < (pos2 := positions[ind2][i]):
                velocities[ind1][i] += 1
                velocities[ind2][i] -= 1
            elif pos1 > pos2:
                velocities[ind1][i] -= 1
                velocities[ind2][i] += 1
    # update positions
    for k in positions:
        for i in range(3):
            positions[k][i] += velocities[k][i]


# get total energy
total_energy = sum(
    sum(map(abs, positions[k])) * sum(map(abs, velocities[k])) for k in positions
)
print(f"{total_energy=}")

# part 2
# let us find the cycle length for each planet on each of the three dimensions
# we'll then find the least common multiple between those numbers
ROWS = TEST_INPUT.splitlines()
positions = {i: list(map(int, NB_PAT.findall(ROWS[i]))) for i in range(len(ROWS))}
velocities = {i: [0, 0, 0] for i in positions}

initial_x = [[positions[i][0], 0] for i in positions]
initial_y = [[positions[i][1], 0] for i in positions]
initial_z = [[positions[i][2], 0] for i in positions]

# find cycle length for the x dimension
c = 0
while True:
    # update gravity
    for ind1, ind2 in combinations(velocities, 2):
        if (pos1 := positions[ind1][0]) < (pos2 := positions[ind2][0]):
            velocities[ind1][0] += 1
            velocities[ind2][0] -= 1
        elif pos1 > pos2:
            velocities[ind1][0] -= 1
            velocities[ind2][0] += 1
    # update positions
    for k in positions:
        positions[k][0] += velocities[k][0]
    if [[positions[i][0], 0] for i in positions] == initial_x:
        break
    c += 1
print(c)

# find cycle length for the y dimension
c = 0
while True:
    # update gravity
    for ind1, ind2 in combinations(velocities, 2):
        if (pos1 := positions[ind1][1]) < (pos2 := positions[ind2][1]):
            velocities[ind1][1] += 1
            velocities[ind2][1] -= 1
        elif pos1 > pos2:
            velocities[ind1][1] -= 1
            velocities[ind2][1] += 1
    # update positions
    for k in positions:
        positions[k][1] += velocities[k][1]
    if [[positions[i][1], 0] for i in positions] == initial_y:
        break
    c += 1
print(c)

# find cycle length for the z dimension
c = 0
while True:
    # update gravity
    for ind1, ind2 in combinations(velocities, 2):
        if (pos1 := positions[ind1][2]) < (pos2 := positions[ind2][2]):
            velocities[ind1][2] += 1
            velocities[ind2][2] -= 1
        elif pos1 > pos2:
            velocities[ind1][2] -= 1
            velocities[ind2][2] += 1
    # update positions
    for k in positions:
        positions[k][2] += velocities[k][2]
    if [[positions[i][2], 0] for i in positions] == initial_z:
        break
    c += 1
print(c)
