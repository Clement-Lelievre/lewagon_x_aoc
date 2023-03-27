inp = 36000000

# The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
# The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
# Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15,


# nb_tried = 1_000_000 # kinda arbitrarily chosen...
# street_state = [0]*nb_tried
# for elf_nb in range(1,  nb_tried+1): # elves
#     for i in range(elf_nb-1, nb_tried, elf_nb): # houses
#         street_state[i] += 10*elf_nb

# # What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?
# for idx, house in enumerate(street_state):
#     if house >= inp:
#         print(idx+1)
#         break

# part 2
nb_tried = 1_000_000  # kinda arbitrarily chosen...
street_state = [0] * nb_tried
for elf_nb in range(1, nb_tried + 1):  # elves
    for i in list(range(elf_nb - 1, nb_tried, elf_nb))[:50]:  # houses
        street_state[i] += 11 * elf_nb

# What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?
for idx, house in enumerate(street_state):
    if house >= inp:
        print(idx + 1)
        break
