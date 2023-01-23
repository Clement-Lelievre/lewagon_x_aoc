from collections import namedtuple
import re
from itertools import combinations

BIG = 10**999

# if I buy nothing, at each turn I inflict -1 and I suffer from 8, hence I'd lose the game
# I must buy exactly one weapon, but rings (at most 2) and armor (at most 1) are optional
# so I will add lines representing buying nothing to rings and armor so that then I only have to iterate over combinations

Item = namedtuple("Item", "name cost damage armor")
conv = lambda n: int(n) if n.isdigit() else n
load = lambda lines, func=conv: [
    Item(*map(func, re.split(r"\s{2,}", l))) for l in lines
]

weapons = load(
    """\
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
""".splitlines()
)

armors = load(
    """\
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
Nothing       0     0       0
""".splitlines()
)

rings = load(
    """\
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
Nothing       0     0       0
Nothing       0     0       0
""".splitlines()
)

weapons = sorted(weapons, key=lambda x: x.cost)
armour = sorted(armors, key=lambda x: x.cost)
rings = sorted(rings, key=lambda x: x.cost)

stats = {
    "boss": {"damage": 8, "armor": 2, "hit points": 100},
    "me": {"damage": 0, "armor": 0, "hit points": 100},
}
my_stats = stats.get("me")
boss_stats = stats.get("boss")


def fight(
    p1_harm,
    p2_harm,
    p1hit_points=my_stats["hit points"],
    p2hit_points=boss_stats["hit points"],
) -> int:
    """Simulates a fight. 2 possible outcomes: win or lose. Player 1 (me) starts.

    Args:
        p1_harm (str, optional):  Defaults to 'me'.
        p2_harm (str, optional):  Defaults to 'boss'.

    Returns:
        int: 1 if p1 wins else 0
    """
    # print(f'{p2hit_points=}, {p1hit_points=}, {p1_harm=}, {p2_harm=}')
    while True:
        p2hit_points -= p1_harm
        if p2hit_points <= 0:
            return 1
        p1hit_points -= p2_harm
        if p1hit_points <= 0:
            return 0


def buy_items(items: list[Item]) -> None:
    """Buys an item from the shop and updates the stats dict accordingly"""
    my_stats["damage"] = 0
    my_stats["armor"] = 0
    for item in items:
        my_stats["damage"] += item.damage
        my_stats["armor"] += item.armor


def find_answer_part1():
    ans = BIG
    for weapon in weapons:
        for armor in armors:
            for ring1, ring2 in combinations(rings, 2):
                buy_items([weapon, armor, ring1, ring2])
                p1_harm = max(stats.get("me")["damage"] - stats.get("boss")["armor"], 1)
                p2_harm = max(stats.get("boss")["damage"] - stats.get("me")["armor"], 1)
                if fight(p1_harm, p2_harm):
                    cost = sum(item.cost for item in (weapon, armor, ring1, ring2))
                    if cost < ans:
                        ans = cost
    return (
        ans
        if ans != BIG
        else "It is impossible to win, even win the most expensive items"
    )


print("part 1", find_answer_part1())

# part 2
def find_answer_part2():
    ans = 0
    for weapon in weapons:
        for armor in armors:
            for ring1, ring2 in combinations(rings, 2):
                buy_items([weapon, armor, ring1, ring2])
                p1_harm = max(stats.get("me")["damage"] - stats.get("boss")["armor"], 1)
                p2_harm = max(stats.get("boss")["damage"] - stats.get("me")["armor"], 1)
                if fight(p1_harm, p2_harm) == 0:
                    cost = sum(item.cost for item in (weapon, armor, ring1, ring2))
                    if cost > ans:
                        ans = cost
    return ans if ans else "It is impossible to win, even win the most expensive items"


print("part 2", find_answer_part2())
