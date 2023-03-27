from itertools import permutations
from tqdm import tqdm

INPUT = """Alice would lose 57 happiness units by sitting next to Bob.
Alice would lose 62 happiness units by sitting next to Carol.
Alice would lose 75 happiness units by sitting next to David.
Alice would gain 71 happiness units by sitting next to Eric.
Alice would lose 22 happiness units by sitting next to Frank.
Alice would lose 23 happiness units by sitting next to George.
Alice would lose 76 happiness units by sitting next to Mallory.
Bob would lose 14 happiness units by sitting next to Alice.
Bob would gain 48 happiness units by sitting next to Carol.
Bob would gain 89 happiness units by sitting next to David.
Bob would gain 86 happiness units by sitting next to Eric.
Bob would lose 2 happiness units by sitting next to Frank.
Bob would gain 27 happiness units by sitting next to George.
Bob would gain 19 happiness units by sitting next to Mallory.
Carol would gain 37 happiness units by sitting next to Alice.
Carol would gain 45 happiness units by sitting next to Bob.
Carol would gain 24 happiness units by sitting next to David.
Carol would gain 5 happiness units by sitting next to Eric.
Carol would lose 68 happiness units by sitting next to Frank.
Carol would lose 25 happiness units by sitting next to George.
Carol would gain 30 happiness units by sitting next to Mallory.
David would lose 51 happiness units by sitting next to Alice.
David would gain 34 happiness units by sitting next to Bob.
David would gain 99 happiness units by sitting next to Carol.
David would gain 91 happiness units by sitting next to Eric.
David would lose 38 happiness units by sitting next to Frank.
David would gain 60 happiness units by sitting next to George.
David would lose 63 happiness units by sitting next to Mallory.
Eric would gain 23 happiness units by sitting next to Alice.
Eric would lose 69 happiness units by sitting next to Bob.
Eric would lose 33 happiness units by sitting next to Carol.
Eric would lose 47 happiness units by sitting next to David.
Eric would gain 75 happiness units by sitting next to Frank.
Eric would gain 82 happiness units by sitting next to George.
Eric would gain 13 happiness units by sitting next to Mallory.
Frank would gain 77 happiness units by sitting next to Alice.
Frank would gain 27 happiness units by sitting next to Bob.
Frank would lose 87 happiness units by sitting next to Carol.
Frank would gain 74 happiness units by sitting next to David.
Frank would lose 41 happiness units by sitting next to Eric.
Frank would lose 99 happiness units by sitting next to George.
Frank would gain 26 happiness units by sitting next to Mallory.
George would lose 63 happiness units by sitting next to Alice.
George would lose 51 happiness units by sitting next to Bob.
George would lose 60 happiness units by sitting next to Carol.
George would gain 30 happiness units by sitting next to David.
George would lose 100 happiness units by sitting next to Eric.
George would lose 63 happiness units by sitting next to Frank.
George would gain 57 happiness units by sitting next to Mallory.
Mallory would lose 71 happiness units by sitting next to Alice.
Mallory would lose 28 happiness units by sitting next to Bob.
Mallory would lose 10 happiness units by sitting next to Carol.
Mallory would gain 44 happiness units by sitting next to David.
Mallory would gain 22 happiness units by sitting next to Eric.
Mallory would gain 79 happiness units by sitting next to Frank.
Mallory would lose 16 happiness units by sitting next to George.
"""

# my plan: trying all combinations (not trying to find a smart way, at this stage)
# 1) process the input to extract the meaningul parts -> get the total hapiness change for every couple (sum the two parts)
# 2) get all the possible settings (itertools)
# 3) (optional) some settings are actually the same because the table is circular (e.g. a,b,c,d and d,a,b,c are the same for that matter)
# -> create function to identify these (onmy needed if processing all possibilities is too greedy)
# 4) (optional) apply abovementioned function to the set of settings to get all unique settings
# 5) use the input from 1) to compute scores
# 6) the answer is the max score

# 1
inp = [_.replace(".", "") for _ in INPUT.split("\n") if _]
names = set(row[0] for row in inp)
inp = [((r := row.split())[0][0], r[2], r[3], r[-1][0]) for row in inp]
inp = [
    ("".join(sorted(e[0] + e[-1])), int(e[2]) if e[1] != "lose" else -1 * int(e[2]))
    for e in inp
]
couples = set(e[0] for e in inp)
couple_total_happiness = dict(
    zip(couples, [sum(e[1] for e in inp if e[0] == couple) for couple in couples])
)
print(couple_total_happiness)
# 2
perms = permutations(names, len(names))
nb_people = len(names)
# 5
best = 0

for perm in tqdm(perms):
    perm = "".join(perm)
    score = sum(
        couple_total_happiness[
            "".join(
                sorted(perm[i : i + 2] if i + 1 < nb_people else perm[-1] + perm[0])
            )
        ]
        for i in range(nb_people)
    )
    if score > best:
        best = score
# 6
print(best)

# part 2
names.add("Z")  # I am Z
for name in names:
    if name != "Z":
        couple_total_happiness[name + "Z"] = 0
# then redo the same
perms = permutations(names, len(names))
nb_people = len(names)
best = 0

for perm in tqdm(perms):
    perm = "".join(perm)
    score = sum(
        couple_total_happiness[
            "".join(
                sorted(perm[i : i + 2] if i + 1 < nb_people else perm[-1] + perm[0])
            )
        ]
        for i in range(nb_people)
    )
    if score > best:
        best = score
# 6
print(best)

# in the end, there was no need to optimize as this ran in under 2 seconds on an average machine
