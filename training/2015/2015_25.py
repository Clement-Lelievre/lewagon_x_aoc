from tqdm import tqdm

INPUT = "To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029."

code = 20151125


def generate_code(code: int) -> int:
    return (code * 252_533) % 33_554_393


# build the empty structure
row = [0] * (2947 + 3029)
arr = []
for i in range(2947 + 3029):
    arr.append(row.copy())


for i in tqdm(range(2947 + 3029)):  # fill up the structure
    idx_couples = [(row, i - row) for row in range(i, -1, -1)]
    for r, c in idx_couples:
        code = generate_code(code) if r != 0 or c != 0 else code
        # print((r,c), code)
        arr[r][c] = code
        # print(arr)


print(arr[2946][3028])
