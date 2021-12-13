input = """
8271653836
7567626775
2315713316
6542655315
2453637333
1247264328
2325146614
2115843171
6182376282
2384738675"""

demo = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

demo = [item for item in demo.split('\n') if item != '']
demo = [[int(char) for char in item] for item in demo]
input = [item for item in input.split('\n') if item != '']
input = [[int(char) for char in item] for item in input]
nb_flashes = 0

def no_more_flash(cavern: list[list[int]]) -> bool:
    for row in cavern:
        for octopus in row:
            if octopus > 9:
                return False
    return True
   
   
def flash(cavern: list[list[int]]) -> list[list[int]]:
    """updates the cavern values after flashes occur"""
    # increments by 1 octopuses adjacent to a flash (incl. diagonally adjacent)
    for r in range(len(cavern)):
        for c in range(len(cavern[0])):                
            if cavern[r][c] > 9:
                try:
                    cavern[r-1][c] += 1 if (cavern[r-1][c] >0 and r != 0) else 0
                except IndexError:
                    pass
                try:
                    cavern[r+1][c] += 1 if cavern[r+1][c] >= 0 else 0
                except IndexError:
                    pass
                try:
                    cavern[r-1][c-1] += 1 if ((cavern[r-1][c-1] >= 0) and (r!=0) and (c !=0)) else 0
                except IndexError:
                    pass
                try:
                    cavern[r-1][c+1] += 1 if (cavern[r-1][c+1] >= 0 and r != 0) else 0
                except IndexError:
                    pass
                try:
                    cavern[r+1][c+1] += 1 if cavern[r+1][c+1] >= 0 else 0
                except IndexError:
                    pass
                try:
                    cavern[r+1][c-1] += 1 if (cavern[r+1][c-1] >= 0 and c != 0) else 0
                except IndexError:
                    pass
                try:
                    cavern[r][c-1] += 1 if (cavern[r][c-1] >= 0 and c != 0) else 0
                except IndexError:
                    pass
                try:
                    cavern[r][c+1] += 1 if cavern[r][c+1] >= 0 else 0
                except IndexError:
                    pass
                cavern[r][c] = -1
    return cavern
    
    
def step(cavern: list[list[int]]) -> list[list[int]]:
    """performs one step, increments the nb flashes and returns the cavern after the step"""
    global nb_flashes
    for r in range(len(cavern)):
        for c in range(len(cavern[r])):
            cavern[r][c] += 1
    #nb_flashes += number_flashes(cavern)
    while not no_more_flash(cavern):
        cavern = flash(cavern)
        # for i in cavern:
        #     print(*i)
        # print('\n')
        #nb_flashes += number_flashes(cavern)
    nb_flashes += sum([len([octopus for octopus in row if octopus < 0]) for row in cavern])
    cavern = [[max(0, octopus) for octopus in row] for row in cavern]
    return cavern

cavern = input
for _ in range(100):
    cavern = step(cavern)
    #print(cavern)
print(nb_flashes)
    
