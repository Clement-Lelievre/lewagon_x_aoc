import re
from itertools import combinations
from functools import reduce

INPUT = """<x=1, y=2, z=-9>
<x=-1, y=-9, z=-4>
<x=17, y=6, z=8>
<x=12, y=4, z=2>"""


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
print(f"part 1: {total_energy=}")

# part 2
# let us find the cycle length for each planet on each of the three dimensions
# we'll then find the least common multiple between those numbers
ROWS = INPUT.splitlines()

initial_positions = {
    i: list(map(int, NB_PAT.findall(ROWS[i]))) for i in range(len(ROWS))
}
initial_pos_veloc = {
    k: [[initial_positions[i][k], 0] for i in initial_positions] for k in range(3)
}
cycle_lengths = []
for dim in range(3):  # each of the three dimensions x, y z
    c = 0
    positions = initial_positions
    velocities = {i: [0, 0, 0] for i in initial_positions}
    while True:
        # update gravity
        for ind1, ind2 in combinations(velocities, 2):
            if (pos1 := positions[ind1][dim]) < (pos2 := positions[ind2][dim]):
                velocities[ind1][dim] += 1
                velocities[ind2][dim] -= 1
            elif pos1 > pos2:
                velocities[ind1][dim] -= 1
                velocities[ind2][dim] += 1
        # update positions
        for k in positions:
            positions[k][dim] += velocities[k][dim]
        c += 1
        if [
            [positions[i][dim], velocities[i][dim]] for i in positions
        ] == initial_pos_veloc[dim]:
            cycle_lengths.append(c)
            break

print(f"{cycle_lengths=}")

# now let's find the least common multiple of all three numbers in my <cycle_length> array
def prime_factorization(n: int) -> list[tuple[int, int]]:
    """Returns the prime factorization of n as a list of (prime, exponent) tuples

    Returns:
        list[tuple[int, int]]: list of (prime, exponent) tuples
    """
    factors = []
    d = 2
    while n:
        exp = 0
        while n % d == 0:
            exp += 1
            n //= d
        if exp:
            factors.append((d, exp))
        d += 1
        if d**2 > n:
            if n:
                factors.append((n, 1))
            break
    return factors


def least_common_multiple(*args) -> int:
    """returns the LCM of all the integers passed, using the prime factor decomposition method

    Returns:
        int: the LCM
    """
    prime_factors = []
    for nb in args:
        prime_factors.extend(prime_factorization(nb))
    # retain each unique number once, with the highest exponent found for this number in the list
    unique_primes = set(prime for prime, _ in prime_factors)
    unique_prime_factors = [
        (elem, max(expo for nb, expo in prime_factors if nb == elem))
        for elem in unique_primes
    ]
    print(f"{prime_factors=}")
    print(f"{unique_prime_factors=}")
    answer = reduce(
        lambda x, y: x * y, (pow(base, exp) for base, exp in unique_prime_factors)
    )
    return answer


answer = least_common_multiple(*cycle_lengths)
print(f"part 2: {answer}")
