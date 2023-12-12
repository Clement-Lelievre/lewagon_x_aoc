"""AoC 2023 day 4: https://adventofcode.com/2023/day/4
Usage: python day4.py day4_input.txt
"""

import argparse

TEST_DATA = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def main_p1(text: str) -> int:
    lines = [line for line in text.splitlines() if line]
    answer = 0
    for line in lines:
        card_data = line.split(":")[1].strip()
        winning, you_have = card_data.split("|")
        winning, you_have = [int(nb) for nb in winning.split()], [
            int(nb) for nb in you_have.split()
        ]
        winning_you_have = set(winning) & set(you_have)
        answer += 0 if not winning_you_have else 2 ** (len(winning_you_have) - 1)
    print(f"part 1 {answer=}")
    return answer


def main_p2(text: str) -> int:
    lines = [line for line in text.splitlines() if line]
    answer = 0
    cards = {
        k: 1 for k in range(1, len(lines) + 1)
    }  # key: card number, value: nb of them I have
    for card_nb, line in enumerate(lines, start=1):
        card_data = line.split(":")[1].strip()
        winning, you_have = card_data.split("|")
        winning, you_have = [int(nb) for nb in winning.split()], [
            int(nb) for nb in you_have.split()
        ]
        nb_cards_won = len(set(winning) & set(you_have))
        for i in range(card_nb + 1, card_nb + 1 + nb_cards_won):
            cards[i] += cards[card_nb]
    answer = sum(cards.values())
    print(f"part 2 {answer=}")
    return answer


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 13, "should be 13 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    assert main_p2(TEST_DATA) == 30, "should be 30 for the test input p2"
    main_p2(text)
