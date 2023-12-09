"""AoC 2023 day 5: https://adventofcode.com/2023/day/5
Usage: python day5.py day5_input.txt
"""

import argparse


TEST_DATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# given the size of the numbers in my input, it is a bad idea
# to use a dict for the mappings

# there are:
# "number ranges": the ranges of actual numbers I'll have, starting with the top row
# "operation ranges": ranges that define the numbers onto which a transformation will be applied
# "transformations": an addition or a subtraction; as defined in the text and used in part 1


def main_p1(text: str) -> int:
    lines = iter([line for line in text.split("\n") if line.strip()])
    current_nbs = [int(seq) for seq in next(lines).split()[1:] if seq.isdigit()]
    next_nbs = []
    for line in lines:
        if "-" in line:
            were_not_in_range = [elem for elem in current_nbs if elem not in next_nbs]
            current_nbs = next_nbs
            current_nbs.extend(were_not_in_range)
            next_nbs = []
            continue
        numbers = [int(seq) for seq in line.split()]
        source_range = range(numbers[1], numbers[1] + numbers[2])
        dest_range = range(numbers[0], numbers[0] + numbers[2])
        for nb in current_nbs:
            if nb in source_range:  # O(1)
                next_nbs.append(dest_range[0] + nb - source_range[0])
                current_nbs = [nb_ for nb_ in current_nbs if nb_ != nb]
    were_not_in_range = [elem for elem in current_nbs if elem not in next_nbs]
    current_nbs = next_nbs
    current_nbs.extend(were_not_in_range)
    print(f"part1: {min(current_nbs)}")
    return min(current_nbs)


def main_p2(text: str) -> int:
    # apply transformations on ranges, not on numbers, else will OOM
    # I'll use the `range` class and the "and" operator to get the intersection of several ranges
    lines = iter([line for line in text.split("\n") if line.strip()])
    current_nbs = [int(seq) for seq in next(lines).split()[1:] if seq.isdigit()]
    number_ranges = [
        range(current_nbs[i], current_nbs[i] + current_nbs[i + 1])
        for i in range(0, len(current_nbs), 2)
    ]
    next_number_ranges = []
    for line in lines:
        if "-" in line:
            next_number_ranges.extend(number_ranges)
            number_ranges = next_number_ranges
            next_number_ranges = []
            continue
        assert line.strip()
        numbers = [int(seq) for seq in line.split()]
        assert len(numbers) == 3
        operation_range = range(numbers[1], numbers[1] + numbers[2])
        for number_range in tuple(number_ranges):
            if intersection := range(
                max(operation_range.start, number_range.start),
                min(operation_range.stop, number_range.stop),
            ):
                next_number_ranges.append(
                    range(
                        intersection.start + numbers[0] - numbers[1],
                        intersection.stop + numbers[0] - numbers[1],
                    )
                )
                number_ranges.remove(number_range)  # remove the whole range
                range1, range2 = range(number_range.start, intersection.start), range(
                    intersection.stop, number_range.stop
                )
                if range1:
                    number_ranges.append(
                        range1
                    )  # put back difference; insertion order does not matter
                if range2:
                    number_ranges.append(
                        range2
                    )  # put back difference; insertion order does not matter
    answer = min(
        min(range_[0] for range_ in next_number_ranges),
        min(
            range_[0] for range_ in number_ranges
        ),  # at the last iteration we haven't yet considered remaining numbers in number_ranges
        # the minimum location might be in it
    )
    print(f"part2: {answer}")
    return answer


if __name__ == "__main__":
    assert main_p1(TEST_DATA) == 35, "should be 35 for the test input p1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Input filepath", type=str)
    args = parser.parse_args()
    input_path = args.input_path
    with open(input_path, "r") as f:
        text = f.read()
    main_p1(text)
    assert main_p2(TEST_DATA) == 46, "should be 46 for the test input p2"
    main_p2(text)
