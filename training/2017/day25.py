from tqdm import tqdm

INPUT = """Begin in state A.
Perform a diagnostic checksum after 12399302 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.

In state B:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state D.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state D.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state F.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state B.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
"""

instructions = {
    "F": {0: [1, 1, "A"], 1: [1, 1, "E"]},
    "E": {0: [1, 1, "F"], 1: [1, -1, "B"]},
    "D": {0: [1, -1, "E"], 1: [0, -1, "D"]},
    "C": {0: [1, 1, "D"], 1: [1, 1, "A"]},
    "B": {0: [0, -1, "A"], 1: [0, 1, "D"]},
    "A": {0: [1, 1, "B"], 1: [0, 1, "C"]},
}
tape = [0]
cursor_idx = 0
state = "A"

for _ in tqdm(range(12_399_302)):
    instr = instructions[state][tape[cursor_idx]]
    tape[cursor_idx] = instr[0]
    m = instr[1]
    if cursor_idx == len(tape) - 1 and m == 1:
        tape.append(0)
    elif cursor_idx == 0 and m == -1:
        tape.insert(0, 0)
        # do not change cursor index as it is already 0
    cursor_idx += m if cursor_idx or m == 1 else 0
    state = instr[2]
    # print(len(tape), cursor_idx)

print(sum(tape))

# part 2 : I cannot yet acces it as it requires all 49 stars for that year
