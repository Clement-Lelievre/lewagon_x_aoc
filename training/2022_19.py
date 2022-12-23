import re
from random import randint
from multiprocessing import Pool
from functools import reduce
from tqdm import tqdm

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

    def __floordiv__(self, other_money) -> int:
        return min(
            (self.ore // other_money.ore) if other_money.ore != 0 else BIG,
            (self.clay // other_money.clay) if other_money.clay != 0 else BIG,
            (self.obsidian // other_money.obsidian)
            if other_money.obsidian != 0
            else BIG,
        )


def compute_max_nb_geodes(
    recipe: str, start_nb_ore_robots: int = 1, time: int = 24, verbose: bool = False
) -> int:
    if int(recipe_nb_extractor.search(recipe).group(1)) in [7,15,18,20,22,28,30]: # to speed things up, as I noticed these recipes always yield 0 geodes
        return 0
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
        if verbose:
            print(f"== Minute {total_time_allowed - time +1} ==")
        # manage possible transactions: consume resources but do not add robots just yet as it takes one minute to build them
        (
            nb_geode_robot_bought,
            nb_obsidian_robot_bought,
            nb_clay_robot_bought,
            nb_ore_robot_bought,
        ) = (0, 0, 0, 0)
        if current_money >= geode_robot_price:
            nb_geode_robot_bought = 1#current_money // geode_robot_price # if I can buy geode robots it's always the best choice
            current_money = Money(
                (
                    current_money.ore
                    - geode_robot_price.ore * nb_geode_robot_bought,
                    current_money.clay
                    - geode_robot_price.clay * nb_geode_robot_bought,
                    current_money.obsidian
                    - geode_robot_price.obsidian * nb_geode_robot_bought,
                )
            )
            if verbose:
                print(
                    f"bought {nb_geode_robot_bought} geode robot(s), {current_money=} after the transaction"
                )
        if current_money >= obsidian_robot_price and (nb_geode_robot_bought == 0):
            nb_obsidian_robot_bought = randint(0, 1)#current_money // obsidian_robot_price)
            if nb_obsidian_robot_bought:  # random choice
                current_money = Money(
                    (
                        current_money.ore
                        - obsidian_robot_price.ore * nb_obsidian_robot_bought,
                        current_money.clay
                        - obsidian_robot_price.clay * nb_obsidian_robot_bought,
                        current_money.obsidian
                        - obsidian_robot_price.obsidian * nb_obsidian_robot_bought,
                    )
                )
                if verbose:
                    print(
                        f"bought {nb_obsidian_robot_bought} obsidian robot(s), {current_money=} after the transaction"
                    )
        if (
            current_money >= clay_robot_price
            and (nb_geode_robot_bought + nb_obsidian_robot_bought == 0)
        ):
            nb_clay_robot_bought = randint(0, 1)#current_money // clay_robot_price)
            if nb_clay_robot_bought:  # random choice
                current_money = Money(
                    (
                        current_money.ore - clay_robot_price.ore * nb_clay_robot_bought,
                        current_money.clay
                        - clay_robot_price.clay * nb_clay_robot_bought,
                        current_money.obsidian
                        - clay_robot_price.obsidian * nb_clay_robot_bought,
                    )
                )
                if verbose:
                    print(
                        f"bought {nb_clay_robot_bought} clay robot(s), {current_money=} after the transaction"
                    )
        if (
            current_money >= ore_robot_price
            and (
                nb_geode_robot_bought + nb_obsidian_robot_bought + nb_clay_robot_bought == 0)
        ):
            nb_ore_robot_bought = randint(0, 1)#current_money // ore_robot_price)
            if nb_ore_robot_bought:  # random choice
                current_money = Money(
                    (
                        current_money.ore - ore_robot_price.ore * nb_ore_robot_bought,
                        current_money.clay - ore_robot_price.clay * nb_ore_robot_bought,
                        current_money.obsidian
                        - ore_robot_price.obsidian * nb_ore_robot_bought,
                    )
                )
                if verbose:
                    print(
                        f"bought {nb_ore_robot_bought} ore robot(s), {current_money=} after the transaction"
                    )
        # manage robot activity
        current_money = Money(
            (
                current_money.ore + nb_ore_robot,
                current_money.clay + nb_clay_robot,
                current_money.obsidian + nb_obsidian_robot,
            ))
        nb_geodes += nb_geode_robot
        # update robot numbers in case transaction(s) occurred
        nb_ore_robot += nb_ore_robot_bought
        if verbose and nb_ore_robot_bought:
            print(
                f"The new ore-collecting robot is ready; you now have {nb_ore_robot} of them."
            )
        nb_clay_robot += nb_clay_robot_bought
        if verbose and nb_clay_robot_bought:
            print(
                f"The new clay-collecting robot is ready; you now have {nb_clay_robot} of them."
            )
        nb_obsidian_robot += nb_obsidian_robot_bought
        if verbose and nb_obsidian_robot_bought:
            print(
                f"The new obsidian-collecting robot is ready; you now have {nb_obsidian_robot} of them"
            )
        nb_geode_robot += nb_geode_robot_bought
        if verbose and nb_geode_robot_bought:
            print(
                f"The new geode-cracking robot is ready; you now have {nb_geode_robot} of them"
            )
        # update timer
        time -= 1
        if verbose:
            print("\n")
    return nb_geodes


def monte_carlo(recipe: str, n_sim: int = 100_000, verbose: bool = False, time:int=24) -> int:
    """Performs a Monte Carlo simulation using `n_sim` simulations and returning the best try (i.e. the max nb of geodes across runs)

    Args:
        recipe (str): the recipe
        n_sim (int, optional): _description_. Defaults to 10_000.
        verbose (bool, optional): _description_. Defaults to False.

    Returns:
        int: the result from the best try/tries
    """
    current_best = 0
    for _ in range(n_sim):
        if (score := compute_max_nb_geodes(recipe, time=time)) > current_best:
            current_best = score
            if verbose:
                print(f"{current_best=}")
    return current_best


def get_quality_level(recipe: str) -> int:
    return int(recipe_nb_extractor.search(recipe).group(1)) * monte_carlo(recipe)

recipes = [recipe for recipe in INPUT.splitlines() if recipe.strip()]
recipe_nb_extractor = re.compile(r"(\d+):")
price_extractor = re.compile(r"\d+.*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)")
BIG = 10**10
SOLVE_PART_1 = False
if __name__ == "__main__" and SOLVE_PART_1 is True:
    # going for a Monte Carlo simulation (though I'm aware it shines to get the average of the distribution, not the max)
    with Pool() as p:
        a = p.map(get_quality_level, recipes)
    print(a)
    print(sum(a)) #[1, 6, 9, 4, 50, 18, 0, 24, 27, 20, 33, 108, 13, 210, 0, 16, 85, 0, 19, 0, 42, 0, 207, 24, 50, 78, 54, 0, 29, 0] -> 1127
# part 2
SOLVE_PART_2 = True

def monte_carlo(recipe: str, n_sim: int = 250_000, verbose: bool = False, time:int=32) -> int:
    """Performs a Monte Carlo simulation using `n_sim` simulations and returning the best try (i.e. the max nb of geodes across runs)

    Args:
        recipe (str): the recipe
        n_sim (int, optional): _description_. Defaults to 10_000.
        verbose (bool, optional): _description_. Defaults to False.

    Returns:
        int: the result from the best try/tries
    """
    current_best = 0
    for _ in range(n_sim):
        if (score := compute_max_nb_geodes(recipe, time=time)) > current_best:
            current_best = score
            if verbose:
                print(f"{current_best=}")
    return current_best

if __name__ == "__main__" and SOLVE_PART_2 is True:
    recipes = [recipe for recipe in INPUT.splitlines() if recipe.strip()][:3] # now we only look at the first three blueprints
    mul = lambda x, y : x*y
    with Pool() as p:
        a = p.map(monte_carlo, recipes) # now we have 32 minutes
        print(a)
        print(reduce(mul, a))


