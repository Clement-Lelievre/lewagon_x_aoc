from collections import defaultdict
from tqdm import tqdm

INPUT = """177, 51
350, 132
276, 139
249, 189
225, 137
337, 354
270, 147
182, 329
118, 254
174, 280
42, 349
96, 341
236, 46
84, 253
292, 143
253, 92
224, 137
209, 325
243, 195
208, 337
197, 42
208, 87
45, 96
64, 295
266, 248
248, 298
194, 261
157, 74
52, 248
243, 201
242, 178
140, 319
69, 270
314, 302
209, 212
237, 217
86, 294
295, 144
248, 206
157, 118
155, 146
331, 40
247, 302
250, 95
193, 214
345, 89
183, 206
121, 169
79, 230
88, 155
"""


# note: rows and cols numbering is unlike the convention in this challenge (invert cols and rows, but still 0-indexed)

coords = set(tuple(map(int, elem.split(","))) for elem in INPUT.strip().split("\n"))

min_row = min(c[1] for c in coords)
max_row = max(c[1] for c in coords)
min_col = min(c[0] for c in coords)
max_col = max(c[0] for c in coords)

margin = 100  # arbitrarily chosen, used to pad the grid so as to not miss any point


def manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Computes and returns the Manhattan distance between point a and point b

    Args:
        a (tuple[int, int]): coordinates of point a
        b (tuple[int, int]): coordinates of point b

    Returns:
        int: distance between a and b, expressed in the grid unit
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# part 1
def point_on_perimeter(
    point: tuple[int],
    min_row=min_row,
    max_row=max_row,
    min_col=min_col,
    max_col=max_col,
    margin=margin,
) -> bool:
    """says if given `point` is on the perimeter of the grid

    Returns:
        bool: _description_
    """
    x, y = point
    return True if x in (min_col, max_col) or y in (min_row, max_row) else False


points_to_discard = (
    []
)  # points that are suspected to yield infinite surfaces, because a point on the bounding box is closer to them than to any other
coords_nb_closest_points = defaultdict(int)

for row in tqdm(range(-margin, max_row + margin)):
    for col in range(-margin, max_col + margin):
        if (current_point := (col, row)) in coords:
            coords_nb_closest_points[current_point] += 1
        else:
            distances = zip(
                coords,
                map(lambda coord: manhattan_distance(coord, current_point), coords),
            )
            distances = sorted(distances, key=lambda x: x[1])
            if (closest := distances[0])[1] != distances[1][
                1
            ]:  # if there is only 1 closest point, with no tie
                coords_nb_closest_points[closest[0]] += 1
                if point_on_perimeter(current_point):
                    points_to_discard.append(closest[0])

candidates = {
    k: v for k, v in coords_nb_closest_points.items() if k not in points_to_discard
}
print(max(candidates.values()))

# part 2
# What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?

max_dist: int = 10_000
region_size = sum(
    filter(
        None,
        (
            sum(manhattan_distance((y, x), coord) for coord in coords) < max_dist
            for x in tqdm(range(max_row + 1))
            for y in range(max_col + 1)
        ),
    )
)
print(region_size)

# I could optimize this in several ways, e.g. usoing a while loop instead and breaking when the sum of distances is > max_dist, but this wasn't necessary for the input I was given
