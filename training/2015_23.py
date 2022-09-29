import re

INPUT = """jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
"""


a, b, i = 0, 0, 0


instructions = [r for row in INPUT.splitlines() if (r := row.replace("\n", ""))]
tpl = lambda x: 3 * x
inc = lambda x: x + 1
hlf = lambda x: x // 2
l = len(instructions)
jump_pat = re.compile(r"((-)?\d+)")

while True:
    inst = instructions[i]
    if "hlf" in inst:
        if inst[-1] == "a":
            a = hlf(a)
        else:
            b = hlf(b)
        if i + 1 < l:
            i += 1
        else:
            break
    elif "inc" in inst:
        if inst[-1] == "a":
            a = inc(a)
        else:
            b = inc(b)
        if i + 1 < l:
            i += 1
        else:
            break
    elif "tpl" in inst:
        if inst[-1] == "a":
            a = tpl(a)
        else:
            b = tpl(b)
        if i + 1 < l:
            i += 1
        else:
            break
    elif "jmp" in inst:
        jump_amount = int(jump_pat.search(inst).group())
        if (new_idx := i + jump_amount) in range(l):
            i = new_idx
        else:
            break
    elif "jie" in inst:
        tank = a if inst.split()[1][0] == "a" else b
        if tank % 2 == 0:
            jump_amount = int(jump_pat.search(inst).group())
            if (new_idx := i + jump_amount) in range(l):
                i = new_idx
            else:
                break
        else:
            i += 1
    else:
        tank = a if inst.split()[1][0] == "a" else b
        if tank == 1:
            jump_amount = int(jump_pat.search(inst).group())
            if (new_idx := i + jump_amount) in range(l):
                i = new_idx
            else:
                break
        else:
            i += 1

print(a, b)

# part 2
a, b, i = 1, 0, 0


instructions = [r for row in INPUT.splitlines() if (r := row.replace("\n", ""))]
tpl = lambda x: 3 * x
inc = lambda x: x + 1
hlf = lambda x: x // 2
l = len(instructions)
jump_pat = re.compile(r"((-)?\d+)")

while True:
    inst = instructions[i]
    if "hlf" in inst:
        if inst[-1] == "a":
            a = hlf(a)
        else:
            b = hlf(b)
        if i + 1 < l:
            i += 1
        else:
            break
    elif "inc" in inst:
        if inst[-1] == "a":
            a = inc(a)
        else:
            b = inc(b)
        if i + 1 < l:
            i += 1
        else:
            break
    elif "tpl" in inst:
        if inst[-1] == "a":
            a = tpl(a)
        else:
            b = tpl(b)
        if i + 1 < l:
            i += 1
        else:
            break
    elif "jmp" in inst:
        jump_amount = int(jump_pat.search(inst).group())
        if (new_idx := i + jump_amount) in range(l):
            i = new_idx
        else:
            break
    elif "jie" in inst:
        tank = a if inst.split()[1][0] == "a" else b
        if tank % 2 == 0:
            jump_amount = int(jump_pat.search(inst).group())
            if (new_idx := i + jump_amount) in range(l):
                i = new_idx
            else:
                break
        else:
            i += 1
    else:
        tank = a if inst.split()[1][0] == "a" else b
        if tank == 1:
            jump_amount = int(jump_pat.search(inst).group())
            if (new_idx := i + jump_amount) in range(l):
                i = new_idx
            else:
                break
        else:
            i += 1

print(a, b)