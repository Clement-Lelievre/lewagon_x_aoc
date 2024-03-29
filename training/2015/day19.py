import re
from collections import deque
from typing import Generator

REPLACEMENTS = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg"""

MOLECULE = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

possible_molecules = set()
pat = re.compile(r"(\w+)\s=>\s(\w+)")
for mol in REPLACEMENTS.splitlines():
    before, after = (res := pat.search(mol)).group(1), res.group(2)
    for e in re.finditer(before, MOLECULE):
        span = e.span()
        possible_molecules.add(MOLECULE[: span[0]] + after + MOLECULE[span[1] :])

print("part 1:", len(possible_molecules))

# part 2
# I feel like starting from the end, i.e. from my input molecule. I feel there'll be less explosive combinatorics
def transform_mol(mol: str) -> Generator[str, str, str]:
    """Shrinks `mol` by returning all neighbours after exactly one possible transformation

    Args:
        mol (str): the molecule currently under consideration

    Returns:
        set: the set of neighbours of this molecule
    """
    neighbours = set()
    for after, before in replacements.items():
        for e in re.finditer(after, mol):
            span = e.span()
            neighbours.add("".join((mol[: span[0]], before, mol[span[1] :])))
    for neigh in neighbours:
        yield neigh


# recursive functino below (DFS?) solves instantly
def backtrack(
    current_mol: str = MOLECULE, nb_steps: int = 0, target_mol: str = "e"
) -> None:
    global found
    if found:
        return
    if current_mol == target_mol:
        found = True
        print(f"part 2: {nb_steps=}")
        return
    visited.add(current_mol)
    for neigh in transform_mol(current_mol):
        if neigh not in visited:
            backtrack(neigh, nb_steps + 1)
    return


replacements = {
    (res := pat.search(mol)).group(2): res.group(1) for mol in REPLACEMENTS.splitlines()
}  # reverse the order given in the text
visited = set()
found = False
backtrack()

# wile loop below (BFS?) is way too slow
queue = (
    deque()
)  # provides O(1) insertion and removal whereas a Python list is O(n) when it comes to removing an item from the front
nb_steps = 0
queue.append((MOLECULE, nb_steps))
visited = set()
while queue:
    current_mol, nb_steps = queue.popleft()
    if current_mol == "e":
        print(nb_steps)
        break
    visited.add(current_mol)
    for neigh in transform_mol(current_mol):
        if neigh not in visited:
            queue.append((neigh, nb_steps + 1))
else:
    raise ValueError("Not found")
