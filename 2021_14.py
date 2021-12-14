TEMPLATE = "FNFPPNKPPHSOKFFHOFOC"
INPUT = """VS -> B
SV -> C
PP -> N
NS -> N
BC -> N
PB -> F
BK -> P
NV -> V
KF -> C
KS -> C
PV -> N
NF -> S
PK -> F
SC -> F
KN -> K
PN -> K
OH -> F
PS -> P
FN -> O
OP -> B
FO -> C
HS -> F
VO -> C
OS -> B
PF -> V
SB -> V
KO -> O
SK -> N
KB -> F
KH -> C
CC -> B
CS -> C
OF -> C
FS -> B
FP -> H
VN -> O
NB -> N
BS -> H
PC -> H
OO -> F
BF -> O
HC -> P
BH -> S
NP -> P
FB -> C
CB -> H
BO -> C
NN -> V
SF -> N
FC -> F
KK -> C
CN -> N
BV -> F
FK -> C
CF -> F
VV -> B
VF -> S
CK -> C
OV -> P
NC -> N
SS -> F
NK -> V
HN -> O
ON -> P
FH -> O
OB -> H
SH -> H
NH -> V
FF -> B
HP -> B
PO -> P
HB -> H
CH -> N
SN -> P
HK -> P
FV -> H
SO -> O
VH -> V
BP -> V
CV -> P
KP -> K
VB -> N
HV -> K
SP -> N
HO -> P
CP -> H
VC -> N
CO -> S
BN -> H
NO -> B
HF -> O
VP -> K
KV -> H
KC -> F
HH -> C
BB -> K
VK -> P
OK -> C
OC -> C
PH -> H
"""
from collections import defaultdict
from tqdm import tqdm

d = defaultdict(str)
for line in INPUT.splitlines():
    pair, inserted = line.split('->')
    d[pair.strip()] = inserted.strip()

def step(template: str, rules: dict) -> str:
    """performs one insertion step as described here: https://adventofcode.com/2021/day/14"""
    split = [template[i:i+2] for i in range(len(template)-1)]
    new_template = [item[0] + d[item] + item[1] for item in split]
    nt = new_template[0]
    for item in new_template[1:]:
        nt += item[1:]
    return nt

# template = TEMPLATE
# for i in tqdm(range(10)):
#     template = step(template, d)

# c = {}
# for letter in set(template):
#     c[letter] = template.count(letter)
# print(max(c.values()) - min(c.values()))

# part 2