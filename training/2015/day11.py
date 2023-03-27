from string import ascii_lowercase

three_letters = [ascii_lowercase[i : i + 3] for i in range(len(ascii_lowercase) - 2)]
current_pwd = "cqjxjnds"


def is_valid(pwd: str) -> bool:
    # if len(pwd) != 8: # no need to check this one as it'll always be true
    #     return False
    if "i" in pwd or "o" in pwd or "l" in pwd:
        return False
    for tl in three_letters:
        if tl in pwd:
            break
    else:
        return False
    nb_double = 0
    for letter in ascii_lowercase:
        if letter * 2 in pwd:
            nb_double += 1
        if nb_double == 2:
            break
    else:
        return False
    return True


def increment(pwd: str) -> str:
    pwd = [ascii_lowercase.index(letter) for letter in pwd]
    i = 7
    while pwd[i] == 25:
        i -= 1
    pwd[i] += 1
    new_pwd = pwd[: i + 1] + [0] * (7 - i)
    new_pwd = "".join(str(ascii_lowercase[ind]) for ind in new_pwd)
    return new_pwd

# while not is_valid(current_pwd):
#     current_pwd = increment(current_pwd)

# print(current_pwd)
# answer to part 1 is: cqjxxyzz
# part 2
current_pwd='cqjxxzaa'
while not is_valid(current_pwd):
    current_pwd = increment(current_pwd)

print(current_pwd)
# cqkaabcc

# hint to get maybe better perf: use a generator to yield the values + only convert back to str when password is found