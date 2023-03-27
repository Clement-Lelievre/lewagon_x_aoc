import re
from functools import reduce

INPUT = """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
"""

# INPUT="""Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
# process the input
inp = [_ for _ in INPUT.splitlines() if _]
masterdict = {}
pat = re.compile(r"(\w+)\s(-?\d+)")
for row in inp:
    masterdict[row[: row.index(":")]] = {k: int(v) for k, v in pat.findall(row)}

ingredients = list(masterdict.keys())
features = masterdict[ingredients[0]].keys()
# print(features, f"{ingredients=}", f"{d=}", sep="\n" * 2)

# get all possibilities


def all_splits():
    """Generator to get valid splits of ingredients

    Yields:
        _type_: a tuple such that the numbers of ingredients of each type sum to 100
    """
    for i in range(101):
        for j in range(101):
            for k in range(101):
                for l in range(101):
                    if i + j + k + l == 100:
                        yield i, j, k, l


# make a score computer
def compute_score(ingr_numbers: list[int] | tuple[int]) -> int:
    d = masterdict.copy()
    for i in range(len(ingr_numbers)):
        d[ingredients[i]] = {
            k: ingr_numbers[i] * v for k, v in d[ingredients[i]].items()
        }
    ingr_dicts = d
    cookie_dict = {
        feature: sum(ingr_dict[feature] for ingr_dict in ingr_dicts.values())
        for feature in features
        if feature != "calories"
    }
    score = reduce(lambda x, y: x * y, (max(nb, 0) for nb in cookie_dict.values()))
    return score


# iterate over possibilities using the score computer
# best = 0
# for sp in all_splits():
#     if (s := compute_score(sp)) > best:
#         best = s


# print(best)

# part 2
def compute_score(ingr_numbers: list[int] | tuple[int]) -> int:
    d = masterdict.copy()
    for i in range(len(ingr_numbers)):
        d[ingredients[i]] = {
            k: ingr_numbers[i] * v for k, v in d[ingredients[i]].items()
        }
    ingr_dicts = d
    cookie_dict = {
        feature: sum(ingr_dict[feature] for ingr_dict in ingr_dicts.values())
        for feature in features
    }
    if cookie_dict["calories"] != 500:
        return 0
    cookie_dict.pop("calories")
    score = reduce(lambda x, y: x * y, (max(nb, 0) for nb in cookie_dict.values()))
    return score


# iterate over possibilities using the score computer
best = 0
for sp in all_splits():
    if (s := compute_score(sp)) > best:
        best = s

print(best)
