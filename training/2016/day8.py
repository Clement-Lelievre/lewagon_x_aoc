import re

INPUT = """rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x2
rotate row y=1 by 5
rotate row y=0 by 3
rect 1x2
rotate column x=30 by 1
rotate column x=25 by 1
rotate column x=10 by 1
rotate row y=1 by 5
rotate row y=0 by 2
rect 1x2
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 18
rotate row y=0 by 5
rotate column x=0 by 1
rect 3x1
rotate row y=2 by 12
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate column x=20 by 1
rotate row y=2 by 5
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 15
rotate row y=0 by 15
rotate column x=10 by 1
rotate column x=5 by 1
rotate column x=0 by 1
rect 14x1
rotate column x=37 by 1
rotate column x=23 by 1
rotate column x=7 by 2
rotate row y=3 by 20
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 5
rotate row y=2 by 2
rotate row y=1 by 4
rotate row y=0 by 4
rect 1x4
rotate column x=35 by 3
rotate column x=18 by 3
rotate column x=13 by 3
rotate row y=3 by 5
rotate row y=2 by 3
rotate row y=1 by 1
rotate row y=0 by 1
rect 1x5
rotate row y=4 by 20
rotate row y=3 by 10
rotate row y=2 by 13
rotate row y=0 by 10
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 10
rotate row y=3 by 10
rotate row y=1 by 10
rotate row y=0 by 10
rotate column x=7 by 2
rotate column x=5 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 20
rotate row y=3 by 12
rotate row y=1 by 15
rotate row y=0 by 10
rotate column x=8 by 2
rotate column x=7 by 1
rotate column x=6 by 2
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=46 by 2
rotate column x=43 by 2
rotate column x=24 by 2
rotate column x=14 by 3
rotate row y=5 by 15
rotate row y=4 by 10
rotate row y=3 by 3
rotate row y=2 by 37
rotate row y=1 by 10
rotate row y=0 by 5
rotate column x=0 by 3
rect 3x3
rotate row y=5 by 15
rotate row y=3 by 10
rotate row y=2 by 10
rotate row y=0 by 10
rotate column x=7 by 3
rotate column x=6 by 3
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=19 by 1
rotate column x=10 by 3
rotate column x=5 by 4
rotate row y=5 by 5
rotate row y=4 by 5
rotate row y=3 by 40
rotate row y=2 by 35
rotate row y=1 by 15
rotate row y=0 by 30
rotate column x=48 by 4
rotate column x=47 by 3
rotate column x=46 by 3
rotate column x=45 by 1
rotate column x=43 by 1
rotate column x=42 by 5
rotate column x=41 by 5
rotate column x=40 by 1
rotate column x=33 by 2
rotate column x=32 by 3
rotate column x=31 by 2
rotate column x=28 by 1
rotate column x=27 by 5
rotate column x=26 by 5
rotate column x=25 by 1
rotate column x=23 by 5
rotate column x=22 by 5
rotate column x=21 by 5
rotate column x=18 by 5
rotate column x=17 by 5
rotate column x=16 by 5
rotate column x=13 by 5
rotate column x=12 by 5
rotate column x=11 by 5
rotate column x=3 by 1
rotate column x=2 by 5
rotate column x=1 by 5
rotate column x=0 by 1"""

# observation: the two 'rotate' operations do not affect the number of lit pixels.
# So I only have to consider the 'rect' operations

NUMBER_PAT = re.compile(r"\d+")


class Screen:
    def __init__(self, width: int = 50, height: int = 6) -> None:
        self.width = width
        self.height = height
        self.make_screen()

    def make_screen(self) -> None:
        assert self.width > 0 and self.height > 0
        row = [0] * self.width  # 0 denotes an off pixel, 1 an on pixel
        self.screen = [
            row.copy() for _ in range(self.height)
        ]  # if you don't use a copy, then it's wrong as all pixels will be wrongly copied to any row

    def pretty_print(self, screen=None) -> None:
        """Helper function to get a clear view of the screen"""
        for row in self.screen if screen is None else screen:
            print(*row)

    def rotate(self, by: int, row_nb=None, col_nb=None) -> None:
        """Performs an inplace rotation on the screen, as described in the instructions

        Args:
            screen (list[list[int]]): screen
            by (int): the amount to shift by
            row_nb (_type_, optional): _description_. Defaults to None.
            col_nb (_type_, optional): _description_. Defaults to None.
        """
        assert (row_nb is None) ^ (
            col_nb is None
        )  # XOR, as only 1 of the 2 should be None
        if row_nb is not None:
            self.screen[row_nb] = [
                self.screen[row_nb][(i - by) % self.width] for i in range(self.width)
            ]
        else:
            new_col = [self.screen[row][col_nb] for row in range(self.height)]
            new_col_shifted = [
                new_col[(i - by) % self.height] for i in range(self.height)
            ]
            for row in range(self.height):
                self.screen[row][col_nb] = new_col_shifted[row]

    def get_input(self, input: str) -> None:
        """Yields the non empty rows of the input string"""
        self.input = filter(None, input.splitlines())

    def process_input(self) -> None:
        for _, cmd in enumerate(self.input):
            print(cmd)
            data = map(int, NUMBER_PAT.findall(cmd))
            if cmd.startswith("rect"):
                width, height = data
                for h in range(height):
                    for w in range(width):
                        self.screen[h][w] = 1
            else:
                nb, by = data
                if "row" in cmd:
                    self.rotate(by=by, row_nb=nb)  # use functools.partial() ?
                else:
                    self.rotate(by=by, col_nb=nb)

            # print(cmd)
            self.pretty_print()
        self.print_nb_on_pixels()

    def print_message(self):
        msg = [["O" if item else " " for item in row] for row in self.screen]
        self.pretty_print(msg)

    def print_nb_on_pixels(self) -> None:
        """Prints out the number of pixels that are lit on the screen"""
        print(sum(sum(row) for row in self.screen))


# main code, this solves both parts of the challenge
my_screen = Screen()
my_screen.get_input(INPUT)
my_screen.process_input()
my_screen.print_message()
