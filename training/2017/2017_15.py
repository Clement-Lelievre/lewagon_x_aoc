from tqdm import tqdm

START_A = 783
START_B = 325
FACTOR_A = 16_807
FACTOR_B = 48_271
MOD = 2_147_483_647

def gen_a(current_val: int) -> int:
    return current_val * FACTOR_A % MOD


def gen_b(current_val: int) -> int:
    return current_val * FACTOR_B % MOD


matches = 0
val_a = START_A
val_b = START_B
for _ in tqdm(range(40_000_000)):
    val_a = gen_a(val_a)
    val_b = gen_b(val_b)
    if val_a % 2**16 == val_b % 2**16:
      # the key was to understand that truncating the binary representation to the lowest 16 digits
        # is equivalent to taking the modulo 2**16
        matches += 1

print(matches)

# part 2
val_a = START_A
val_b = START_B
for_the_judge_a = []
for_the_judge_b = []

while min(len(for_the_judge_a), len(for_the_judge_b)) < 5_000_000:
    val_a = gen_a(val_a)
    val_b = gen_b(val_b)
    if val_a % 4 == 0:
        for_the_judge_a.append(val_a % 2**16)
    if val_b % 8 == 0:
        for_the_judge_b.append(val_b % 2**16)


print(sum(a == b for a, b in zip(for_the_judge_a, for_the_judge_b)))
