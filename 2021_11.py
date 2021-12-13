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

nb_flashes = 0

def no_more_flash(cavern: list[list[int]]) -> bool:
    for row in cavern:
        for octopus in row:
            if octopus > 9:
                return False
    return True

def number_flashes(cavern: list[list[int]]) -> int:
    return sum([len([octopus for octopus in row if octopus > 9]) for row in cavern])   
   
def flash(cavern: list[list[int]]) -> list[list[int]]:
    """updates the cavern values after flashes occur"""
    # sets the octopuses that just flashed to 0
    [[(2-len(str(octopus)))*octopus for octopus in row] for row in cavern]
    # 
    
    
def step(cavern: list[list[int]]) -> None:
    """performs one step, increments the nb flashes and returns the cavern after the step"""
    global nb_flashes
    for row in cavern:
        for octopus in row:
            octopus += 1
    nb_flashes += number_flashes(cavern)
    while not no_more_flash(cavern):
        cavern = flash(cavern)
        nb_flashes += number_flashes(cavern)

print(nb_flashes)
    
