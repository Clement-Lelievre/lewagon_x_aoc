"Let's try to build a directed, unweighted graph and then walk through it"
import logging
from collections import deque

logging.basicConfig(level=logging.INFO)

TEST_INPUT_P1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

TEST_INPUT_P2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

INPUT = """<paste_input_here>"""


class Graph:
    "The orbital map and its utilities"

    def __init__(self, input_: str) -> None:
        self.input_ = input_
        self.neighbors: dict[str, str] = {}
        self.parse_input()
        self.graph: dict[str, set[str]] = {}

    def parse_input(self) -> None:
        """Parses the input and stores the orbiting relationships in a dict"""
        for line in self.input_.splitlines():
            orbited, orbiting = line.split(")")
            self.neighbors[orbiting] = orbited

    def solve_part1(self) -> int:
        "Walk through every possible path and increment the orbit counter"
        nb_orbits = 0
        for vertex in self.neighbors:
            current_vertex = vertex
            while current_vertex != "COM":
                current_vertex = self.neighbors[current_vertex]
                nb_orbits += 1
        logging.info("Part 1: %d", nb_orbits)
        return nb_orbits

    def build_undirected_graph(self) -> None:
        """For part 2 the graph becomes undirected, so I extend the neihbours dict from part one"""
        for orbiting, orbited in self.neighbors.items():
            self.graph[orbiting] = {orbited} | {
                k for k, v in self.neighbors.items() if v == orbiting
            }

    def solve_part2(self) -> int:
        """Performs a BFS to compute the path length between the object
        orbited by YOU and the one orbited by SAN"""
        assert "YOU" in self.neighbors and "SAN" in self.neighbors, "Missing vertices"
        self.build_undirected_graph()
        queue = deque([(0, self.neighbors["YOU"])])
        visited = set()
        shortest_path_length = float("inf")
        while queue:
            dist, current_vertex = queue.pop()
            if (
                current_vertex in visited
                or current_vertex == "COM"
                or dist >= shortest_path_length
            ):
                continue
            visited.add(current_vertex)
            if current_vertex == self.neighbors["SAN"]:
                shortest_path_length = dist
                logging.info("Part 2: %d", shortest_path_length)
                break
            for neigh in self.graph[current_vertex]:
                queue.append((dist + 1, neigh))
        else:
            raise Exception("Unsolvable")
        return shortest_path_length


if __name__ == "__main__":
    test_graph_p1 = Graph(TEST_INPUT_P1)
    assert test_graph_p1.solve_part1() == 42

    actual_graph = Graph(INPUT)
    actual_graph.solve_part1()

    #  part 2
    test_graph_p2 = Graph(TEST_INPUT_P2)
    assert test_graph_p2.solve_part2() == 4

    actual_graph.solve_part2()
