"""this would need refacto as currently , following my modifs for part 2 part 1 types are no longer correct"""

actual_input=...
example_input = "2333133121414131402"
example_input_small = "12345"
three_consecutive_blocks = "40102"
a = "19123"
more_than_nine = "10" * 11  # to check that ids go > 9 not just 0 to 9 included

# part 1
# what I initially got wrong was that I used strs instead of a list of strs, so the checksum was wrong because at the char level instead of at the integer level


def to_ids(blocks: str) -> list[str]:
    ids = []
    for ind, char in enumerate(blocks):
        new = [str(ind // 2)] * int(char) if ind % 2 == 0 else list("." * int(char))
        ids.extend(new)
    return ids


def move_blocks_left(ids: list[str]) -> list[str]:
    leftmost_dot_index = 0
    for i in range(len(ids) - 1, -1, -1):
        if (val := ids[i]) == ".":
            continue
        for j in range(leftmost_dot_index, i):
            if ids[j] == ".":
                ids[i] = "."
                ids[j] = val
                leftmost_dot_index = j + 1
                assert leftmost_dot_index < len(ids)
                break
        else:
            break
    return ids


def compute_checksum(moved_blocks: list[str]) -> int:
    s = 0
    for ind, val in enumerate(moved_blocks):
        if val == ".":
            continue
        s += ind * int(val)
    return s


def solve_p1(inp: str) -> int:
    ids = to_ids(inp)
    print("got ids")
    moved_blocks = move_blocks_left(ids)
    print("moved blocks")
    checksum = compute_checksum(moved_blocks)
    print(f"computed checksum: {checksum}")
    return checksum


# part 2

def make_groups(ids: list[str]) -> list[list[str]]:
    grouped = []
    i = 0
    while i < len(ids):
        char = ids[i]
        to_add = []
        while i < len(ids) and ids[i] == char:
            to_add.append(ids[i])
            i += 1
        grouped.append(to_add)
    return grouped


def move_blocks_left_p2(ids: list[str]) -> list[str]:
    grouped = make_groups(ids)
    leftmost_dot_index = 0
    for i in range(len(grouped) - 1, -1, -1):
        if "." in (blocks := grouped[i]):
            continue
        for j in range(leftmost_dot_index, i):
            if grouped[j].count(".") >= len(blocks):
                grouped[j] = (
                    grouped[j][: grouped[j].index(".")]
                    + grouped[i]
                    + grouped[j][grouped[j].index(".") + len(blocks) :]
                )
                grouped[i] = list("." * len(blocks))
                j += 1
                # print(grouped, end="\n\n")
                break
    # flatten the list
    print("flattening")
    final = []
    for group in grouped:
        final.extend(group)
    # print(final)
    return final


def solve_p2(inp: str) -> int:
    ids = to_ids(inp)
    print("got ids")
    moved_blocks = move_blocks_left_p2(ids)
    print("moved blocks")
    checksum = compute_checksum(moved_blocks)
    print(f"computed checksum: {checksum}")
    return checksum


if __name__ == "__main__":
    assert (a := make_groups(["1", "1", ".", ".", ".", "61"])) == [
        ["1", "1"],
        [".", ".", "."],
        ["61"],
    ], f"found {a}"
    assert to_ids(more_than_nine) == [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
    ], f"{to_ids(more_than_nine)}"
    assert (r := move_blocks_left(to_ids(more_than_nine))) == to_ids(
        more_than_nine
    ), f"{r}"
    assert (res := solve_p1(more_than_nine)) == 385, f"{res}"
    assert len(more_than_nine) == 22
    assert (ids_small := to_ids(example_input_small)) == [
        "0",
        ".",
        ".",
        "1",
        "1",
        "1",
        ".",
        ".",
        ".",
        ".",
        "2",
        "2",
        "2",
        "2",
        "2",
    ], f"found {ids_small}"
    assert (ids := to_ids(example_input)) == [
        "0",
        "0",
        ".",
        ".",
        ".",
        "1",
        "1",
        "1",
        ".",
        ".",
        ".",
        "2",
        ".",
        ".",
        ".",
        "3",
        "3",
        "3",
        ".",
        "4",
        "4",
        ".",
        "5",
        "5",
        "5",
        "5",
        ".",
        "6",
        "6",
        "6",
        "6",
        ".",
        "7",
        "7",
        "7",
        ".",
        "8",
        "8",
        "8",
        "8",
        "9",
        "9",
    ], f"found {ids}"
    assert to_ids(three_consecutive_blocks) == ["0", "0", "0", "0", "1", "2", "2"]
    assert to_ids(a) == [
        "0",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        "1",
        ".",
        ".",
        "2",
        "2",
        "2",
    ], f"{to_ids(a)}"
    assert (moved_blocks_small := move_blocks_left(ids_small)) == [
        "0",
        "2",
        "2",
        "1",
        "1",
        "1",
        "2",
        "2",
        "2",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
    ], f"found {moved_blocks_small}"
    assert (moved_blocks := move_blocks_left(ids)) == list(
        "0099811188827773336446555566.............."
    ), f"found {moved_blocks}"
    assert move_blocks_left(to_ids(a)) == list("02221...........")
    assert compute_checksum(moved_blocks) == 1928

    assert (res := solve_p1(example_input)) == 1928, f"{res}"
    solve_p1(actual_input)

    assert solve_p2(example_input) == 2858
    solve_p2(actual_input)
