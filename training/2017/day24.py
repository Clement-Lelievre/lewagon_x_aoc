"""Initially I opted for subclassing the frozenset class and implementing a
custom dunder .__add__() method, but that proved overkill"""
import logging
from collections import deque

logging.basicConfig(level=logging.INFO)

INPUT = """<paste_input_here>"""

TEST_INPUT = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""


class BridgeBuilder:
    """Parses the input and builds the strongest bridge possible"""

    def __init__(self, port_list: str) -> None:
        self.ports = {
            tuple(map(int, row.split("/")))
            for row in port_list.splitlines()
            if row.strip()
        }
        # a set, which is fine as all ports are unique
        self.starting_ports = {tuple(sorted(port)) for port in self.ports if 0 in port}
        self.longest = 0
        self.strongest = 0

    def solve_part1(self) -> int:
        """Performs a breadth-first search to find the strongest bridge

        Returns:
            int: the strength of the strongest bridge
        """
        self.strongest = 0
        for start in self.starting_ports:
            queue = deque([[start]])
            while queue:
                current_path = queue.pop()
                current_vertex = current_path[-1]
                neighbours = {
                    port
                    for port in self.ports.difference(current_path)
                    if current_vertex[-1] in port and port[::-1] not in current_path
                }
                if (
                    not neighbours
                    and (scp := sum(sum(elem) for elem in current_path))
                    > self.strongest
                ):
                    # print(f"{current_path=} is new best with {scp}")
                    self.strongest = scp
                else:
                    queue.extend(
                        [
                            current_path
                            + [neigh if neigh[0] == current_vertex[-1] else neigh[::-1]]
                            for neigh in neighbours
                        ]
                    )
        logging.info(f"{self.strongest=}")
        return self.strongest

    def solve_part2(self) -> int:
        """Performs a breadth-first search to find the strength of the longest bridge

        Returns:
            int: the strength of the longest bridge (if several, the highest strength)
        """
        self.longest = 0
        self.strongest = 0
        for start in self.starting_ports:
            queue = deque([[start]])
            while queue:
                current_path = queue.pop()
                current_vertex = current_path[-1]
                neighbours = {
                    port
                    for port in self.ports.difference(current_path)
                    if current_vertex[-1] in port and port[::-1] not in current_path
                }
                if not neighbours:
                    if len(current_path) > self.longest:
                        self.longest = len(current_path)
                        self.strongest = sum(sum(elem) for elem in current_path)
                    elif len(current_path) == self.longest:
                        self.strongest = max(
                            self.strongest, sum(sum(elem) for elem in current_path)
                        )
                else:
                    queue.extend(
                        [
                            current_path
                            + [neigh if neigh[0] == current_vertex[-1] else neigh[::-1]]
                            for neigh in neighbours
                        ]
                    )
        logging.info(f"{self.strongest=}")
        return self.strongest


components_test = BridgeBuilder(TEST_INPUT)
components_actual = BridgeBuilder(INPUT)

# test
assert components_test.solve_part1() == 31

# actual input
components_actual.solve_part1()

# part 2
# test
assert components_test.solve_part2() == 19

# actual input
components_actual.solve_part2()
