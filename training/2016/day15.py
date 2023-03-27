import re
from functools import reduce

pat = re.compile(r"has\s(\d+).*?(\d+)\.")

INPUT = """Disc #1 has 13 positions; at time=0, it is at position 1.
Disc #2 has 19 positions; at time=0, it is at position 10.
Disc #3 has 3 positions; at time=0, it is at position 2.
Disc #4 has 7 positions; at time=0, it is at position 1.
Disc #5 has 5 positions; at time=0, it is at position 3.
Disc #6 has 17 positions; at time=0, it is at position 5.
"""


clean_input = INPUT.strip().splitlines()
nb_items = 50_000  # arbitrary
while True:  # keep increasing the number of elems if needed
    all_valid_start_times = []
    print(f"storing {nb_items=}...")
    for i in range(1, len(clean_input) + 1):
        assert (ps := pat.search(clean_input[i - 1])) is not None
        nb_pos, pos_at_start = int(ps.group(1)), int(ps.group(2))
        valid_start_times = frozenset(
            (nb_pos - (pos_at_start + i) % nb_pos) + nb_pos * k for k in range(nb_items)
        )  # the frozenset data structure is not mandatory here
        all_valid_start_times.append(valid_start_times)
    valid_vals = reduce(lambda x, y: x.intersection(y), all_valid_start_times)
    try:
        print("part 1:", min(valid_vals))
        break
    except ValueError:
        nb_items *= 2

# part 2
# I manually appended to my input with the newer disc
INPUT = """Disc #1 has 13 positions; at time=0, it is at position 1.
Disc #2 has 19 positions; at time=0, it is at position 10.
Disc #3 has 3 positions; at time=0, it is at position 2.
Disc #4 has 7 positions; at time=0, it is at position 1.
Disc #5 has 5 positions; at time=0, it is at position 3.
Disc #6 has 17 positions; at time=0, it is at position 5.
Disc #7 has 11 positions; at time=0, it is at position 0.
"""
clean_input = INPUT.strip().splitlines()
nb_items = (
    1_000_000  # arbitrary, higher than before because I'm expecting it takes longer now
)
while True:  # keep increasing the number of elems if needed
    all_valid_start_times = []
    print(f"storing {nb_items=}...")
    for i in range(1, len(clean_input) + 1):
        assert (ps := pat.search(clean_input[i - 1])) is not None
        nb_pos, pos_at_start = int(ps.group(1)), int(ps.group(2))
        valid_start_times = frozenset(
            (nb_pos - (pos_at_start + i) % nb_pos) + nb_pos * k for k in range(nb_items)
        )  # the frozenset data structure is not mandatory here
        all_valid_start_times.append(valid_start_times)
    valid_vals = reduce(lambda x, y: x.intersection(y), all_valid_start_times)
    try:
        print("part 2:", min(valid_vals))
        break
    except ValueError:
        nb_items *= 2

# to get a x19 speedup, notice that the largest disc has 19 positions so you could write down when it gets aligned
# and then iterate. You need to wait 7 sec, 26 sec, 45 sec etc. so you can iterate on these values only and detect the first
# alignment of all values
