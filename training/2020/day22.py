"""https://adventofcode.com/2020/day/22"""

from collections import deque


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

# I choose a deck not because it's about decks of cards, but for fast access to both ends of an array


class CrabGame:
    """The crabs' card game"""

    def __init__(self, cards: str) -> None:
        self.cards = cards
        self.make_decks()

    def make_decks(self) -> None:
        """Parses the input into two card decks"""
        self.deck1: deque[int] = deque([])
        self.deck2: deque[int] = deque([])
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

    def play_normal_game(
        self,
    ) -> None:
        """Playing the base version of the game"""
        while self.deck1 and self.deck2:
            a, b = self.deck1.popleft(), self.deck2.popleft()
            self.deck1.extend([a, b]) if a > b else self.deck2.extend([b, a])
        winner_deck = self.deck1 or self.deck2
        self.compute_winner_score(winner_deck)

    def compute_winner_score(self, winner_deck: deque[int]) -> None:
        """Computes the score as requested

        Args:
            winner_deck (deque[int]): the final deck of the winner of the game
        """
        score = sum(
            val * (len(winner_deck) - ind) for ind, val in enumerate(winner_deck)
        )
        print(f"{score=}")

    def play_recursive_game(
        self,
        deck1: deque[int],
        deck2: deque[int],
    ) -> tuple[int, deque[int]]:
        """Playing the recursive game

        Args:
            deck1 (deque[int]): _description_
            deck2 (deque[int]): _description_

        Returns:
            tuple[int, deque[int]]: _description_
        """
        seen = set()
        while deck1 and deck2:
            if (current_distrib := (tuple(deck1), tuple(deck2))) in seen:
                return 0, deck1  # player 1 wins
            a, b = deck1.popleft(), deck2.popleft()
            seen.add(current_distrib)
            if len(deck1) >= a and len(deck2) >= b:
                round_winner_ind, _ = self.play_recursive_game(
                    deque(list(deck1)[:a]), deque(list(deck2)[:b])
                )
                deck2.extend((b, a)) if round_winner_ind else deck1.extend((a, b))
            elif a > b:
                deck1.extend((a, b))
            else:
                deck2.extend((b, a))
        winner_deck = deck1 or deck2
        return (0 if winner_deck == deck1 else 1), winner_deck


if __name__ == "__main__":
    # part 1 on test data
    test_game = CrabGame(TEST_INPUT)
    test_game.play_normal_game()
    # part 2 on test data
    test_game.make_decks()
    _, winner_deck_ = test_game.play_recursive_game(
        test_game.deck1,
        test_game.deck2,
    )
    test_game.compute_winner_score(winner_deck_)
    # part 1 on actual data
    real_game = CrabGame(INPUT)
    real_game.play_normal_game()
    # part 2 on actual data
    real_game.make_decks()
    _, winner_deck_ = real_game.play_recursive_game(real_game.deck1, real_game.deck2)
    real_game.compute_winner_score(winner_deck_)
