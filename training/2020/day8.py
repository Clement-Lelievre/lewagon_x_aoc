import re
from tqdm import tqdm

INPUT = '''acc -7
acc +6
acc +4
nop +191
jmp +199
acc +44
acc -9
jmp +505
acc -12
acc +45
jmp +204
jmp +129
acc +17
nop +287
jmp +584
acc +16
jmp +363
acc +4
nop +142
acc +34
nop +345
jmp +522
jmp +53
acc -10
jmp +524
jmp +492
jmp +319
acc -9
jmp +550
acc -19
jmp +15
acc +24
jmp +30
acc -19
acc +12
acc -2
jmp +274
nop +91
acc +10
acc +4
jmp +501
acc +49
acc +29
jmp +488
jmp +504
jmp +277
acc +20
acc +34
jmp -40
acc +10
acc -4
acc -19
acc +38
jmp +239
acc -16
acc -3
nop +513
jmp +526
jmp +131
nop +539
acc -11
jmp +470
acc +30
jmp +166
acc +17
acc -16
nop +315
jmp +364
acc +15
nop -61
acc -12
nop +147
jmp -31
acc -9
jmp +324
acc +0
jmp +1
jmp +321
acc +0
acc +6
acc -17
acc +13
jmp +461
jmp +184
acc +22
jmp +182
jmp +504
nop +131
acc +12
acc -6
acc +29
jmp +187
acc +17
jmp +67
jmp -2
acc +50
acc +17
jmp +442
acc +8
nop +146
acc -12
acc +32
jmp +237
jmp +1
acc +34
acc +1
acc +18
jmp +274
acc +17
acc -12
jmp +282
acc +49
acc +11
acc +28
acc +40
jmp +79
acc +19
acc -8
nop +87
jmp +347
acc +48
nop +189
jmp +419
acc +31
jmp +1
acc +31
jmp +1
jmp -94
nop -45
nop +412
acc -14
acc +35
jmp -49
jmp +177
jmp +127
jmp +360
jmp +114
acc -11
nop +248
jmp -64
acc +31
acc +23
acc +4
nop +110
jmp +61
acc +45
nop +444
jmp +218
jmp -131
acc +36
jmp -142
nop +361
acc -3
acc +6
jmp +161
acc +24
acc -7
acc +4
acc +31
jmp +91
jmp -20
jmp +1
nop -11
jmp -146
acc +25
acc +33
jmp +52
acc -7
jmp +82
acc +7
acc +21
acc +6
jmp +397
acc +12
acc +5
acc -9
acc +24
jmp +371
acc +50
acc +47
acc +19
jmp +238
jmp +396
acc -16
nop +394
jmp +180
acc +1
acc +40
jmp +237
acc +22
nop -30
jmp -129
acc +22
jmp +232
acc +23
acc +27
acc +47
jmp +133
acc +0
nop +30
acc +11
acc -9
jmp +381
jmp +75
jmp -64
acc -15
acc +29
acc +49
jmp +195
nop +113
acc -16
nop +312
acc +6
jmp -44
acc +26
acc +40
jmp +272
jmp +83
jmp +365
acc +24
acc +4
jmp +29
acc +8
jmp -137
acc +13
jmp +1
acc +33
nop -182
jmp +22
jmp +9
nop +20
acc +14
nop +291
jmp -28
jmp -83
acc +18
acc +5
jmp +32
acc +48
nop -128
acc +28
jmp +225
acc +29
nop +280
jmp +304
acc +37
acc +50
acc +30
jmp +131
jmp -60
acc +27
jmp +272
jmp +358
acc -1
acc +37
jmp +203
acc +1
acc +37
acc +12
acc -16
jmp +263
acc -16
acc +30
jmp +86
acc +26
acc +6
jmp +344
jmp -147
jmp -185
acc -5
acc -3
acc +7
acc +9
jmp -205
nop -85
acc -4
acc -1
jmp +266
acc +19
nop -143
acc -3
jmp -12
acc +12
acc -18
jmp +326
acc +39
jmp +165
nop -279
acc +19
acc +46
acc +5
jmp -163
acc -13
jmp +1
acc +33
acc +44
jmp -62
acc -10
acc +7
jmp +240
acc -19
jmp -190
acc -12
jmp -167
acc -2
nop -288
acc -13
jmp +303
acc +24
jmp -283
jmp +309
nop +190
acc +38
acc -12
jmp -47
acc +15
acc +31
jmp -259
nop +154
acc +25
acc +8
jmp -295
acc +37
acc +34
acc -18
acc +41
jmp +156
acc +17
acc +37
jmp -243
nop -318
acc +45
acc +33
jmp +139
acc -6
acc +34
acc +25
acc +3
jmp +260
jmp +1
acc +24
jmp +154
acc +34
acc -19
jmp +211
acc +28
jmp +98
acc +45
jmp -143
acc +41
acc +8
acc +33
nop +217
jmp +119
acc +21
jmp -150
acc +25
acc +19
jmp +1
acc +20
jmp +209
acc +43
acc +18
acc +2
jmp -159
acc +25
acc +20
acc -4
acc +45
jmp +89
nop +33
acc +27
jmp +190
acc +47
acc +36
jmp +180
acc +3
jmp +1
jmp -349
jmp -6
jmp -244
acc +2
acc +42
jmp -357
acc +3
jmp -377
acc +31
nop -292
acc +6
acc +9
jmp -212
jmp -91
acc +11
jmp +119
acc -18
acc +38
acc +31
jmp -261
jmp +1
acc +2
jmp -197
acc +0
jmp +1
acc +40
acc +31
acc +4
acc +45
jmp -68
acc -17
acc +8
nop -384
jmp -193
acc +22
nop +170
acc -19
acc +34
jmp -321
acc +46
jmp +130
acc -19
jmp +115
acc -12
acc +23
acc +16
jmp -94
acc +11
nop -286
jmp -276
acc +36
acc +25
jmp -32
acc +6
acc +39
jmp +171
acc -5
nop -131
jmp -368
acc +41
acc -7
nop -336
jmp -428
acc +21
acc +45
jmp -225
acc -2
acc +14
acc +29
jmp -439
acc +36
acc +26
jmp -433
acc +29
acc +36
acc +31
jmp -232
nop -210
nop -44
jmp -382
nop -119
acc +43
jmp +1
jmp -24
acc -13
acc +22
acc +16
jmp +90
nop -443
acc +23
acc +15
acc -3
jmp -225
jmp -448
acc +21
acc -19
acc +23
jmp +1
jmp -447
acc +36
acc -1
acc +31
nop +8
jmp +97
jmp -96
acc -16
acc +7
acc -2
jmp +1
jmp -237
jmp +1
acc -12
acc +29
acc -1
jmp -188
acc +8
jmp -453
nop -234
acc +46
acc +20
acc +24
jmp -68
jmp -178
acc +42
jmp -469
acc +19
acc +35
jmp -4
acc +49
jmp +65
nop +15
nop -209
acc +27
jmp -261
acc +15
jmp -344
acc +13
acc +43
jmp -194
jmp +1
jmp -335
nop -424
acc -13
nop -387
jmp -333
acc +33
acc +30
jmp -272
acc +16
acc +5
acc +21
acc +41
jmp -312
acc +50
jmp -429
nop +57
jmp -212
acc +7
acc -13
jmp -252
jmp -277
jmp -114
jmp -528
jmp -40
jmp -275
acc +27
nop -322
jmp -356
acc -11
jmp -96
nop -9
acc -15
jmp -194
acc +9
acc +47
acc +44
jmp -459
acc -2
acc -12
nop -354
jmp -166
acc +44
acc +23
jmp -503
acc +47
acc +39
acc +10
acc +14
jmp -543
acc +43
jmp -25
jmp -52
acc -19
jmp -423
acc +35
acc +22
acc +10
acc +16
jmp -527
jmp -482
acc +2
acc +21
acc -17
jmp -417
jmp -282
acc +16
nop -424
nop -527
jmp -207
acc +23
acc +21
jmp -503
acc +17
acc -14
jmp -189
acc +43
acc +14
acc +11
nop -427
jmp -54
acc +8
nop -37
nop -542
jmp -332
acc +27
jmp +7
jmp -98
acc +50
acc +0
acc +48
acc +0
jmp -517
acc +15
acc +10
jmp -478
jmp -141
acc +0
acc +18
jmp -468
acc +49
jmp -112
nop -536
acc -14
acc -13
acc +34
jmp +1
'''

visited_idx = [0]
acc = 0
pat = re.compile(r'(.\d+)$')
instructions = INPUT.splitlines()
i = 0
while len(set(visited_idx)) == len(visited_idx):
    if (inst := instructions[i]).startswith('acc'):  
        visited_idx.append(i+1)
        acc += int(pat.search(inst).group())
        i += 1
    elif inst.startswith('nop'):
        visited_idx.append(i+1)
        i += 1
    else:
        visited_idx.append((new_idx := int(pat.search(inst).group()) + i ))
        i = new_idx
        
print(acc)

# part 2
# looking at the tail of the instructions file, targeting any instruction from 'nop -536' till the last one would 
# have the program run properly

# i = 0
# acc = 0
# while True:
#     if (inst := instructions[i]).startswith('acc'):  
#         i += 1
#     elif inst.startswith('nop'):
#         if i + int(pat.search(inst).group()) in range(len(instructions)-5, len(instructions)):
#             print(i, inst)
#             break
#         i += 1
#     else:   
#         i = int(pat.search(inst).group())
        
# print(acc)

# the above approach didn't work, implying I cannot jump to the end of the instructions file by changing a 'nop' into a 'jmp'
# so legt's try the reverse: changing a 'jmp' into 'nop'. First let us get all the 'jmp's

visited_idx = [0]
acc = 0
pat = re.compile(r'(.\d+)$')
instructions = INPUT.splitlines()
jumps = set()
i = 0
while len(set(visited_idx)) == len(visited_idx):
    if (inst := instructions[i]).startswith('acc'):  
        visited_idx.append(i+1)
        acc += int(pat.search(inst).group())
        i += 1
    elif inst.startswith('nop'):
        visited_idx.append(i+1)
        i += 1
    else:
        jumps.add(i)
        visited_idx.append((new_idx := int(pat.search(inst).group()) + i ))
        i = new_idx
        
print(f'{jumps=}')

# now that we have the indices of the 'jmp's we met, let us iterate over each, changing each 'jmp' into a 'nop'
found = False
jump_idx = 0
jumps = list(jumps)
while not found:
    jump = jumps[jump_idx]
    new_inst = instructions.copy()
    new_inst[jump] = new_inst[jump].replace('jmp', 'nop')
    visited_idx = [0]
    acc = 0
    i = 0
    while len(set(visited_idx)) == len(visited_idx):
        if (inst := new_inst[i]).startswith('acc'):  
            visited_idx.append(i+1)
            acc += int(pat.search(inst).group())
            i += 1
        elif inst.startswith('nop'):
            visited_idx.append(i+1)
            i += 1
        else:
            visited_idx.append((new_idx := int(pat.search(inst).group()) + i ))
            i = new_idx
        if i == len(new_inst):
            print(acc)
            found = True
            break
    jump_idx += 1
        