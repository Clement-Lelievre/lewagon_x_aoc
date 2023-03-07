"""Today we have a bunch of bots that exchange chips according 
to predefined rules.
Themes: logging, REGEX, defaultdict, functools, OOP
Code formatted with Black, imports sorted with isort, type hints checked 
with mypy and the rest with pylint"""
import logging
import re
from collections import defaultdict
from functools import partial, reduce

logging.basicConfig(level=logging.INFO)

INPUT = """paste_input_here"""

TEST_INPUT = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""


class BotsShow:
    """Simulates the bots' chip-exchanging process.
    On second thought, it might have been better to define a Bot class,
    with give and receive methods"""

    VALUE_GOES_TO_PAT = re.compile(r"value (\d+) goes to bot (\d+)")
    BOT_GIVES_TO_PAT = re.compile(
        r"bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)"
    )

    def __init__(self, input_: str) -> None:
        self.input_ = input_.splitlines()
        self.bots_chips: dict[int, set[int]] = defaultdict(set)
        self.output_bins: dict[int, list[int]] = defaultdict(list)
        self.giving_rules: dict = {}
        self.give_to_bots()
        self.get_giving_rules()

    def give_to_bots(self) -> None:
        """Provides to each bot the values as stated in the instructions that
        match 'value x goes to bot y'"""
        for line in self.input_:
            if data := self.VALUE_GOES_TO_PAT.findall(line):
                val, bot_nb = map(int, data[0])
                self.bots_chips[bot_nb].add(val)
        if max(map(len, self.bots_chips.values())) > 2:
            raise Exception("A bot has more than 2 chips")
        logging.info("Successfully gave chips to bots")

    def get_giving_rules(self) -> None:
        """Stores in a dict the rules that tell each bot how to give its low/
        high value, when it's holding exactly two chips"""
        for line in self.input_:
            if data := self.BOT_GIVES_TO_PAT.findall(line):
                (
                    giving_bot_nb,
                    low_receiver_type,
                    low_receiver_nb,
                    high_receiver_type,
                    high_receiver_nb,
                ) = data[0]
                self.giving_rules[int(giving_bot_nb)] = (
                    partial(
                        self.bot_give_to,
                        bot_nb=int(giving_bot_nb),
                        receiver_type=low_receiver_type,
                        receiver_nb=int(low_receiver_nb),
                    ),
                    partial(
                        self.bot_give_to,
                        bot_nb=int(giving_bot_nb),
                        receiver_type=high_receiver_type,
                        receiver_nb=int(high_receiver_nb),
                    ),
                )
        if max(map(len, self.giving_rules.values())) > 2:
            raise Exception("A bot has more than 2 instructions to give")
        logging.info("Successfully processed the giving rules")

    def bot_give_to(
        self, bot_nb: int, receiver_type: str, receiver_nb: int, value: int
    ) -> None:
        """Performs the action of transferring a chip numbered `value` from
        bot number `bot_nb` to receiver type `receiver_type`
        number `receiver_nb`

        Args:
            bot_nb (int): number of the bot that gives a chip
            receiver_type (str): either 'output' or 'bot'
            receiver_nb (int): receiver number
            value (int): number of the chip being transferred
        """
        if receiver_type.startswith("o"):  # output bin
            self.output_bins[receiver_nb].append(value)
        else:  # give to bot
            self.bots_chips[receiver_nb].add(value)
        self.bots_chips[bot_nb].remove(value)

    def solve_part_one(self, nb1: int, nb2: int) -> int:
        """Simulates the chip-exchanging process till a bot owns nb1 and nb2
        numbered chips

        Args:
            nb1 (int): the number of the first chip
            nb2 (int): the number of the second chip

        Raises:
            Exception: if a bot has more than 2 chips

        Returns:
            int: the number of the bot that first owns both chips numbered `nb1` and `nb2`
        """
        while {
            nb1,
            nb2,
        } not in self.bots_chips.values():
            for bot_nb in [
                bot_nb
                for bot_nb in self.giving_rules
                if len(self.bots_chips[bot_nb]) == 2
            ]:
                low, high = sorted(self.bots_chips[bot_nb])
                self.giving_rules[bot_nb][0](value=low)
                self.giving_rules[bot_nb][1](value=high)
            if max(map(len, self.bots_chips.values())) > 2:
                raise Exception("A bot has more than 2 chips")
        assert self.bots_chips, "Error: No bot owns chips"
        for k in self.bots_chips:
            if self.bots_chips[k] == {nb1, nb2}:
                logging.info(f"Part 1: Bot number {k}")
                break
        return k

    def solve_part_two(self) -> int:
        """Simulates the full chip-exchanging process till no action
        is possible

        Raises:
            Exception: if a bot has more than 2 chips

        Returns:
            int: the number you get if you multiply chips in output
            bins numbered 0, 1, 2
        """
        can_play = True
        while can_play:
            can_play = False
            for bot_nb, give_to in self.giving_rules.items():
                if len(self.bots_chips[bot_nb]) == 2:
                    can_play = True
                    low, high = sorted(self.bots_chips[bot_nb])
                    give_to[0](value=low)
                    give_to[1](value=high)
            if max(map(len, self.bots_chips.values())) > 2:
                raise Exception("A bot has more than 2 chips")
        assert all(
            (i in self.output_bins for i in range(3))
        ), "At least one output bin is missing a chip"
        logging.info(
            f"Part 2: {(answer := reduce(lambda x,y:x*y, (self.output_bins[i][0] for i in range(3))))}"
        )
        return answer


if __name__ == "__main__":
    # test part 1
    bs_test = BotsShow(TEST_INPUT)
    assert bs_test.solve_part_one(5, 2) == 2
    # solving for my actual input
    bs = BotsShow(INPUT)
    bs.solve_part_one(61, 17)

    # test part 2
    assert bs_test.solve_part_two() == 5 * 2 * 3
    # solving for my actual input
    bs.solve_part_two()
