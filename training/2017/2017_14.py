from functools import reduce
from collections import deque

# reusing my code from 2017 day 10


def length_to_ascii(length) -> int:
    s = str(length)
    nchars = len(s)
    return sum(
        ord(s[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars)
    )  # found on SO


XOR = lambda x, y: x ^ y  # alternatively, use operator.xor
HEX = lambda x: res if len((res := f"{x:x}")) == 2 else "0" + res
HEX_TO_BINARY = lambda x: bin(int(x, 16))[2:].zfill(4)


def nb_occupied_squares(lengths: str) -> str:
    """Executing sequentially the hashing steps described in 2017 day 10

    Args:
        lengths (str): the input

    Returns:
        str: the knot hash
    """
    numbers = list(range(256))
    actual_input = [length_to_ascii(length) for length in lengths]
    actual_input.extend([17, 31, 73, 47, 23])

    current_ind = 0
    skip_size = 0
    for _ in range(64):
        for length in actual_input:
            if length > len(numbers):
                continue
            numbers = numbers[current_ind:] + numbers[:current_ind]
            numbers = numbers[:length][::-1] + numbers[length:]
            numbers = numbers[-current_ind:] + numbers[:-current_ind]
            current_ind = (current_ind + length + skip_size) % len(numbers)
            skip_size += 1
    assert len(numbers) == 256

    output = [reduce(XOR, numbers[i : i + 16]) for i in range(0, len(numbers), 16)]
    assert len(output) == 16
    assert 0 <= min(output) <= max(output) <= 255
    hex_ = "".join(map(HEX, output))
    assert len(hex_) == 32
    answer = "".join(map(HEX_TO_BINARY, hex_))
    return answer


occupied = 0
for row_nb in range(128):
    key_string = f"nbysizxe-{row_nb}"
    occupied += nb_occupied_squares(key_string).count("1")
print(f"part 1: {occupied}")

# part 2
# get the grid
grid = [list(nb_occupied_squares(f"nbysizxe-{row_nb}")) for row_nb in range(128)]
# retain only occupied squares
grid = {
    (row, col): elem
    for row in range(len(grid))
    for col in range(len(grid[0]))
    if (elem := grid[row][col]) == "1"
}
# let's do a search on the grid to mark the regions
visited = set()
current_region = 0

for x, y in grid:
    if (x, y) in visited:
        continue
    queue = deque()  # the queue to search the current region
    queue.append((x, y))
    while queue:
        x, y = queue.pop()
        visited.add((x, y))
        for neigh in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            if neigh not in visited and neigh in grid:
                queue.append(neigh)
    current_region += 1

print(f"part 2: {current_region}")
