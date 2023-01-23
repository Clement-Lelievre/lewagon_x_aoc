import re
from itertools import permutations

INPUT = '''Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70'''

distances = {}
unique_cities = set()
pat = re.compile(r'(\w+)\sto\s(\w+).*?(\d+)')
for row in INPUT.splitlines():
    cities = pat.findall(row)[0]
    distances[','.join(sorted([cities[0], cities[1]]))] = int(cities[2])
    unique_cities.add(cities[0])
    unique_cities.add(cities[1])

min_dist = 10**9
perms= permutations(unique_cities, len(unique_cities))
for perm in perms:
    dist = 0
    for i in range(len(perm)-1):
        dist += distances[','.join(sorted([perm[i], perm[i+1]]))]
        if dist > min_dist:
            break
    if dist < min_dist:
        min_dist = dist
        
print(f'{min_dist=}')

# part 2
max_dist = 0
perms= permutations(unique_cities, len(unique_cities))
for perm in perms:
    dist = 0
    for i in range(len(perm)-1):
        dist += distances[','.join(sorted([perm[i], perm[i+1]]))]
    if dist > max_dist:
        max_dist = dist
        
print(f'{max_dist=}')