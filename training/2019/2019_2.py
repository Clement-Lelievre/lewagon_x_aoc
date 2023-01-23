from tqdm import tqdm

INPUT = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0"""

# Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the
# "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program,
# replace position 1 with the value 12 and replace position 2 with the value 2.

INPUT = """1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0"""

# What value is left at position 0 after the program halts?

inp = [int(x) for x in INPUT.split(",")]
instructions = [inp.copy()[i : i + 4] for i in range(0, len(inp), 4)]


def process_instruction(instr: list[int]):
    opcode, ind1, ind2, ind3 = instr
    if opcode == 1:
        inp[ind3] = inp[ind1] + inp[ind2]
    elif opcode == 2:
        inp[ind3] = inp[ind1] * inp[ind2]
    else:
        return -1


for instr in instructions:
    if process_instruction(instr) == -1:
        break
# print(INPUT, instructions,inp, sep='\n')
print(inp[0])

# part 2
# for noun in tqdm(range(100)):
#     for verb in range(100):
#         INPUT = f"""1,{noun},{verb},3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0"""
#         inp = [int(x) for x in INPUT.split(",")]
#         instructions = [inp.copy()[i:i+4] for i in range(0, len(inp), 4)]

#         for instr in instructions:
#             if process_instruction(instr) == -1:
#                 break
#         if inp[0] == 19690720:
#             print(noun, verb, 100 * noun + verb)
#             break
