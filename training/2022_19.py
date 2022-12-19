import re

INPUT = """Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 4: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 4 ore and 14 obsidian.
Blueprint 5: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 9 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 6: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 17 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 7: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 13 obsidian.
Blueprint 8: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 2 ore and 8 obsidian.
Blueprint 9: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 4 ore and 7 obsidian.
Blueprint 10: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 6 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 12: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 13: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 14: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 9 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 15: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 13 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 16: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 17: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 6 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 18: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 19: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 20: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 21: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 22: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 23: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 5 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 11 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 25: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 26: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 5 clay. Each geode robot costs 3 ore and 18 obsidian.
Blueprint 27: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 2 ore and 13 obsidian.
Blueprint 28: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 9 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 29: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 4 ore and 16 obsidian."""
INPUT = """Blueprint 1:Each ore robot costs 4 ore.Each clay robot costs 2 ore.Each obsidian robot costs 3 ore and 14 clay.Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2:Each ore robot costs 2 ore.Each clay robot costs 3 ore.Each obsidian robot costs 3 ore and 8 clay.Each geode robot costs 3 ore and 12 obsidian."""

recipes = [recipe for recipe in INPUT.splitlines() if recipe.strip()]
recipe_nb_extractor = re.compile(r"(\d+):")
price_extractor = re.compile(r"\d+.*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)")


class Money(tuple):
    """A helper class to easily check if I've enough money to buy a given robot type"""

    def __init__(self, levels: tuple) -> None:
        self.levels = levels
        self.ore = self.levels[0]
        self.clay = self.levels[1]
        self.obsidian = self.levels[2]

    def __ge__(self, other_money) -> bool:
        return all(
            self.levels[i] >= other_money.levels[i] for i in range(len(self.levels))
        )

    def __mul__(self, n: int) -> "Money":
        return Money((self.ore * n, self.clay * n, self.obsidian * n))


def compute_max_nb_geodes(
    recipe: str, start_nb_ore_robots: int = 1, time: int = 24
) -> int:
    total_time_allowed = time
    current_money = Money((0, 0, 0))  # initial money
    nb_ore_robot, nb_clay_robot, nb_obsidian_robot, nb_geode_robot = (
        start_nb_ore_robots,
        0,
        0,
        0,
    )  # initial robots
    nb_geodes = 0
    price_data = price_extractor.search(recipe)
    ore_robot_price = Money(
        (int(price_data.group(1)), 0, 0)
    )  # expressed in ore, clay, obsidian required
    clay_robot_price = Money(
        (int(price_data.group(2)), 0, 0)
    )  # expressed in ore, clay, obsidian required
    obsidian_robot_price = Money(
        (int(price_data.group(3)), int(price_data.group(4)), 0)
    )  # expressed in ore, clay, obsidian required
    geode_robot_price = Money(
        (int(price_data.group(5)), 0, int(price_data.group(6)))
    )  # expressed in ore, clay, obsidian required

    # strategy: buy as many geodes as possible, then buy as many obsidian as possible, then buy as many clay as possible, then buy as many ore as possible
    while time:
        print(f"== Minute {total_time_allowed - time +1} ==")
        (
            bought_geode_robot,
            bought_obsidian_robot,
            bought_clay_robot,
            bought_ore_robot,
        ) = (False, False, False, False)
        # manage possible transactions: consume resources but do not add robots just yet as it takes one minute to build them
        if current_money >= geode_robot_price:
            bought_geode_robot = True
            current_money = Money(
                (
                    current_money.ore - geode_robot_price.ore,
                    current_money.clay - geode_robot_price.clay,
                    current_money.obsidian - geode_robot_price.obsidian,
                )
            )
            print(f"bought geode robot, {current_money=} after the transaction")
        elif current_money >= obsidian_robot_price:
            bought_obsidian_robot = True
            current_money = Money(
                (
                    current_money.ore - obsidian_robot_price.ore,
                    current_money.clay - obsidian_robot_price.clay,
                    current_money.obsidian - obsidian_robot_price.obsidian,
                )
            )
            print(f"bought obsidian robot, {current_money=} after the transaction")
        elif current_money >= clay_robot_price:
            bought_clay_robot = True
            current_money = Money(
                (
                    current_money.ore - clay_robot_price.ore,
                    current_money.clay - clay_robot_price.clay,
                    current_money.obsidian - clay_robot_price.obsidian,
                )
            )
            print(f"bought clay robot, {current_money=} after the transaction")
        elif current_money >= ore_robot_price:
            bought_ore_robot = True
            current_money = Money(
                (
                    current_money.ore - ore_robot_price.ore,
                    current_money.clay - ore_robot_price.clay,
                    current_money.obsidian - ore_robot_price.obsidian,
                )
            )
            print(f"bought ore robot, {current_money=} after the transaction")
        # manage robot activity
        if nb_ore_robot:
            current_money = Money(
                (
                    current_money.ore + nb_ore_robot,
                    current_money.clay,
                    current_money.obsidian,
                )
            )
            print(
                f"{nb_ore_robot} ore-collecting robot collects {nb_ore_robot} ore; you now have {current_money.ore} ore."
            )
        if nb_clay_robot:
            current_money = Money(
                (
                    current_money.ore,
                    current_money.clay + nb_clay_robot,
                    current_money.obsidian,
                )
            )
            print(
                f"{nb_clay_robot} clay-collecting robot collects {nb_clay_robot} clay; you now have {current_money.clay} clay."
            )
        if nb_obsidian_robot:
            current_money = Money(
                (
                    current_money.ore,
                    current_money.clay,
                    current_money.obsidian + nb_obsidian_robot,
                )
            )
            print(
                f"{nb_obsidian_robot} obsidian-collecting robot collects {nb_obsidian_robot} obsidian; you now have {current_money.obsidian} obsidian."
            )
        if nb_geode_robot:
            nb_geodes += nb_geode_robot
            print(
                f"{nb_geode_robot} geode-cracking robot cracks {nb_geode_robot} geode; you now have {nb_geodes} open geodes."
            )
        # print(f'{current_money=} after robot activity')
        # update robot numbers in case a transaction occurred
        if bought_ore_robot:
            nb_ore_robot += 1
            print(
                f"The new ore-collecting robot is ready; you now have {nb_ore_robot} of them."
            )
        if bought_clay_robot:
            nb_clay_robot += 1
            print(
                f"The new clay-collecting robot is ready; you now have {nb_clay_robot} of them."
            )
        if bought_obsidian_robot:
            nb_obsidian_robot += 1
            print(
                f"The new obsidian-collecting robot is ready; you now have {nb_obsidian_robot} of them"
            )
        if bought_geode_robot:
            nb_geode_robot += 1
            print(
                f"The new geode-cracking robot is ready; you now have {nb_geode_robot} of them"
            )
        # update timer
        time -= 1
        print("\n")
    return nb_geodes


def get_quality_level(recipe: str) -> int:
    return int(recipe_nb_extractor.search(recipe).group(1)) * compute_max_nb_geodes(
        recipe
    )


compute_max_nb_geodes(recipes[0])
# answer = sum(map(get_quality_level, recipes))
# print(answer)


# part 2
