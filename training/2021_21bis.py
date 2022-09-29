INPUT= """Player 1 starting position: 6
Player 2 starting position: 8
"""
# part 2



from itertools import product
from functools import reduce
from tqdm import tqdm
from collections import defaultdict

combs_player_1 = set(product('3456789' , repeat=4))
combs_player_2 = set(product('3456789' , repeat=4))

dice_comb = {3: 1, # key: the sum of the 3 dice throws, value: the nb of dice combinations leading to this sum
             4: 3,
             5: 6,
             6: 7,
             7: 6,
             8: 3,
             9: 1}

gen1 = (c for c in combs_player_1)
gen2 = (c for c in combs_player_2)

def who_wins(start1: int, throws1: list[str], start2: int, throws2: list[str]) -> int:
    """says which player will win in the scenario given"""
    score1 = 0
    score2 = 0
    pos1 = start1
    pos2 = start2
    i = 0
    while True:
        pos1 += int(throws1[i])
        pos1 = a if (a := pos1%10) != 0 else 10
        score1 += pos1
        if score1 >= 8:
            return 0
        pos2 += int(throws2[i])
        pos2 = a if (a := pos2%10) != 0 else 10
        score2 += pos2
        if score2 >= 8:
            return 1
        i += 1

ans = 0
for seq1 in tqdm(gen1):
    gen2 = (c for c in combs_player_2)
    for seq2 in gen2:
        ans += who_wins(4,seq1 , 8, seq2)

print('player 2 wins', ans, 'games')

































# def win_in_n_rounds(n: int) -> tuple[set]:
#     """returns the possibilities of winning after exactly n rounds in terms of dice sum at each round"""
#     combs = product('3456789' , repeat=n)
#     wins_in_n =  set([comb for comb in combs if sum([int(v) for v in comb])>=21 and sum([int(v) for v in comb][:n-1])<21])
#     return wins_in_n

# def loss_in_n_rounds(n: int) -> tuple[set]:
#     """returns the possibilities of not winning after exactly n rounds in terms of dice sum at each round"""
#     combs = product('3456789' , repeat=n)
#     nowins_in_n = set([comb for comb in combs if sum([int(v) for v in comb])<21])
#     return nowins_in_n



# pos_sum_combs = defaultdict(int) # the (sum, pos) -> score dictionary
# for sum in range(3,10):
#     for position in range(1,11):
#         pos_sum_combs[(sum, position)] = a if (a := (position + sum) %10) != 0 else 10

# score_1 = 0
# score_2 = 0
# pos_1 = 4
# pos_2 = 8
 
# ans = 0
# for nb_rounds in tqdm(range(3,8)):
#     w  = win_in_n_rounds(nb_rounds)
#     l = loss_in_n_rounds(nb_rounds-1)
#     for win in w:
#         win = [dice_comb[int(item)] for item in win]
#         for nowin in l:
#             nowin = [dice_comb[int(item)] for item in nowin]
#             ans += reduce(lambda x, y : x*y , win) * reduce(lambda x, y : x*y , nowin)

# print(ans)
# score_1 = 0
# score_2 = 0
# pos_1 = 4
# pos_2 = 8
# combs_player_1 = set(product('3456789' , repeat=7))
# combs_player_2 = set(product('3456789' , repeat=7))
# player1_wins = 0
# player2_wins = 0


        
# for comb1 in tqdm(combs_player_1):
#     for comb2 in combs_player_2:      
#         print(who_wins(4, comb1, 8, comb2))

# for comb1 in tqdm(combs_player_1):
#     for comb2 in combs_player_2:
#         print(len(comb1), len(comb2))
#         # for i in range(7):
#         #     pos_1 += int(comb1[i])
#         #     pos_1 =  a if (a := pos_1%10) != 0 else 10
#         #     score_1 += pos_1
#         #     if score_1 >= 21:
#         #         player1_wins += 1
#         #         break
            
#         #     pos_2 += int(comb2[i])
#         #     pos_2 =  a if (a := pos_2%10) != 0 else 10
#         #     score_2 += pos_2
#         #     if score_2 >= 21:
#         #         player2_wins += 1
#         #         break
    
# print(max(player1_wins, player2_wins))