from tqdm import tqdm
import numpy as np

INPUT='''59715091976660977847686180472178988274868874248912891927881770506416128667679122958792624406231072013221126623881489317912309763385182133601840446469164152094801911846572235367585363091944153574934709408511688568362508877043643569519630950836699246046286262479407806494008328068607275931633094949344281398150800187971317684501113191184838118850287189830872128812188237680673513745269645219228183633986701871488467284716433953663498444829748364402022393727938781357664034739772457855166471802886565257858813291667525635001823584650420815316132943869499800374997777130755842319153463895364409226260937941771665247483191282218355610246363741092810592458'''
# INPUT = '80871224585914546619083218645595'
# INPUT='12345678'

# output = list(map(int, INPUT))
# l = len(output)
# mult_func = lambda x,y:x*y

# for i in tqdm(range(100)): # nb of phases
#     new_seq = ''
#     for _ in range(l): # in each phase, one iteration per sequence character
#         pat = [0]*(_+1) + [1]*(_+1) + [0]*(_+1) + [-1]*(_+1)
#         if len(pat) < l:
#             pat = pat * (l//len(pat)+1)
#         seqs_to_multiply = zip(pat[1:], output)
#         # print(f'{list(zip(pat[1:], output))}')
#         new_digit = str(sum(mult_func(x,y) for x,y in seqs_to_multiply))[-1]
#         new_seq += new_digit
#     # print(f'{new_seq}')
#     output = list(map(int, new_seq)) # if one doesn't write list(), then it gets badly wrong: it works only on the first ietartion of each phase
# # and then the map object has been consumed so the zip yields nothing
    
# print(''.join(map(str,output))[:8])

# MRE to understand why error happens on line 22 if list() is not used##############################
# toto = map(int, ['1','2','3'])
# tata = [0,1]
# for _ in range(3):
#     print(list(zip(toto, tata)))
#########################################################################################################
# this is also true for zip():
# a=zip([1,2],['a'])
# for _ in range(2):
#     print(list(a))


# part 2 ####################################################################################################
# Let's use Numpy to fasten things up
# so the first seven digits of my initial input represent the message offset and are: 5971509, meaning
# that the relevant digits in the final output list are 5971110 through 5971117 included
# it seems I can just compute the digits for each phase at those indices and below, because it'll only be 1s
# output = np.array(list(map(int, INPUT*10_000)))
# l = output.shape[0]
# # # l =100
# # # # # notice how in the above method there was redundant work: creating the pattern rows over and over again
# # # # # this time, let us make once and for all a 650000*650000 pattern matrix
# relevant_input = output[int(INPUT[:7]):]
# pattern_matrix = []
# rl = len(relevant_input)
# # z, o = np.zeros(shape=(l,)), np.ones(shape=(l,))
# for i in tqdm(range(int(INPUT[:7]), l)):
#     zeros, ones = np.zeros(shape=(i,)), np.ones(shape=(l - i,))
#     base_pat = np.hstack((zeros,ones))
#     pattern_matrix.append(base_pat)
# pattern_matrix = np.array(pattern_matrix)



# for i in tqdm(range(2)): # nb of phases
#     new_seq = ''
#     print(pattern_matrix @ relevant_input)
    

        
# print(output)   
# str_output = ''.join(map(str,output))
# offset = int(str_output[:7])
# print(str_output[offset+1:offset+9])

# borrowed from https://github.com/Dementophobia/advent-of-code-2019/blob/master/2019_16_p2.py after giving up
def solve():
    offset   = int(INPUT[:7])
    elements = [int(num) for _ in range(10_000) for num in INPUT][offset:]
    print(len(elements), offset, len(INPUT)-offset)
    for _ in range(100):
        for i in range(-2, -len(elements)-1, -1):
            elements[i] = (elements[i] + elements[i+1]) % 10
    return "".join(str(x) for x in elements[:8])

print(solve())
