# this is the famous Josephus problem: https://brilliant.org/wiki/josephus-problem/
# hence the challenge name

nb_elves = 3_014_387
# find the power of two right below my input number
i = 1
power_ = 0
while i < nb_elves:
    i *= 2
    power_ += 1

power_ -= 1
# kill the right number of elves such that a power of 2 remains
remaining = nb_elves - i // 2 # // is for nicer display
print(f"part 1: {remaining*2+1}")

# part 2
# this time I'm going to simulate the whole process
for nb_elves in range(2,17):
    table = list(range(1, nb_elves+1))
    current_elf_ind = 0
    while len(table) > 1:
        #print(f'speaking: {table[current_elf_ind]}')
        # locate number of the elf across the table
        elf_stolen_from_ind = (current_elf_ind + (nb_remaining := len(table)) // 2) % nb_remaining
        #print(f'{elf_stolen_from_ind=}')
        # discard him
        table.remove(table[elf_stolen_from_ind])
        #print(table)
        current_elf_ind = (current_elf_ind + 1 ) % nb_remaining if current_elf_ind != nb_remaining - 1 else 0
        
    print(f'{nb_elves=}: {table[0]}')