import re
from tqdm import tqdm
from itertools import combinations

INPUT = """Sensor at x=2288642, y=2282562: closest beacon is at x=1581951, y=2271709
Sensor at x=2215505, y=2975419: closest beacon is at x=2229474, y=3709584
Sensor at x=275497, y=3166843: closest beacon is at x=-626874, y=3143870
Sensor at x=1189444, y=2115305: closest beacon is at x=1581951, y=2271709
Sensor at x=172215, y=2327851: closest beacon is at x=-101830, y=2000000
Sensor at x=3953907, y=1957660: closest beacon is at x=2882446, y=1934422
Sensor at x=685737, y=2465261: closest beacon is at x=1581951, y=2271709
Sensor at x=1458348, y=2739442: closest beacon is at x=1581951, y=2271709
Sensor at x=3742876, y=2811554: closest beacon is at x=3133845, y=3162635
Sensor at x=437819, y=638526: closest beacon is at x=-101830, y=2000000
Sensor at x=2537979, y=1762726: closest beacon is at x=2882446, y=1934422
Sensor at x=1368739, y=2222863: closest beacon is at x=1581951, y=2271709
Sensor at x=2743572, y=3976937: closest beacon is at x=2229474, y=3709584
Sensor at x=2180640, y=105414: closest beacon is at x=3011118, y=-101788
Sensor at x=3845753, y=474814: closest beacon is at x=3011118, y=-101788
Sensor at x=2493694, y=3828087: closest beacon is at x=2229474, y=3709584
Sensor at x=2786014, y=3388077: closest beacon is at x=3133845, y=3162635
Sensor at x=3593418, y=3761871: closest beacon is at x=3133845, y=3162635
Sensor at x=856288, y=3880566: closest beacon is at x=2229474, y=3709584
Sensor at x=1757086, y=2518373: closest beacon is at x=1581951, y=2271709
Sensor at x=2853518, y=2939097: closest beacon is at x=3133845, y=3162635
Sensor at x=1682023, y=1449902: closest beacon is at x=1581951, y=2271709
Sensor at x=3360575, y=1739100: closest beacon is at x=2882446, y=1934422
Sensor at x=2904259, y=1465606: closest beacon is at x=2882446, y=1934422
Sensor at x=3078500, y=3564862: closest beacon is at x=3133845, y=3162635
Sensor at x=2835288, y=1011055: closest beacon is at x=2882446, y=1934422
Sensor at x=2998762, y=2414323: closest beacon is at x=2882446, y=1934422
"""

# INPUT = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

rows = [r for r in INPUT.splitlines() if r.strip()]
coord_pat = re.compile(r"(-?\d+)")

coords = [tuple(map(int, coord_pat.findall(row))) for row in rows]
coords = [
    (elem[:2][::-1], elem[2:][::-1]) for elem in coords
]  # I reverse coordinates because they're provided as col_nb, row_nb

# I need to offset the provided coordinates to have a positive grid that starts at 0,0
# e.g. the example provides the beacon point (-2, 15) meaning row 15, column -2, but I need to have (15,0) instead

# Plan:
# create a function to compute the Manhattan distance
# identify the sensors that do impact row # 2000000
# sum the row # 2000000


def manhattan_dist(point1: tuple[int], point2: tuple[int]) -> int:
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


impossible_spots = set()
TARGET_ROW_NB = 2_000_000 if len(INPUT.splitlines()) > 17 else 10

for sensor, beacon in coords:
    dist = manhattan_dist(sensor, beacon)
    if TARGET_ROW_NB in range(
        sensor[0] - dist, sensor[0] + dist + 1
    ):  # target row is impacted
        nb_elem = 2 * dist + 1 - 2 * abs(TARGET_ROW_NB - sensor[0])
        impossible_coords = range(
            sensor[1] - (nb_elem - 1) // 2, sensor[1] + (nb_elem - 1) // 2 + 1
        )  # just the col nbs is enough because they all share the same row number
        for ic in impossible_coords:
            impossible_spots.add(ic)

# now remove the number of unique beacons and sensors that happen to be on the row number we're interested in
beacons_on_target_row = set(
    [beacon[1] for _, beacon in coords if beacon[0] == TARGET_ROW_NB]
)
answer = len(impossible_spots) - len(beacons_on_target_row)

print(answer)
# part 2 # the massive size of the grid is a tipoff that some smart computation must be performed instead of looping or building the grid
# below in comments, the naïve approach (works on the test input but doesn't scale)

# MAX_SEARCH = 4_000_000 if len(INPUT.splitlines()) > 17 else 20
# search_space = (
#     (x, y) for x in range(MAX_SEARCH) for y in range(MAX_SEARCH)
# )  # generator so it's memory efficient

# for sensor, beacon in tqdm(coords):
#     dist = manhattan_dist(sensor, beacon)
#     is_out_of_zone = (
#         lambda coord: True
#         if manhattan_dist(coord, sensor)
#         > dist  # or (coord[0]+coord[1] < sensor[0] - dist))
#         else False
#     )
#     search_space = frozenset(
#         filter(is_out_of_zone, search_space)
#     )  # this is the bottleneck, especially at the first iteration of the loop

# print(list(search_space))

# drawing the 'diamond' shapes, it seems that the fact there is a unique point that isn't on any diamond
# means there must be some parallel edges between some of the diamonds, only separated by a distance 1
# I found that by drawing the coveted point surrounded by 8 points that belong to at least 1 diamond shape

# let us first try to find those parallels

# generate the lines coeff from a diamond
def get_diamond_edge_points(data) -> tuple[tuple[int]]:
    '''Returns the slope and intercept of each of the four straight lines created by the diamond shape'''
    sensor, beacon = data
    dist = manhattan_dist(sensor, beacon)
    
    west = (sensor[0], sensor[1] - dist)
    east = (sensor[0], sensor[1]+dist)
    north = (sensor[0]-dist, sensor[1])
    south = (sensor[0]+dist, sensor[1])
    
    slope1 = (north[1] - west[1]) // (north[0]-west[0])
    intercept1 = west[1] - slope1*west[0]
    line1_points = set((x, slope1*x+intercept1) for x in range(north[0], west[0]+1))
    
    slope2 = (south[1] - west[1]) // (south[0]-west[0])
    intercept2 = west[1] - slope2*west[0]
    line2_points = set((x, slope2*x+intercept2) for x in range(west[0], south[0]+1))
    
    slope3 = (south[1] - east[1]) // (south[0]-east[0])
    intercept3 = east[1] - slope3*east[0]
    line3_points = set((x, slope3*x+intercept3) for x in range(south[0], east[0]+1))
    
    slope4 = (north[1] - east[1]) // (north[0]-east[0])
    intercept4 = east[1] - slope4*east[0]
    line4_points = set((x, slope4*x+intercept4) for x in range(north[0], east[0]+1))
    
    return line1_points.union(line2_points).union(line3_points).union(line4_points)
    
diamond_edges = [get_diamond_edge_points(data) for data in coords]    
# parallel_lines = []
# for line_1, line_2 in combinations(unique_lines, 2):
#     if line_1[0] == line_2[0] and abs(line_1[1] - line_2[1]) == 2:
#         parallel_lines.append(line_1)
#         parallel_lines.append(line_2)

# print(parallel_lines)

# find crossing points
def get_crossing_point(line_1, line_2):
    slope1, intercept1 = line_1
    slope2, intercept2 = line_2
    return (intercept2 - intercept1) / (slope1 - slope2) if slope1 != slope2 else None

# look at intercepting points
all_crossing_points = set()
for diamond1, diamond2 in combinations(diamond_edges, 2):
    s = diamond1.intersection(diamond2)
    for point in s:
        all_crossing_points.add(point)
        
print(sorted(all_crossing_points))
