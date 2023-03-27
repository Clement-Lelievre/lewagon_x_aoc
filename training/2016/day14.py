import hashlib
from string import ascii_lowercase as alphabet

INPUT = "ahsbgdzn"
nb_keys = 0
ALL_CHARS = list(alphabet) + list(map(str, range(10)))

# potentially there is a lot of repeated calcs in this challenge, so I'm gonna cache the results of each hash


def get_first_triple(seq: str) -> str | None:
    for letter in set(seq):
        if letter * 3 in seq:
            return letter


def get_quintuples(seq: str) -> list[str]:
    """Computes and returns a list of the single charcaters that are present (at least) five times in a row in `seq`

    Args:
        seq (str): the hash to check

    Returns:
        list[str]: a list of all characters present at least 5 times in a row
    """
    return [char for char in ALL_CHARS if char * 5 in seq]


hashes = {
    (hash := hashlib.md5(bytes(INPUT + str(i), "utf-8")).hexdigest()): get_first_triple(
        hash
    )
    for i in range(25_000)
}

quintuples = [get_quintuples(hash) for hash in hashes]

for ind, hash in enumerate(hashes):
    if (first_triple := hashes[hash]) is not None and any(
        first_triple in quin for quin in quintuples[ind + 1 : ind + 1 + 1_000]
    ):
        nb_keys += 1
    if nb_keys == 64:
        print(f"The first index is {ind}")
        break
else:
    print("Not found, raise the number of hashes")

# part 2
nb_keys = 0


def hash_n_times(seq: str, n: int = 2_017) -> str:
    for _ in range(n):
        seq = hashlib.md5(bytes(seq, "utf-8")).hexdigest()
    return seq


hashes = {  # this is the slow part; there may be repeated computations here that I'd rather cache using an appropriate data structure
    (hash := hash_n_times(INPUT + str(i))): get_first_triple(hash)
    for i in range(25_000)
}

quintuples = [get_quintuples(hash) for hash in hashes]

for ind, hash in enumerate(hashes):
    if (first_triple := hashes[hash]) is not None and any(
        first_triple in quin for quin in quintuples[ind + 1 : ind + 1 + 1_000]
    ):
        nb_keys += 1
    if nb_keys == 64:
        print(f"The first index is {ind}")
        break
else:
    print("Not found, raise the number of hashes")
