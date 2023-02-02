import heapq
from functools import cache


DEPTH = 5616
TARGET = (10, 785)
ENTRANCE = (0, 0)

erosion_levels = {}


def get_geologic_index(x: int, y: int) -> int:
    if (x, y) in {ENTRANCE, TARGET}:
        return 0
    if y == 0:
        return x * 16_807
    if x == 0:
        return y * 48_271
    return (
        erosion_levels[(x - 1, y)] * erosion_levels[(x, y - 1)]
    )  # requires having visited the region above and that to the left beforehand


def get_erosion_level(geologic_index: int, depth: int = DEPTH) -> int:
    return (geologic_index + depth) % 20_183


def get_region_type(erosion_level: int) -> int:
    return erosion_level % 3


def get_all_region_types(end_location: tuple[int, int]):
    region_types = {}
    TARGET_X, TARGET_Y = end_location
    queue = sorted(
        ((i, j) for i in range(TARGET_X + 1) for j in range(TARGET_Y + 1)),
        key=sum,
    )  # sorting with key = sum ensures we visit locations that we can for sure get the geo index
    for current_region in queue:
        geo_index = get_geologic_index(*current_region)
        ero_level = get_erosion_level(geo_index)
        erosion_levels[current_region] = ero_level
        region_types[current_region] = get_region_type(ero_level)
    return region_types


print("part 1:", sum(get_all_region_types(TARGET).values()))

# part 2
# this looks a like a shortest path search in an undirected, weighted graph that has additional constraints
# here is how I see things unfolding: part 1 was here to ensure we know how to determine the region type of any square
# I'll reuse the part 1 code and now I need to perform A*, tracking the states (manhattan_dist, location, time to get there, equipment type)
# the degrees of liberty are on the location (which square do I visit next?) and equipment (what do I carry to visit it?), with constraints though

# Note on the data structure used: after first trying out a BFS, it worked on the example test provided,
# but did not scale to my actual input. So, to make the search more efficient, I then used a priority queue
# (heapq in Python: see docs here: https://docs.python.org/3/library/heapq.html)
# using as heuristic the Manhattan distance to the target because intuitively we need to "roughly go "towards" the target"
# I put the manahattan distance as the first element of my state tuples, so that when I heappop(), I get the closest point to the target

# then this still wasn't efficient enough, so I changed my heuristic to a mix of the estimated
# time spent switching gears and the manhattan distance


@cache
def heuristic(
    pt1: tuple[int, int], time_spent: int, pt2: tuple[int, int] = TARGET
) -> int:
    """The heuristic function for my priority queue. It uses the Manhattan distance to the target location combined
    with a penalty related to the estimated number of gear switches ahead

    Args:
        pt1 (tuple[int, int]): X, Y location (x: rows, y: columns)
        time_spent (int): path cost so far
        pt2 (tuple[int, int], optional): target X, Y location. Defaults to TARGET.

    Returns:
        int: the priority value of `pt1`
    """
    x1, y1 = pt1
    x2, y2 = pt2
    return (abs(x1 - x2) + abs(y1 - y2)) * (
        TRAVEL_TIME + SWITCH_GEAR_TIME * 2 / 3
    ) + time_spent


# step 1 : compute all region types as in part 1, with an (arbitrary) margin in case we
# exceed the target location row or column

MARGIN = 100
ALLOWED_EQUIPMENTS = {  # using a frozenset is not mandatory, but it makes the code more readable, as it conveys the intent of having an immutable and unsorted arrays (besides, membership test is O(1))
    0: frozenset((1, 2)),
    1: frozenset((0, 2)),
    2: frozenset((0, 1)),
}  # keys are region types (rocky 0, wet 1, narrow 2), values are allowed equipments
REGION_TYPES = get_all_region_types(
    (TARGET[0] + MARGIN, TARGET[1] + MARGIN)
)  # after checking, there is a good balance between all 3 types
INITIAL_TIME = 0
INITIAL_EQUIPMENT = 1
TRAVEL_TIME = 1  # from any location to a neighbouring, non-negative location
SWITCH_GEAR_TIME = 7

# step 2: visit the cave with a best-first search (and a priority queue) using the Manhattan distance as heuristic
visited = set()  # will store seen states (manhattan_dist, (x, y), time, equipment)
queue = []

# (0 : neither, 1 : torch, 2: climbing gear) in this region type

queue.append(
    (heuristic(ENTRANCE, INITIAL_TIME), ENTRANCE, INITIAL_TIME, INITIAL_EQUIPMENT)
)
min_time = float("inf")

while queue:
    heuristic_val, current_region, current_time, current_equipment = heapq.heappop(
        queue
    )
    if min_time <= current_time:
        continue  # I can already discard this state based on time spent
    if (
        heuristic_val,
        current_region,
        current_time,
        current_equipment,
    ) in visited:
        continue  # discard state if already seen
    if current_region == TARGET:
        path_time = current_time + (7 if current_equipment != 1 else 0)
        if path_time < min_time:
            min_time = path_time
            print(f"current best: {min_time}")
        continue
    visited.add((heuristic_val, current_region, current_time, current_equipment))
    x, y = current_region
    for x_neigh, y_neigh in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)):
        if (x_neigh, y_neigh) not in REGION_TYPES:
            continue
        neigh_region_type = REGION_TYPES[(x_neigh, y_neigh)]
        for required_equipment in ALLOWED_EQUIPMENTS[neigh_region_type]:
            new_equipment = required_equipment
            new_time = (
                current_time
                + TRAVEL_TIME
                + (0 if new_equipment == current_equipment else SWITCH_GEAR_TIME)
            )
            new_heuristic_val = heuristic((x_neigh, y_neigh), new_time)
            if (
                new_state := (
                    new_heuristic_val,
                    (x_neigh, y_neigh),
                    new_time,
                    new_equipment,
                )
            ) not in visited:
                heapq.heappush(queue, new_state)

print(f"part 2: {min_time=}")
