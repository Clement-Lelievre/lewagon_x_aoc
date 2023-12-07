"""AoC 2023 day 7: https://adventofcode.com/2023/day/7
"""
import argparse
from collections import Counter


# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456


CARDS = "A,K,Q,J,T,9,8,7,6,5,4,3,2"
CARDS_VALUES = {
    v: k for k, v in dict(enumerate(CARDS[::-1].split(","), start=1)).items()
}

TEST_DATA = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def hand_value(hand: str) -> tuple[int, tuple[int]]:
    c = Counter(hand)
    card_values = tuple([CARDS_VALUES[card_value] for card_value in hand])
    match sorted(c.values(), reverse=True):
        case [5]:
            return (7, card_values)
        case [4, 1]:
            return (6, card_values)
        case [3, 2]:
            return (5, card_values)
        case [3, 1, 1]:
            return (4, card_values)
        case [2, 2, 1]:
            return (3, card_values)
        case [2, 1, 1, 1]:
            return (2, card_values)
        case _:
            print(1111)
            return (1, card_values)


def main_p1(cards_data: str) -> int:
    lines = [line for line in cards_data.splitlines() if line.strip()]
    bid_data = dict(
        zip(
            [line.split()[0] for line in lines],
            map(int, [line.split()[1] for line in lines]),
        )
    )  # {hand:bid_amount}
    hands = bid_data.keys()
    sorted_hands = sorted(hands, key=hand_value)  # use native tuple sorting
    answer = sum(
        bid_data[hand] * rank for rank, hand in enumerate(sorted_hands, start=1)
    )
    print(f"part 1 : {answer=}")
    return answer


def main_p2() -> int:
    ...


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 6440, "should be 6440 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    # assert main_p2(TEST_DATA) == 46, "should be 46 for the test input p2"
    # main_p2(text)
