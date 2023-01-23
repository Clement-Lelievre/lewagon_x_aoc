import numpy as np

INPUT = """addx 1
addx 5
noop
addx -1
noop
addx 3
addx 29
addx -1
addx -21
addx 5
noop
addx -20
addx 21
addx 2
addx 8
addx -1
noop
noop
noop
noop
addx 6
addx -1
addx -37
addx 40
addx -10
addx -25
addx 5
addx 2
addx 5
noop
noop
noop
addx 21
addx -20
addx 2
noop
addx 3
addx 2
addx -5
addx 12
addx 3
noop
addx 2
addx 3
addx -2
addx -37
addx 1
addx 5
addx 3
addx -2
addx 2
addx 29
addx -22
addx 13
noop
addx -8
addx -6
addx 7
addx 2
noop
addx 7
addx -2
addx 5
addx 2
addx -26
addx -11
noop
noop
addx 6
addx 1
addx 1
noop
addx 4
addx 5
noop
noop
addx -2
addx 3
noop
addx 2
addx 5
addx 2
addx -22
addx 27
addx -1
addx 1
addx 5
addx 2
noop
addx -39
addx 22
noop
addx -15
addx 3
addx -2
addx 2
addx -2
addx 9
addx 3
noop
addx 2
addx 3
addx -2
addx 2
noop
noop
noop
addx 5
addx -17
addx 24
addx -7
addx 8
addx -36
addx 2
addx 3
addx 33
addx -32
addx 4
addx 1
noop
addx 5
noop
noop
addx 20
addx -15
addx 4
noop
addx 1
noop
addx 4
addx 6
addx -30
addx 30
noop
noop
noop
noop
noop
"""

x = 1
instructions = [inst for inst in INPUT.splitlines() if inst.strip()]
all_values = []

nbs = (20, 60, 100, 140, 180, 220)
solution = 0
for nb in nbs:
    answer = 1
    cycle = 0
    inst_nb = 0
    while cycle < nb - 2:
        if (elem := instructions[inst_nb]).startswith("n"):
            cycle += 1
        else:
            answer += int(elem.split()[-1])
            cycle += 2
        inst_nb += 1
    # print(nb, answer, f'last instruction: {elem}')
    solution += answer * nb

print(solution)

# part 2
# the X register controls the horizontal position of a sprite. Specifically,
# the sprite is 3 pixels wide, and the X register sets
# the horizontal position of the middle of that sprite
# If the sprite is positioned such that one of its three pixels is the pixel
# currently being drawn, the screen produces a lit pixel (#);
# otherwise, the screen leaves the pixel dark (.)


x = 1
sprite = [x - 1, x, x + 1]
nb_pixels = 40 * 6
pixel_currently_drawn_ind = 0
drawing = []
cycle = 0
inst_nb = 0

while cycle < nb_pixels:
    # compute x
    if (elem := instructions[inst_nb]).startswith("n"):
        # check if pixel lit or not
        if pixel_currently_drawn_ind % 40 in sprite:
            drawing.append("#")
        else:
            drawing.append(
                " "
            )  # space will be clearer than a dot when reading the image
        cycle += 1
        pixel_currently_drawn_ind += 1
        # print(f'{elem},{cycle=}, {sprite=}, {"".join(drawing)}')
    else:
        for _ in range(2):
            # check if pixel lit or not
            if pixel_currently_drawn_ind % 40 in sprite:
                drawing.append("#")
            else:
                drawing.append(" ")  # will be clearer than a dot when reading
                # the image
            pixel_currently_drawn_ind += 1
            cycle += 1
            # print(f'{elem},{cycle=}, {sprite=}, {"".join(drawing)}')
        # update the sprite
        x += int(elem.split()[-1])
        sprite = [x - 1, x, x + 1]
    inst_nb += 1


# displaying the image (could add an OCR layer instead)
image = np.array(drawing).reshape(6, 40)
for row in image:
    print(*row)
