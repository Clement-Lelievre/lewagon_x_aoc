import pandas as pd
from tqdm import tqdm

SERIAL_NB = 5719


def get_power_level(coord: tuple[int, int], serial_nb: int = SERIAL_NB) -> int:
    x, y = coord
    rack_id = x + 10
    nb = (y * rack_id + serial_nb) * rack_id
    nb = (nb // 100) % 10
    return nb - 5


# tests provided
tests = ((3, 5, 8, 4), (122, 79, 57, -5), (217, 196, 39, 0), (101, 153, 71, 4))
for item in tests:
    *coord, serial_nb, solution = item
    assert get_power_level(coord, serial_nb) == solution

df = pd.DataFrame({f"{x}": [(x, y) for y in range(1, 301)] for x in range(1, 301)})
df.index = range(1, 301)
grid = df.applymap(get_power_level).to_numpy()
current_best = 0
answer = None
for x in range(298):
    for y in range(298):
        if (cb := grid[y : y + 3, x : x + 3].sum()) > current_best:
            current_best = cb
            answer = x + 1, y + 1

print("part 1:", answer)

# part 2
current_best = 0
answer = None
best_size = 0
for size in tqdm(
    range(2, 301)
):  # it is not satisfying to resort to a for loop here, better to use Numpy. there's a lot of repeated calcs
    for x in range(300 - size):
        for y in range(300 - size):
            if (cb := grid[y : y + size, x : x + size].sum()) > current_best:
                current_best = cb
                answer = x + 1, y + 1
                best_size = size

print("part 2:", answer, best_size)
