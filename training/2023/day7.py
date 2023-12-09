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
CARDS_VALUES_P1 = {
    v: k for k, v in dict(enumerate(CARDS[::-1].split(","), start=1)).items()
}
CARDS_VALUES_P2 = CARDS_VALUES_P1 | {"J": min(CARDS_VALUES_P1.values()) - 1}
TEST_DATA = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def hand_value_p1(hand: str) -> tuple[int, tuple[int]]:
    c = Counter(hand)
    card_values = tuple([CARDS_VALUES_P1[card_value] for card_value in hand])
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
    sorted_hands = sorted(hands, key=hand_value_p1)  # use native tuple sorting
    answer = sum(
        bid_data[hand] * rank for rank, hand in enumerate(sorted_hands, start=1)
    )
    print(f"part 1 : {answer=}")
    return answer


def hand_value_p2(hand: str) -> tuple[int, tuple[int]]:
    c = Counter(hand)
    card_values = tuple([CARDS_VALUES_P2[card_value] for card_value in hand])
    sorted_values = sorted(c.values(), reverse=True)
    if "J" not in hand or hand == "J" * 5:
        match sorted_values:
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
                return (1, card_values)
    nb_js = c["J"]
    match sorted_values:
        case [4, 1] | [3, 2]:
            return (7, card_values)
        case [3, 1, 1]:
            return (6, card_values)
        case [2, 2, 1]:
            return (6, card_values) if nb_js == 2 else (5, card_values)
        case [2, 1, 1, 1]:
            return (4, card_values)
        case _:
            return (2, card_values)


def main_p2(cards_data: str) -> int:
    lines = [line for line in cards_data.splitlines() if line.strip()]
    bid_data = dict(
        zip(
            [line.split()[0] for line in lines],
            map(int, [line.split()[1] for line in lines]),
        )
    )  # {hand:bid_amount}
    hands = bid_data.keys()
    sorted_hands = sorted(hands, key=hand_value_p2)  # use native tuple sorting
    answer = sum(
        bid_data[hand] * rank for rank, hand in enumerate(sorted_hands, start=1)
    )
    print(f"part 2 : {answer=}")
    return answer


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 6440, "should be 6440 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    assert main_p2(TEST_DATA) == 5905, "should be 5905 for the test input p2"
    main_p2(text)
