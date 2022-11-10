INPUT = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 14 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5
"""

instructions = [inst.replace("\n", "") for inst in INPUT.splitlines() if inst]
# registers = {letter:0 for letter in ('a','b','c','d')}
# i = 0
# while 0 <= i < len(instructions):
#     cmd = instructions[i]
#     parts = cmd.split()
#     if cmd.startswith('d'):
#         registers[parts[-1]] -= 1
#         i += 1
#     elif cmd.startswith('i'):
#         registers[parts[-1]] += 1
#         i += 1
#     elif cmd.startswith('c'):
#         registers[parts[-1]] = registers[parts[-2]] if parts[-2] in registers else int(parts[-2])
#         i += 1
#     elif cmd.startswith('j'):
#         if parts[1] in registers: # it's a register
#             i += int(parts[-1]) if registers[parts[1]] else 1
#         else: # it's a number
#             i += int(parts[-1]) if int(parts[1]) else 1


# print(registers['a'])

# part 2
registers = {letter: 0 for letter in ("a", "b", "c", "d")}
registers["c"] = 1
i = 0
while 0 <= i < len(instructions):
    cmd = instructions[i]
    parts = cmd.split()
    if cmd.startswith("d"):
        registers[parts[-1]] -= 1
        i += 1
    elif cmd.startswith("i"):
        registers[parts[-1]] += 1
        i += 1
    elif cmd.startswith("c"):
        registers[parts[-1]] = (
            registers[parts[-2]] if parts[-2] in registers else int(parts[-2])
        )
        i += 1
    elif cmd.startswith("j"):
        if parts[1] in registers:  # it's a register
            i += int(parts[-1]) if registers[parts[1]] else 1
        else:  # it's a number
            i += int(parts[-1]) if int(parts[1]) else 1


print(registers["a"])
