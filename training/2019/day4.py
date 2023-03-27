INPUT = '152085-670283'

#     It is a six-digit number.
#     The value is within the range given in your puzzle input.
#     Two adjacent digits are the same (like 22 in 122345).
#     Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# How many different passwords within the range given in your puzzle input meet these criteria?

# output = 0
# for nb in range(152085, 670284):
#     nb = str(nb)
#     if any(nb[i] == nb[i+1] for i in range(len(nb)-1)) and all(nb[i] <= nb[i+1] for i in range(len(nb)-1)):
#         output += 1
# print(output)

# part 2
# the two adjacent matching digits are not part of a larger group of matching digits.
def exactly_two_consecutive_digits(nb:str):
    for i in range(len(nb)-1):
        if nb[i] == nb[i+1]:
            if i == 0:
                if nb[i] != nb[i+2]:
                    return True
            elif i == 4:
                if nb[i] != nb[i-1]:
                    return True
            else:
                if nb[i] != nb[i-1] and nb[i] != nb[i+2]:
                    return True
    return False

output = 0
for nb in map(str, range(152085, 670284)):
    if all(nb[i] <= nb[i+1] for i in range(6-1)) and exactly_two_consecutive_digits(nb):
        output += 1

print(output) 

