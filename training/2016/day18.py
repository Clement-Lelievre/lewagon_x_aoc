row = "^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^......."
nb_safe_tiles = row.count(".")
traps = ("^^.", ".^^", "^..", "..^")
for _ in range(39):
    padded_row = "." + row + "."
    row = "".join(
        "^" if padded_row[i - 1 : i + 2] in traps else "."
        for i in range(1, len(padded_row) - 1)
    )
    nb_safe_tiles += row.count(".")

print(f"part 1: {nb_safe_tiles}")

# part 2 # this did not any modification to my part 1 code
row = "^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^......."
nb_safe_tiles = row.count(".")
for _ in range(399_999):
    padded_row = "." + "".join(row) + "."
    row = []
    for i in range(1, len(padded_row) - 1):
        if padded_row[i - 1 : i + 2] in traps:
            row.append("^")
        else:
            row.append(".")
            nb_safe_tiles += 1

print(f"part 2: {nb_safe_tiles}")
