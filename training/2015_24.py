from itertools import combinations
from tqdm import tqdm
from functools import reduce

INPUT = '''1
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
113'''

# constraints:
# three groups of exactly the same weight, containing every packet exaclty once
# 1st group needs as few packages as possible
#  if there are multiple ways to arrange the packages such that the fewest possible are in the first group, pick the set 
# where the product of weights of packets in group 1 is the lowest

weights = list(map(int, INPUT.splitlines()))
compartment_weight = sum(weights)//3
assert compartment_weight*10//10 == compartment_weight, 'impossible task'
print(f'each compartment weighs {compartment_weight} kg')


for i in range(len(weights)):
    if sum(weights[-i-1:]) >= compartment_weight:
        min_nb_packages = i+1
        print(f'{min_nb_packages=}')
        break
    
# the plan: find the lowest nb of packages that sum to 508, then determine if 508 can be reached again using the remaining packages 
# if so, that's a valid set with the minimum number of packages! all that's left to do is work out the minimal product with reduce()

candidates = []
found_min_nb = False
for nb_packages in range(min_nb_packages, len(weights)):
    print(f'checking {nb_packages} assortments...')
    for comb in combinations(weights, nb_packages):
        if sum(comb) == compartment_weight:
            candidates.append(comb)
    if candidates:
        break
    
# in reality I'd need to foresee the case where nb_packages doesn't yield any valid setup below, but here luckily it works
    
weights = set(weights)
valid_sets = []
for comb1 in tqdm(candidates):
    found = False
    remaining_packages = weights.difference(comb1)
    for nb_packages in range(min_nb_packages, len(weights)):
        for comb2 in combinations(remaining_packages, nb_packages):
            if sum(comb2) == compartment_weight:
                valid_sets.append(comb1) 
                found = True
                break
        if found:
            break


print(f'''{len(valid_sets)} combinations found containing {len(valid_sets[0])} packages;\n
      e.g.: {[valid_sets[i] for i in range(3)]}''')


print(min(reduce(lambda x,y:x*y, vs) for vs in valid_sets))
    
# part 2
