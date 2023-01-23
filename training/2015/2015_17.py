from itertools import combinations
from multiprocessing.connection import answer_challenge

containers = sorted(
    [
        50,
        44,
        11,
        49,
        42,
        46,
        18,
        32,
        26,
        40,
        21,
        7,
        18,
        43,
        10,
        47,
        36,
        24,
        22,
        40,
    ]
)

qty = 150
# let's find out the max nb of containers we can ever use
for i in range(len(containers)):
    if (s := sum(containers[:i])) > qty:
        break

answer = 0

max_nb_containers = i - 1
for nb_containers in range(2, max_nb_containers + 1):
    for comb in combinations(containers, nb_containers):
        if sum(comb) == qty:
            answer += 1

print(answer)

# part 2
unknown = True
answer = 0
nb_containers = 2
while unknown:
    for comb in combinations(containers, nb_containers):
        if sum(comb) == qty:
            unknown = False
            answer += 1
    nb_containers += 1

print(answer)
