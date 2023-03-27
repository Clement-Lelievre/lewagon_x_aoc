"""Challenge 24 of AoC 2022 was so interesting that I decided to answer a few
more questions, such as visualizing the path(s) taken. I will code the plotting
here to benefit from the IDE's features but then will copy the code into the 
notebook `puzzles_requiring_graphs.ipynb` in the root dir, in order to view the 
graph in a nicer interface"""
import logging
from queue import PriorityQueue

import matplotlib.pyplot as plt

from day24 import INPUT, PartTwoBlizzardProblem

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class BlizzardFullPath(PartTwoBlizzardProblem):
    "Extends the parent class in order to retain the path taken and to plot it"

    def traverse_pqueue(
        self,
        start: tuple[int],
        dest: tuple[int],
        blizzard_ind: int = 0,
    ) -> tuple[int]:
        """Finds the shortest path with A*

        Args:
            start (tuple[int]): starting location
            dest (tuple[int]): final destination
            blizzard_ind (int, optional): the state of the blizzard map, that has been precomputed during __init__(). Defaults to 0.

        Raises:
            Exception: if the destination is unreachable

        Returns:
            tuple[int]: minimum_ number of minutes to reach the destination, and the blizzard state index at the end of the path
        """
        queue: PriorityQueue[int, tuple[int], int, int] = PriorityQueue()
        INFINITY = float("inf")
        queue.put(
            (0, start, 0, blizzard_ind)
        )  # distance to target (heuristic), current location, current nb of minutes, current blizzard state index
        seen = (
            {}
        )  # will be used to 1) avoid repeating paths 2) reconstruct the shortest path and plot it
        comes_from = self.start_square
        while not queue.empty():
            _, curr_pos, nb_minutes, blizzard_ind = queue.get()
            if seen.get((curr_pos, blizzard_ind), (INFINITY, None))[0] <= nb_minutes:
                continue  # prune the tree
            seen[(curr_pos, blizzard_ind)] = (nb_minutes, comes_from)
            if curr_pos == dest:
                logging.info(f"{nb_minutes=} taken to reach {dest}")
                break
            # append legal neighbour states to the queue
            comes_from = curr_pos
            x, y = curr_pos
            new_blizzard_ind = (blizzard_ind + 1) % self.nb_blizzard_states
            for neigh in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x, y)):
                if self.blizzard_states[new_blizzard_ind].get(neigh) == []:
                    queue.put(
                        (
                            self.dist_to_target[neigh] + nb_minutes,
                            neigh,
                            nb_minutes + 1,
                            new_blizzard_ind,
                        )
                    )
        else:
            raise Exception("Unreachable")
        self.seen = {
            key[0]: val for key, val in seen.items()
        }  # get rid of the blizzard state index
        return nb_minutes, blizzard_ind

    def _reconstruct_shortest_path(self):
        if not hasattr(self, "seen"):
            logging.info(
                "No path has been found yet, please run `traverse_pqueue()` first"
            )
        else:
            path = []
            latest = self.end_square
            while latest != self.start_square:
                path.append(latest)
                latest = self.seen[latest][1]
        self.shortest_path = path[::-1]

    def plot_shortest_path(self) -> None:
        if not hasattr(self, "seen"):
            print("No path has been found yet, please run `traverse_pqueue()` first")
            return
        if not hasattr(self, "shortest_path"):
            self._reconstruct_shortest_path()
        plt.plot(*zip(*self.shortest_path), marker="o")
        plt.show()


if __name__ == "__main__":
    actual_p2 = BlizzardFullPath(INPUT)
    _ = actual_p2.traverse_pqueue(actual_p2.start_square, actual_p2.end_square, 0)
    actual_p2.plot_shortest_path()
