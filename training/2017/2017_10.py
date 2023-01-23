from functools import reduce

numbers = list(range(256))
lengths = [18, 1, 0, 161, 255, 137, 254, 252, 14, 95, 165, 33, 181, 168, 2, 188]
current_ind = 0
skip_size = 0

for length in lengths:
    if length > len(numbers):
        continue
    numbers = numbers[current_ind:] + numbers[:current_ind]
    numbers = numbers[:length][::-1] + numbers[length:]
    numbers = numbers[-current_ind:] + numbers[:-current_ind]
    current_ind = (current_ind + length + skip_size) % len(numbers)
    skip_size += 1


answer = numbers[0] * numbers[1]
print("part 1:", answer)

# part 2
def length_to_ascii(length) -> int:
    s = str(length)
    nchars = len(s)
    return sum(
        ord(s[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars)
    )  # found on SO


XOR = lambda x, y: x ^ y  # alternatively, use operator.xor
HEX = lambda x: res if len((res := f"{x:x}")) == 2 else "0" + res


def solve_part2(lengths: str) -> str:
    """Executing sequentially the hashing steps described in the challenge

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
    answer = "".join(map(HEX, output))
    assert len(answer) == 32
    return answer


tests = (
    ("", "a2582a3a0e66e6e86e3812dcb672a272"),
    ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
    ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
    ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
)

for input_, output in tests:
    assert solve_part2(input_) == output

my_input = "18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188"
answer = solve_part2(my_input)
print("part 2:", answer)
