DISK_LENGTH = 272
state = "00111101111101000"


def get_checksum(disk_length: int, state: str) -> str:
    # getting the full-length state
    while len(state) < disk_length:
        a = state
        b = state[::-1]
        temp = ""
        for char in b:
            temp += "1" if char == "0" else "0"
        b = temp
        state = "0".join([a, b])

    state = state[:disk_length]
    checksum = state
    # getting the checksum
    while len(checksum) % 2 == 0:
        temp = ""
        for i in range(0, len(checksum), 2):
            temp += "1" if checksum[i : i + 2] in ("11", "00") else "0"
        checksum = temp

    return checksum


print(get_checksum(DISK_LENGTH, state))

# part 2
# no change required, it takes longer but still works in a decent time
DISK_LENGTH = 35651584
print(get_checksum(DISK_LENGTH, state))
