from collections import deque

DEPTH = 5616
TARGET = (10, 785)
ENTRANCE = (0, 0)

DEPTH = 510
TARGET = (10, 10)

erosion_levels = {}
region_types = {}
TARGET_X, TARGET_Y = TARGET

queue = deque()
queue.append(ENTRANCE)
queue.extend(
    sorted(
        [(i, 0) for i in range(1, TARGET_X + 1)]
        + [(0, i) for i in range(1, TARGET_Y + 1)],
        key=sum,
    )
)
queue.append(TARGET)
visited = set()


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


while queue:
    current_region = queue.popleft()
    if current_region in visited:
        continue
    geo_index = get_geologic_index(*current_region)
    ero_level = get_erosion_level(geo_index)
    erosion_levels[current_region] = ero_level
    region_types[current_region] = get_region_type(ero_level)
    visited.add(current_region)  # mark as visited
    # add neighbours
    x, y = current_region
    for x_neigh, y_neigh in ((x, y + 1), (x + 1, y)):
        if (
            x_neigh <= TARGET_X
            and y_neigh <= TARGET_Y
            and (x_neigh, y_neigh) not in visited
        ):
            queue.append((x_neigh, y_neigh))


print("part 1:", sum(region_types.values()))

# part 2
# this looks a like a shortest path search in an undirected, weighted graph
current_equipment = 1  # 0 : neither, 1 : torch, 2: climbing gear

queue = deque()
queue.append(ENTRANCE)
# I need to think about this one and come back to it, as a mere BFS won't do, it looks more like A* is required here
