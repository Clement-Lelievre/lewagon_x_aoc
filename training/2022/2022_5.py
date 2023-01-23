import re

STACKS = """
        [Q] [B]         [H]        
    [F] [W] [D] [Q]     [S]        
    [D] [C] [N] [S] [G] [F]        
    [R] [D] [L] [C] [N] [Q]     [R]
[V] [W] [L] [M] [P] [S] [M]     [M]
[J] [B] [F] [P] [B] [B] [P] [F] [F]
[B] [V] [G] [J] [N] [D] [B] [L] [V]
[D] [P] [R] [W] [H] [R] [Z] [W] [S]
 1   2   3   4   5   6   7   8   9"""

INSTRUCTIONS = """move 1 from 4 to 1
move 2 from 4 to 8
move 5 from 9 to 6
move 1 from 1 to 3
move 5 from 8 to 3
move 1 from 1 to 5
move 4 from 3 to 6
move 14 from 6 to 2
move 5 from 4 to 5
move 7 from 7 to 2
move 24 from 2 to 3
move 13 from 3 to 2
move 1 from 7 to 9
move 1 from 9 to 5
move 7 from 2 to 6
move 3 from 1 to 7
move 3 from 6 to 3
move 2 from 7 to 1
move 1 from 7 to 5
move 2 from 2 to 6
move 2 from 1 to 4
move 9 from 5 to 1
move 1 from 6 to 3
move 4 from 5 to 4
move 1 from 2 to 7
move 4 from 6 to 2
move 7 from 2 to 3
move 2 from 2 to 6
move 2 from 2 to 3
move 2 from 5 to 4
move 1 from 7 to 3
move 4 from 6 to 7
move 19 from 3 to 6
move 3 from 7 to 4
move 1 from 7 to 8
move 1 from 8 to 1
move 2 from 1 to 3
move 10 from 3 to 2
move 3 from 3 to 8
move 1 from 3 to 9
move 1 from 9 to 6
move 11 from 6 to 8
move 2 from 3 to 8
move 6 from 4 to 3
move 3 from 4 to 1
move 7 from 2 to 8
move 1 from 3 to 6
move 6 from 8 to 5
move 1 from 4 to 6
move 9 from 6 to 9
move 6 from 3 to 8
move 1 from 3 to 5
move 10 from 1 to 3
move 11 from 8 to 7
move 1 from 3 to 5
move 1 from 1 to 8
move 5 from 9 to 2
move 1 from 6 to 3
move 5 from 3 to 6
move 1 from 3 to 5
move 4 from 6 to 4
move 1 from 5 to 9
move 6 from 2 to 4
move 2 from 2 to 9
move 5 from 5 to 1
move 2 from 1 to 7
move 10 from 8 to 3
move 1 from 8 to 6
move 3 from 6 to 3
move 6 from 4 to 2
move 8 from 3 to 8
move 3 from 4 to 8
move 4 from 2 to 1
move 3 from 5 to 3
move 4 from 7 to 6
move 2 from 9 to 3
move 1 from 2 to 9
move 1 from 2 to 3
move 2 from 4 to 8
move 1 from 7 to 9
move 5 from 7 to 8
move 2 from 7 to 3
move 14 from 3 to 2
move 3 from 9 to 5
move 1 from 3 to 1
move 1 from 7 to 4
move 3 from 9 to 8
move 7 from 8 to 9
move 7 from 2 to 5
move 2 from 3 to 7
move 2 from 7 to 6
move 16 from 8 to 9
move 4 from 6 to 5
move 1 from 2 to 5
move 21 from 9 to 5
move 3 from 9 to 3
move 6 from 1 to 4
move 1 from 1 to 9
move 1 from 1 to 4
move 2 from 6 to 3
move 3 from 4 to 6
move 3 from 4 to 8
move 1 from 9 to 4
move 2 from 4 to 6
move 4 from 3 to 6
move 1 from 3 to 4
move 1 from 4 to 9
move 1 from 9 to 8
move 1 from 8 to 6
move 6 from 2 to 1
move 2 from 8 to 4
move 6 from 1 to 8
move 23 from 5 to 9
move 1 from 4 to 7
move 1 from 7 to 1
move 22 from 9 to 7
move 4 from 8 to 7
move 1 from 5 to 2
move 1 from 1 to 9
move 2 from 8 to 4
move 6 from 6 to 3
move 2 from 9 to 5
move 18 from 7 to 4
move 18 from 4 to 5
move 1 from 2 to 7
move 1 from 8 to 4
move 6 from 7 to 2
move 5 from 4 to 5
move 1 from 3 to 1
move 1 from 7 to 2
move 4 from 3 to 4
move 1 from 3 to 4
move 1 from 1 to 7
move 1 from 5 to 8
move 3 from 4 to 3
move 3 from 3 to 8
move 2 from 8 to 3
move 2 from 4 to 8
move 2 from 7 to 5
move 1 from 7 to 9
move 2 from 3 to 1
move 1 from 9 to 7
move 4 from 2 to 3
move 1 from 8 to 9
move 2 from 1 to 8
move 2 from 2 to 4
move 1 from 9 to 1
move 4 from 6 to 8
move 1 from 2 to 7
move 1 from 4 to 7
move 4 from 8 to 2
move 1 from 4 to 3
move 1 from 1 to 9
move 4 from 8 to 1
move 2 from 2 to 1
move 3 from 3 to 9
move 2 from 7 to 1
move 32 from 5 to 1
move 1 from 8 to 7
move 6 from 5 to 1
move 2 from 7 to 6
move 1 from 9 to 5
move 1 from 3 to 2
move 1 from 5 to 9
move 2 from 6 to 1
move 1 from 3 to 7
move 1 from 9 to 8
move 36 from 1 to 4
move 1 from 8 to 9
move 5 from 4 to 9
move 6 from 9 to 3
move 2 from 2 to 9
move 3 from 1 to 9
move 1 from 3 to 2
move 30 from 4 to 8
move 1 from 7 to 5
move 1 from 3 to 5
move 3 from 3 to 4
move 2 from 8 to 5
move 3 from 9 to 8
move 3 from 9 to 3
move 19 from 8 to 6
move 2 from 3 to 5
move 3 from 4 to 3
move 1 from 4 to 7
move 8 from 1 to 8
move 1 from 3 to 2
move 1 from 7 to 6
move 4 from 5 to 3
move 1 from 1 to 7
move 2 from 5 to 4
move 1 from 9 to 4
move 12 from 6 to 2
move 1 from 7 to 8
move 6 from 2 to 9
move 3 from 6 to 7
move 2 from 7 to 5
move 6 from 2 to 3
move 8 from 3 to 5
move 5 from 6 to 8
move 5 from 3 to 6
move 1 from 9 to 4
move 1 from 9 to 8
move 5 from 5 to 9
move 3 from 4 to 6
move 1 from 4 to 9
move 1 from 7 to 5
move 1 from 3 to 5
move 8 from 9 to 2
move 3 from 9 to 6
move 27 from 8 to 2
move 10 from 6 to 9
move 1 from 6 to 4
move 1 from 4 to 9
move 2 from 5 to 6
move 5 from 5 to 3
move 2 from 6 to 9
move 5 from 3 to 2
move 12 from 9 to 3
move 5 from 3 to 1
move 3 from 1 to 5
move 1 from 9 to 8
move 1 from 5 to 2
move 1 from 2 to 1
move 1 from 1 to 6
move 1 from 5 to 3
move 34 from 2 to 4
move 8 from 3 to 9
move 1 from 6 to 1
move 1 from 8 to 5
move 4 from 2 to 8
move 3 from 8 to 7
move 1 from 7 to 2
move 7 from 9 to 8
move 1 from 9 to 6
move 2 from 5 to 1
move 1 from 6 to 9
move 1 from 9 to 5
move 2 from 2 to 5
move 5 from 8 to 6
move 2 from 8 to 5
move 1 from 1 to 3
move 12 from 4 to 6
move 2 from 7 to 1
move 4 from 1 to 6
move 3 from 2 to 3
move 1 from 8 to 5
move 1 from 2 to 6
move 1 from 1 to 9
move 1 from 9 to 5
move 16 from 4 to 1
move 4 from 3 to 1
move 8 from 1 to 8
move 1 from 4 to 1
move 6 from 5 to 8
move 1 from 5 to 7
move 12 from 6 to 9
move 7 from 1 to 5
move 2 from 1 to 7
move 1 from 7 to 1
move 9 from 9 to 6
move 15 from 6 to 2
move 2 from 9 to 7
move 4 from 4 to 5
move 2 from 2 to 9
move 3 from 7 to 5
move 2 from 1 to 3
move 1 from 7 to 1
move 10 from 2 to 3
move 6 from 8 to 6
move 3 from 9 to 2
move 14 from 5 to 6
move 1 from 8 to 4
move 5 from 8 to 2
move 2 from 2 to 3
move 24 from 6 to 1
move 3 from 1 to 2
move 9 from 2 to 9
move 1 from 4 to 3
move 1 from 4 to 2
move 1 from 8 to 4
move 23 from 1 to 4
move 3 from 2 to 4
move 2 from 1 to 2
move 1 from 8 to 4
move 3 from 3 to 5
move 3 from 3 to 4
move 3 from 5 to 8
move 3 from 2 to 7
move 2 from 3 to 8
move 15 from 4 to 3
move 2 from 4 to 1
move 19 from 3 to 9
move 1 from 7 to 2
move 1 from 2 to 5
move 1 from 5 to 4
move 1 from 7 to 6
move 1 from 7 to 4
move 3 from 8 to 3
move 1 from 8 to 4
move 5 from 3 to 8
move 1 from 3 to 6
move 22 from 9 to 2
move 17 from 2 to 6
move 3 from 9 to 3
move 9 from 4 to 9
move 6 from 4 to 9
move 5 from 2 to 6
move 1 from 4 to 2
move 1 from 4 to 9
move 1 from 1 to 6
move 19 from 9 to 2
move 4 from 8 to 7
move 1 from 1 to 5
move 1 from 5 to 3
move 1 from 8 to 1
move 1 from 8 to 2
move 4 from 3 to 7
move 12 from 6 to 1
move 3 from 7 to 3
move 7 from 2 to 7
move 9 from 2 to 6
move 4 from 2 to 6
move 13 from 1 to 4
move 8 from 6 to 4
move 16 from 4 to 8
move 12 from 7 to 6
move 3 from 8 to 3
move 1 from 1 to 2
move 4 from 3 to 8
move 5 from 8 to 9
move 27 from 6 to 8
move 2 from 3 to 7
move 2 from 2 to 8
move 2 from 7 to 5
move 1 from 5 to 9
move 1 from 5 to 1
move 1 from 6 to 9
move 2 from 6 to 2
move 2 from 2 to 6
move 2 from 9 to 2
move 3 from 4 to 3
move 1 from 1 to 9
move 5 from 9 to 8
move 1 from 9 to 5
move 2 from 2 to 6
move 2 from 4 to 6
move 1 from 3 to 7
move 1 from 5 to 6
move 1 from 6 to 7
move 6 from 6 to 8
move 2 from 7 to 5
move 2 from 3 to 2
move 34 from 8 to 1
move 1 from 5 to 6
move 1 from 5 to 3
move 1 from 6 to 1
move 32 from 1 to 8
move 23 from 8 to 4
move 1 from 2 to 1
move 24 from 8 to 4
move 1 from 3 to 6
move 47 from 4 to 6
move 2 from 6 to 1
move 3 from 1 to 5
move 1 from 2 to 1
move 3 from 5 to 7
move 21 from 6 to 2
move 3 from 7 to 8
move 2 from 1 to 6
move 8 from 6 to 4
move 4 from 8 to 9
move 3 from 2 to 8
move 4 from 4 to 2
move 2 from 2 to 5
move 4 from 9 to 8
move 2 from 1 to 5
move 11 from 6 to 1
move 14 from 2 to 6
move 2 from 4 to 3
move 1 from 2 to 9
move 3 from 2 to 9
move 20 from 6 to 5
move 2 from 4 to 2
move 4 from 9 to 1
move 8 from 8 to 9
move 1 from 6 to 9
move 14 from 5 to 2
move 10 from 2 to 7
move 7 from 9 to 6
move 1 from 6 to 8
move 6 from 2 to 6
move 1 from 2 to 5
move 1 from 3 to 5
move 9 from 6 to 3
move 1 from 5 to 2
move 9 from 7 to 3
move 12 from 3 to 2
move 9 from 5 to 9
move 1 from 8 to 6
move 3 from 3 to 5
move 1 from 7 to 6
move 14 from 2 to 6
move 3 from 9 to 7
move 6 from 1 to 2
move 5 from 1 to 8
move 10 from 6 to 9
move 4 from 5 to 6
move 3 from 2 to 4
move 9 from 9 to 7
move 1 from 8 to 7
move 3 from 9 to 6
move 3 from 3 to 7
move 1 from 5 to 1
move 15 from 7 to 1
move 2 from 8 to 5
move 2 from 5 to 4
move 1 from 7 to 4
move 1 from 3 to 1
move 15 from 6 to 7
move 2 from 4 to 9
move 3 from 4 to 7
move 18 from 1 to 6
move 1 from 8 to 9
move 6 from 9 to 7
move 3 from 6 to 8
move 1 from 1 to 2
move 2 from 9 to 5
move 2 from 2 to 9
move 16 from 6 to 3
move 15 from 3 to 7
move 2 from 8 to 4
move 1 from 3 to 7
move 3 from 4 to 9
move 2 from 1 to 9
move 26 from 7 to 4
move 1 from 2 to 1
move 7 from 9 to 8
move 1 from 2 to 5
move 2 from 5 to 2
move 8 from 7 to 5
move 1 from 7 to 3
move 1 from 3 to 9
move 2 from 2 to 7
move 1 from 6 to 4
move 4 from 8 to 9
move 1 from 1 to 3
move 1 from 5 to 6
move 2 from 5 to 7
move 17 from 4 to 9
move 6 from 4 to 9
move 1 from 3 to 4
move 6 from 7 to 9
move 3 from 5 to 6
move 2 from 7 to 9
move 4 from 8 to 9
move 4 from 6 to 4
move 8 from 4 to 6
move 1 from 8 to 4
move 3 from 5 to 2
move 2 from 4 to 3
move 1 from 7 to 9
move 2 from 3 to 5
move 4 from 6 to 9
move 1 from 6 to 1
move 36 from 9 to 4
move 2 from 5 to 3
move 3 from 2 to 1
move 3 from 1 to 4
move 14 from 4 to 1
move 1 from 8 to 5
move 4 from 1 to 3
move 5 from 9 to 5
move 2 from 5 to 8
move 1 from 8 to 9
move 4 from 9 to 6
move 3 from 5 to 8
move 1 from 5 to 6
move 2 from 1 to 6
move 2 from 9 to 7
move 6 from 6 to 4
move 1 from 1 to 3
move 29 from 4 to 6
move 7 from 3 to 4
move 1 from 8 to 9
move 3 from 1 to 6
move 4 from 1 to 4
move 1 from 8 to 4
move 4 from 4 to 3
move 15 from 6 to 8
move 9 from 4 to 9
move 1 from 7 to 9
move 8 from 8 to 3
move 3 from 6 to 7
move 1 from 1 to 2
move 4 from 7 to 6
move 7 from 8 to 5
move 1 from 8 to 4
move 2 from 5 to 7
move 1 from 2 to 4
move 5 from 6 to 1
move 4 from 3 to 2
"""
instructions = [inst for inst in INSTRUCTIONS.split("\n") if inst.strip()]

# to solve this challenge I need to be able to:
# - read the stacks
# - create the stacks
# - perform an instruction (and loop over instructions)
# - read the word made up of the letters at the top of the stacks

# I'm gonna create a list of lists of strings.
# Noticing that there can be, in the edge case, at most 56 crates on one stack (when all crates pile up on the same stack),
# I'll create a list of 56 lists of strings, each list representing a stack of crates.

# constants
EXTRACT_CRATE_CONTENT_PAT = re.compile(
    "\[(.)\]"
)  # in prod that'd go to a constants.py file
INSTRUCTION_NB_PAT = re.compile("\d+")

# helper functions
def create_stack_from_string_stack(
    string_stack: str, verbose: bool = False
) -> list[list[str]]:
    """Creates the stacks of crates, a mutable object that I'll perform the instructions on"""
    # clean up and preprocess the input
    stacks = [row for row in string_stack.split("\n")[:-1] if row.strip()]
    assert all(
        len(row) == len(stacks[0]) for row in stacks
    ), "The stacks are not all the same length"
    # make the output stacks
    output_stacks = []
    # recrate all the [ and ] even when crate is empty
    for row in stacks:
        new_row = ""
        for i in range(len(row)):
            new_row += "[" if i % 4 == 0 else ("]" if i % 2 == 0 else row[i])
        output_stacks.append(new_row)
    output_stacks = [EXTRACT_CRATE_CONTENT_PAT.findall(row) for row in output_stacks]
    # last step: allow some room at the top
    nb_crates = sum(
        sum(1 if elem.strip() else 0 for elem in row) for row in output_stacks
    )
    nb_empty_rows_to_add = max(0, nb_crates - len(output_stacks))
    for i in range(nb_empty_rows_to_add):
        output_stacks.insert(0, [" "] * len(output_stacks[0]))
    if verbose:
        for row in output_stacks:
            print(*row)
        print(output_stacks)
    return output_stacks


def perform_instruction(stacks: list, inst: str, reverse: bool = True) -> None:
    """Moves the crates according to `inst`

    Args:
        stacks (list): the current state of the stacks
        inst (str): the instruction (must be like 'move 1 from 4 to 1')
        reverse (bool): optional. Defines whether to reverse the order of the crates (one crate at a time, as in part 1) or not (several crates at a time, in part 2)
    """

    nb_crates, start_stack_ind, end_stack_ind = map(
        int, INSTRUCTION_NB_PAT.findall(inst)
    )
    start_stack_ind -= 1  # because they are 1-indexed in the text
    end_stack_ind -= 1  # because they are 1-indexed in the text
    if nb_crates:
        start_stack = []
        for i in range(len(stacks)):
            if (crate := stacks[i][start_stack_ind]).strip():
                start_stack.append(crate)  # collect the crates
                stacks[i][
                    start_stack_ind
                ] = " "  # replace with void in the 'from' stack
            if len(start_stack) == nb_crates:
                break
        if reverse:
            start_stack = start_stack[::-1]  # invert order of crates as it is LIFO
        # find the index of the top crate in the 'to' stack
        for i in range(len(stacks)):
            if stacks[i][end_stack_ind].strip():
                break
        for ind in range(i - nb_crates, i):
            stacks[ind][end_stack_ind] = start_stack[ind - (i - nb_crates)]


def read_top_crates(stacks: list) -> str:
    """Reads the message given by the crates at the top of each stack

    Args:
        stacks (list): the state of the crates in the stacks

    Returns:
        str: the message
    """
    message = ""
    for i in range(len(stacks[0])):
        letter = " "
        current_stack = (
            stacks[j][i] for j in range(len(stacks))
        )  # the column 0-indexed i
        while not letter.strip():
            letter = next(current_stack)
        message += letter
    print(message)
    return message


# main code
stacks = create_stack_from_string_stack(STACKS)
for inst in instructions:
    perform_instruction(stacks, inst)
read_top_crates(stacks)

# part 2
# now the crates retain their initial order, unlike in part 1
# I'll need a very minor change to my code
stacks = create_stack_from_string_stack(STACKS)
for inst in instructions:
    perform_instruction(stacks, inst, reverse=False)
read_top_crates(stacks)
