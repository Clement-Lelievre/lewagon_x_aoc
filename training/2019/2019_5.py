from tqdm import tqdm
from typing import Generator
from functools import reduce

INPUT = """3,225,1,225,6,6,1100,1,238,225,104,0,1101,91,67,225,1102,67,36,225,1102,21,90,225,2,13,48,224,101,-819,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,62,9,225,1,139,22,224,101,-166,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,102,41,195,224,101,-2870,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1101,46,60,224,101,-106,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1001,191,32,224,101,-87,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,76,90,225,1101,15,58,225,1102,45,42,224,101,-1890,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,101,62,143,224,101,-77,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,55,54,225,1102,70,58,225,1002,17,80,224,101,-5360,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,344,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,359,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,108,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,419,101,1,223,223,1008,226,677,224,102,2,223,223,1006,224,434,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,449,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,509,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,539,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,554,101,1,223,223,1007,677,226,224,1002,223,2,223,1005,224,569,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,584,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,614,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,659,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226"""
# INPUT='1002,4,3,4,33'

inp = list(map(int, INPUT.replace("\n", "").split(",")))
# utilities


def get_instructions(input_: list[int]) -> Generator[list[int], None, None]:
    cursor = 0
    while cursor < len(input_):
        if input_[cursor] in (3, 4):
            yield input_[cursor : cursor + 2]
            cursor += 2
        else:
            yield input_[cursor : cursor + 4]
            cursor += 4


multiplication = lambda iterable_: reduce(lambda x, y, base=1: x * y * base, iterable_)

# main code
def process_instruction(instr: list[int], current_input: int) -> int | None:
    full_opcode, ind1, *rest = instr
    opcode = int((s := str(full_opcode))[-2:])
    nb_params = len(s) - 2
    params = "0" * (3 - nb_params) + s[:-2]
    params = list(map(int, params[::-1]))
    if opcode in (1, 2):
        inp[rest[1]] = (sum if opcode == 1 else multiplication)(
            [ind1 if params[0] else inp[ind1], rest[0] if params[1] else inp[rest[0]]]
        )
    elif opcode == 3:
        inp[ind1] = inp[current_input] if params[0] == 0 else current_input
        # takes a single integer as input and saves it to the position given by its only parameter
    elif opcode == 4:
        print(f"output: {inp[ind1] if params[0] == 0 else ind1}")
        # outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.


# instructions = get_instructions(inp.copy())
# TEST_ID = 1
# current_input = TEST_ID

# for instr in instructions:
#     print(instr)
#     try:
#         current_input = process_instruction(instr, TEST_ID)
#         if current_input is not None:
#             print(current_input)
#             break
#     except IndexError:
#         break

# part 2

# main code
def process_instruction_part2(instr: list[int], current_input: int) -> int | None:
    full_opcode, ind1, *rest = instr
    opcode = int((s := str(full_opcode))[-2:])
    nb_params = len(s) - 2
    params = "0" * (3 - nb_params) + s[:-2]
    params = list(map(int, params[::-1]))
    if opcode in (1, 2):
        inp[rest[1]] = (sum if opcode == 1 else multiplication)(
            [ind1 if params[0] else inp[ind1], rest[0] if params[1] else inp[rest[0]]]
        )
    elif opcode == 3:
        inp[ind1] = inp[current_input] if params[0] == 0 else current_input
        # takes a single integer as input and saves it to the position given by its only parameter
    elif opcode == 4:
        print(f"output: {inp[ind1] if params[0] == 0 else ind1}")
        # outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
    elif opcode == 5:
        # if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter.
        # Otherwise, it does nothing.
        if ind1 if params[0] else inp[ind1]:
            return rest[0] if params[1] else inp[rest[0]]
    elif opcode == 6:
        # if the first parameter is zero, it sets the instruction pointer to the value from the second parameter.
        # Otherwise, it does nothing.
        if not (ind1 if params[0] else inp[ind1]):
            return rest[0] if params[1] else inp[rest[0]]
    elif opcode == 7:
        # if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
        # Otherwise, it stores 0.
        if (ind1 if params[0] else inp[ind1]) < rest[0] if params[1] else inp[rest[0]]:
            inp[rest[1]] == 1
    elif opcode == 8:
        # if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
        # Otherwise, it stores 0.
        if (ind1 if params[0] else inp[ind1]) == rest[0] if params[1] else inp[rest[0]]:
            inp[rest[1]] == 1


TEST_ID = 5
cursor = 0
while True:
    instr = inp[cursor : (auto_cursor := cursor + (2 if inp[cursor] in (3, 4) else 4))]
    try:
        new_cursor = process_instruction_part2(instr, TEST_ID)
        cursor = new_cursor if new_cursor is not None else auto_cursor
    except IndexError:
        break
