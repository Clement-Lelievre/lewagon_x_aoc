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
from collections import defaultdict, Counter
from tqdm import tqdm   

d = defaultdict(str)
for line in INPUT.splitlines():
    pair, inserted = line.split(' -> ')
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

# part 2 (kudos to Flo Reichel)

# Find count of AB pairs in initial string
first_element = 'F'
c = Counter()
for idx in range(len(TEMPLATE[:-1])):
    c[TEMPLATE[idx:idx+2]] += 1

# Loop steps
for i in range(40):
    # Copy and re-initialise counter
    cc = c
    c = Counter()
    for el in cc.keys():
        # Increment counter for AX and XB
        c[el[0] + d[el]] += cc[el]
        c[d[el] + el[1]] += cc[el]

# Now count the actual elements
l = Counter()
# Add back the very first element, since the loop below will only consider the second half of each pair
l[first_element] = 1
for el, ct in c.items():
    l[el[1]] += ct

print(l.most_common()[0][1] - l.most_common()[-1][1])