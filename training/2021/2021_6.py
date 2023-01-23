input = """1,4,3,3,1,3,1,1,1,2,1,1,1,4,4,1,5,5,3,1,3,5,2,1,5,2,4,1,4,5,4,1,5,1,5,5,1,1,1,4,1,5,1,1,1,1,1,4,1,2,5,1,4,1,2,1,1,5,1,1,1,1,
4,1,5,1,1,2,1,4,5,1,2,1,2,2,1,1,1,1,1,5,5,3,1,1,1,1,1,4,2,4,1,2,1,4,2,3,1,4,5,3,3,2,1,1,5,4,1,1,1,2,1,1,5,4,5,1,3,1,1,1,1,1,1,2,1,3,1,2,
1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,4,5,1,3,1,4,4,2,3,4,1,1,1,5,1,1,1,4,1,5,4,3,1,5,1,1,1,1,1,5,4,1,1,1,4,3,1,3,3,1,3,2,1,1,3,1,1,4,5,
1,1,1,1,1,3,1,4,1,3,1,5,4,5,1,1,5,1,1,4,1,1,1,3,1,1,4,2,3,1,1,1,1,2,4,1,1,1,1,1,2,3,1,5,5,1,4,1,1,1,1,3,3,1,4,1,2,1,3,1,1,1,3,2,2,1,5,1,
1,3,2,1,1,5,1,1,1,1,1,1,1,1,1,1,2,5,1,1,1,1,3,1,1,1,1,1,1,1,1,5,5,1"""
from tqdm import tqdm
import threading
from typing import List

gen = [int(nb) for nb in input.split(',') if nb != '']

# for i in tqdm(range(80)):
#     new_gen = []
#     for fish in gen:
#         if fish in range(1,9):
#             new_gen.append(fish - 1)
#         elif fish == 0:
#             new_gen.append(6)
#             new_gen.append(8)
#     gen = new_gen
# print(len(gen))

# part 2
# 256 generations is too big to compute entirely, so let us find a smarter way
# results = []
# def compute_fish(nb_gen: int, gen: List[int]):
#     for i in range(nb_gen):
#         new_gen = []
#         for fish in gen:
#             if fish in range(1,9):
#                 new_gen.append(fish - 1)
#             elif fish == 0:
#                 new_gen.append(6)
#                 new_gen.append(8)
#         gen = new_gen
#     results.append(len(gen))

# threads = []
# for i in range(0, len(gen), len(gen)//20):
#     thread = threading.Thread(target = compute_fish, args = [256, gen[i:i+len(gen)//20]])
#     threads.append(thread)
#     thread.start()
    
# for thread in threads:
#     thread.join()
    
# print(sum(results))

# 1 divide initial poopulation into groups acc to the value
# 2 for each of the above groups perform the following:
# 3 liquidate the residual
# this population doubles every 6 days (gen0)
# gen1: let 8 days pass

#print(set(gen)) {1,2,3,4,5}
# gen = [3,4,3,1,2]
# def compute_children(initial_day_value: int) -> int:
#     days = 18
#     gen_studied = [nb for nb in gen if nb == initial_day_value] # the sub-population studied
#     initial_pop = len(gen_studied)
#     pop = initial_pop
#     # liquidate residual
#     days -= (initial_day_value+1)
#     # compute first generation number of children over the whole period
#     pop *= 2
#     pop += initial_pop*(days//7)
#     for k in range(1, days//9): # next generations
#         days_reset = days
#         days_reset -= (9 * k)
#         pop += initial_pop
#         if days_reset >= 0:
#             pop += initial_pop * (days_reset//7)
#         else:
#             break
#     return pop

# answer = 0
# for i in set(gen):
#     answer += compute_children(i)
# print(answer)

days = [0] * 9
# Update the current numbers
for fish in gen:
    days[fish] +=  1
for i in range(256):
    # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8    
    today = i % len(days)    
    # Add new babies
    days[(today + 7) % len(days)] += days[today]
print(f'Total lanternfish after 256 days: {sum(days)}')

    