from itertools import combinations
from tqdm import tqdm
from functools import reduce
from typing import Iterable

INPUT = """1
3
5
11
13
17
19
23
29
31
37
41
43
47
53
59
67
71
73
79
83
89
97
101
103
107
109
113"""


# constraints:
# three groups of exactly the same weight, containing every packet exaclty once
# 1st group needs as few packages as possible
#  if there are multiple ways to arrange the packages such that the fewest possible are in the first group, pick the set
# where the product of weights of packets in group 1 is the lowest
NB_COMPARTMENTS = 3
weights = list(map(int, INPUT.splitlines()))
print(f"{len(weights)} weights")
# COMPARTMENT_WEIGHT = sum(weights)//3
# assert COMPARTMENT_WEIGHT*10//10 == COMPARTMENT_WEIGHT, 'impossible task'
# print(f'each compartment weighs {COMPARTMENT_WEIGHT} kg')


# for i in range(len(weights)):
#     if sum(weights[-i-1:]) >= COMPARTMENT_WEIGHT:
#         min_nb_packages = i+1
#         print(f'{min_nb_packages=}')
#         break

# the plan: find the lowest nb of packages that sum to 508, then determine if 508 can be reached again twice using the remaining packages
# if so, that's a valid set with the minimum number of packages! all that's left to do is work out the minimal product
# (aka quantum entanglement in the challenge)  with reduce()

# for nb_packages in range(min_nb_packages, len(weights)-min_nb_packages-1): # the upper bound is even lower, but this is good enough
#     candidates = []
#     print(f'Checking {nb_packages} assortments...')
#     candidates = [comb for comb in combinations(weights, nb_packages) if sum(comb) == COMPARTMENT_WEIGHT]
#     if len(candidates) >= NB_COMPARTMENTS: # necessary but not sufficient, as some packages may be used more than once
#         break

# print(f'Found {len(candidates)} settings for {nb_packages} packages')
# in reality I'd need to foresee the case where nb_packages doesn't yield any valid setup below, but here luckily it works

# weights = set(weights)
# valid_sets = []
# for comb1 in tqdm(candidates):
#     found = False
#     remaining_packages = weights.difference(comb1)
#     for nb_packages in range(min_nb_packages, len(weights)):
#         for comb2 in combinations(remaining_packages, nb_packages):
#             if sum(comb2) == COMPARTMENT_WEIGHT: # if I found a second combination, I'm done as the remaining packages must sum to 508 too
#                 valid_sets.append(comb1)
#                 found = True
#                 break
#         if found:
#             break


# print(f'''{len(valid_sets)} combinations found containing {len(valid_sets[0])} packages;\n
#       e.g.: {[valid_sets[i] for i in range(3)]}''')

# # it turns out that of 299 sets of 6 packages that sum up to 508,
# # all of them are valid in the sense that they allow the whole set of all packages to be split into 3 groups of 508!

# print('part 1:', min(reduce(lambda x,y:x*y, vs) for vs in valid_sets))

# part 2 ##############################################################################################################
NB_COMPARTMENTS = 4
COMPARTMENT_WEIGHT = sum(weights) // NB_COMPARTMENTS
weights = list(map(int, INPUT.splitlines()))
print(f"{COMPARTMENT_WEIGHT}")

# find theoretical min nb of packages
for i in range(len(weights)):
    if sum(weights[-i - 1 :]) >= COMPARTMENT_WEIGHT:
        min_nb_packages = i + 1
        print(f" theoretical {min_nb_packages=}")
        break

# find actual min nb of packages possible
candidates = []
while True:
    for comb in tqdm(combinations(weights, min_nb_packages)):
        if sum(comb) == COMPARTMENT_WEIGHT:
            candidates.append(comb)
    if candidates:
        break
    min_nb_packages += 1

print(
    "the actual minimum nb of packages that sums up to ",
    COMPARTMENT_WEIGHT,
    " is ",
    min_nb_packages,
    f"({len(candidates)} candidates)",
)


weights = set(map(int, INPUT.splitlines()))


### DIRTY BUT WORKING SOLUTION BELOW, BASICALLY BETTING ON THE FACT THAT THE FIRST COMPARTMENT WILL BE
#### OF `min_nb_packages` length. IT BASICALLY PULLS OUT ALL POSSIBLE REARRANGEMENTS OF THAT LENGTH THEN GETS THE MINIMUM Q.E.

func = lambda comb: reduce(lambda x, y: x * y, comb)
candidates = [
    comb
    for comb in tqdm(combinations(weights, min_nb_packages))
    if sum(comb) == COMPARTMENT_WEIGHT
]

print(min(map(func, candidates)))

# if this does not yield the solution, it means the actual best arrangement of packages has at minimum more than `min_nb_packages` packages
# all there is to do is iterate over this process: increment `min_nb_packages` by 1 and rerun the above, till you get it right
# it turns out this works on the first run
