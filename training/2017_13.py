"""Without any imports, solve AoC 2017 day 13. A bit of OOP,
dict comprehensions, but by far the most instructive feature is how
the kwargs of the lambda functions are necessary for the code to work.
Full text here: https://adventofcode.com/2017/day/13"""
INPUT = """0: 5
1: 2
2: 3
4: 4
6: 8
8: 4
10: 6
12: 6
14: 8
16: 6
18: 6
20: 12
22: 14
24: 8
26: 8
28: 9
30: 8
32: 8
34: 12
36: 10
38: 12
40: 12
44: 14
46: 12
48: 10
50: 12
52: 12
54: 12
56: 14
58: 12
60: 14
62: 14
64: 14
66: 14
68: 17
70: 12
72: 14
76: 14
78: 14
80: 14
82: 18
84: 14
88: 20
"""


class Scanners(dict):
    """A dict that supports the motion of the scanners, top to bottom then bottom to top,
    using the `update_pos` method"""

    def __init__(self, my_dict: dict) -> None:
        super().__init__()
        self.states = my_dict

    def update_pos(self) -> None:
        """Updates the positions of each scanner as per the motion described in the text"""
        for k in self.states:
            current_ind, length, direction = self.states[k]
            if (current_ind, direction) not in ((0, 1), (length - 1, 0)):
                self.states[k] = (
                    current_ind + (-1 if direction else 1),
                    firewall[k],
                    direction,
                )
            else:  # need to go backwards
                self.states[k] = (
                    1 if direction else length - 2,
                    firewall[k],
                    1 - direction,
                )

    def get(self, k):
        """Convenience method that overrides `dict.get` to make the result subscriptable without
        seeing a harcoded dummy subscriptable value
        """
        dummy = (1,)
        return self.states.get(k, dummy)


firewall = {
    int(row[: (colon_ind := row.index(":"))]): int(row[colon_ind + 2 :])
    for row in INPUT.splitlines()
    if row.strip()
}
scanners = Scanners(
    {k: (0, firewall[k], 0) for k in firewall}
)  # value stores: index, length, direction (0:down, 1: up)


severity = 0
for packet_pos in range(max(firewall) + 1):  # update packet position
    # check if caught
    if packet_pos in firewall and scanners.get(packet_pos)[0] == 0:
        severity += packet_pos * firewall[packet_pos]
    # update scanner positions
    scanners.update_pos()

print(f"part 1: {severity=}")

# part 2
# the naïve solution works on the example but does not scale to my actual input,
# so I'll need to come up with a smarter solution

# My plan: identify the sets of values that get the packet undetected at each layer
# (accounting for the time required to get there). Then intersecting the sets of valid values
# would be too inefficient, instead we'll store the conditionals (with lambda functions)
# and iterate on them


def get_len(layer_depth: int) -> int:
    """Returns the nb of steps made by the scanner before coming back to the top of its layer

    Args:
        layer_depth (int): the layer depth as provided

    Raises:
        ValueError: if layer length is less than 2

    Returns:
        int: the nb of steps needed for the scanner to come back
    """
    if layer_depth < 2:
        raise ValueError
    return 2 + 2 * (layer_depth - 2)


candidates = []
actual_lens = {
    depth: get_len(depth) for depth in set(firewall.values())
}  # a bit of caching
for layer_nb, depth in firewall.items():
    actual_len = actual_lens[depth]
    candidates.append(
        lambda x, layer_nb=layer_nb, actual_len=actual_len: (x + layer_nb) % actual_len
    )

delay = 0
while not all(func(delay) for func in candidates):
    delay += 1
print(f"part 2: {delay=}")
