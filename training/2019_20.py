import numpy as np

INPUT = '''
         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       
'''
             
donut = np.array([list(row) for row in INPUT.splitlines() if row.strip()])
nb_rows, nb_cols = donut.shape
# get the start and end positions
if 'A' in donut[:2, :]:
    for i in range(nb_cols):
        if donut[0, i] == 'A':
            start_pos = (2, i)
            print(f'{start_pos=}')
            break

end_pos = (3,2) # to do

# perform BFS
shortest_path_length = float('inf')
visited = set()
neighbours = {}


def recurse(current_pos: tuple[int, int], current_path_length):
    global shortest_path_length
    if current_pos in visited:
        return
    if current_pos == end_pos:
        if current_path_length < shortest_path_length:
            print(f'new record: {current_path_length}')
            shortest_path_length = current_path_length
        return
    for neigh in neighbours[current_pos]:
        recurse(neigh, current_path_length + 1)
    