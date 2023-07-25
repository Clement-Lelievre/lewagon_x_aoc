"""https://adventofcode.com/2020/day/22"""

TEST_INPUT = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

INPUT = """Player 1:
5
20
28
30
48
7
41
24
29
8
37
32
16
17
34
27
46
43
14
49
35
11
6
38
1

Player 2:
22
18
50
31
12
13
33
39
45
21
19
26
44
10
42
3
4
15
36
2
40
47
9
23
25
"""

from collections import deque


class CrabGame:
    """The crabs' card game"""

    def __init__(self, cards: str) -> None:
        self.cards = cards

    def get_cards(self) -> None:
        """Parses the input into two card decks"""
        self.deck1 = deque([])
        self.deck2 = deque([])
        current_deck = self.deck1
        for row in self.cards.splitlines()[1:]:
            if "Player" in row:
                current_deck = self.deck2
            elif row.strip():
                current_deck.append(int(row.strip()))
        assert len(self.deck1) == len(
            self.deck2
        ), "Both decks should initially have the same length"
        print("Both card decks were initialized")

    def play_normal_game(self) -> None:
        self.get_cards()
        while self.deck1 and self.deck2:
            a, b = self.deck1.popleft(), self.deck2.popleft()
            if a > b:
                self.deck1.extend([a, b])
            else:
                self.deck2.extend([b, a])
        winner_deck = self.deck1 or self.deck2
        self.compute_winner_score(winner_deck)

    def compute_winner_score(self, winner_deck: list[int]) -> None:
        """Computes the winner's score as requested"""
        score = sum(
            val * (len(winner_deck) - ind) for ind, val in enumerate(winner_deck)
        )
        print(f"{score=}")

    def play_recursive_game(
        self, top_game: bool = False, verbose: bool = False
    ) -> tuple[int, list[int]]:
        if top_game:  # top-level game
            self.get_cards()
            self.known_results = {}
        seen = set()
        while self.deck1 and self.deck2:
            if (current_distrib := (tuple(self.deck1), tuple(self.deck2))) in seen:
                if verbose:
                    print("Cards already seen! Player 1 wins")
                return 0, self.deck1
            a, b = self.deck1.popleft(), self.deck2.popleft()
            seen.add(current_distrib)
            if (len(self.deck1) >= a) and (len(self.deck2) >= b):
                if current_distrib in self.known_results:
                    round_winner_ind = self.known_results[current_distrib]
                else:
                    frozen_deck1, frozen_deck2 = deque(self.deck1), deque(self.deck2)
                    if verbose:
                        print("playing sub-game...")
                    round_winner_ind, _ = self.play_recursive_game()
                    self.known_results[current_distrib] = round_winner_ind
                    self.deck1 = frozen_deck1  # reset initial deck, as it was modified by the above sub-game
                    self.deck2 = frozen_deck2  # reset initial deck, as it was modified by the above sub-game
                if (
                    round_winner_ind == 0
                ):  # player 1 won the sub-game, hence wins the current round
                    self.deck1.extend((a, b))
                else:
                    self.deck2.extend((b, a))
                continue
            if a > b:
                self.deck1.extend((a, b))
            else:
                self.deck2.extend((b, a))
        winner_deck = self.deck1 or self.deck2
        return (0 if winner_deck == self.deck1 else 1), winner_deck


if __name__ == "__main__":
    # part 1
    test_game = CrabGame(TEST_INPUT)
    test_game.play_normal_game()
    _, winner_deck = test_game.play_recursive_game(top_game=True)
    test_game.compute_winner_score(winner_deck)

    real_game = CrabGame(INPUT)
    real_game.play_normal_game()
    _, winner_deck = real_game.play_recursive_game(top_game=True)
    real_game.compute_winner_score(winner_deck)

    # part 2
