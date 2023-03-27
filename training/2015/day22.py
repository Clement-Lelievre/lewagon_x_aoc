stats = {
    "boss": {"damage": 9, "hit points": 51},
    "me": {"damage": 0, "mana": 500, "hit points": 50, "armor": 0},
}
my_stats = stats.get("me")
portfolio = my_stats["mana"]
boss_stats = stats.get("boss")
mana = stats["me"]["mana"]
spell_costs = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229,
}
spell_min_cost = min(spell_costs.values())
effect_timer = 0


def fight():

    while True:
        if mana < spell_min_cost:  #  If you cannot afford to cast any spell, you lose
            return 0
        spell = "to do"
        portfolio -= spell_costs[spell]


# What is the least amount of mana you can spend and still win the fight?
# (Do not include mana recharge effects as "spending" negative mana.)
