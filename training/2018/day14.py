"My solution for AoC 2018 day 14, using namedtuples for the functional tests"
from collections import namedtuple

INPUT = 440_231
TestP1 = namedtuple("TestP1", "nb_recipes scores")
tests_p1 = (
    TestP1(9, "5158916779"),
    TestP1(5, "0124515891"),
    TestP1(18, "9251071085"),
    TestP1(2018, "5941429882"),
)
TestP2 = namedtuple("TestP2", "scores nb_recipes")
tests_p2 = (
    TestP2("51589", 9),
    TestP2("01245", 5),
    TestP2("92510", 18),
    TestP2("59414", 2018),
)


def solve_part1(nb_recipes: int, ind1: int = 0, ind2: int = 1) -> str:
    """Makes recipes till 10 + `nb_recipes` is reached

    Args:
        nb_recipes (int): _description_
        ind1 (int, optional): _description_. Defaults to 0.
        ind2 (int, optional): _description_. Defaults to 1.

    Returns:
        str: the sequence searched
    """
    scores = [3, 7]  # avoiding the pitfall of mutable default arguments
    while len(scores) < nb_recipes + 10:
        scores.extend(int(elem) for elem in str(scores[ind1] + scores[ind2]))
        ind1 = (ind1 + scores[ind1] + 1) % len(scores)
        ind2 = (ind2 + scores[ind2] + 1) % len(scores)
    return "".join(map(str, scores[nb_recipes : nb_recipes + 10]))


def solve_part2(seq: str, ind1: int = 0, ind2: int = 1) -> int:
    """Now, we need to find how many recipes are made before the sequence appears in the scores

    Args:
        seq (str): the sequence looked for
        ind1 (int, optional): _description_. Defaults to 0.
        ind2 (int, optional): _description_. Defaults to 1.

    Returns:
        int: the number of recipes before the sequence appears
    """
    scores = "37"  # avoiding the pitfall of mutable default arguments
    nb_new = 0
    len_seq = len(seq)
    len_scores = len(scores)
    while True:
        s1, s2 = int(scores[ind1]), int(scores[ind2])
        to_append = str(s1 + s2)
        nb_new = len(to_append)
        scores += to_append
        len_scores += nb_new
        for i in range(nb_new):
            if scores[-len_seq - i : len_scores - i] == seq:
                return len_scores - len_seq - i
        ind1 = (ind1 + s1 + 1) % len_scores
        ind2 = (ind2 + s2 + 1) % len_scores


if __name__ == "__main__":
    # testing
    for test in tests_p1:
        print(f"testing {test.nb_recipes} -> {test.scores}")
        assert solve_part1(test.nb_recipes) == test.scores

    print(f"part1: {solve_part1(INPUT)}")

    # testing
    for testp2 in tests_p2:
        print(f"testing {testp2.scores} -> {testp2.nb_recipes}")
        assert solve_part2(testp2.scores) == testp2.nb_recipes

    print(f"part2: {solve_part2(str(INPUT))}")
