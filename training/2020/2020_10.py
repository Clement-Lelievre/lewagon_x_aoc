from functools import reduce


INPUT = """76
12
97
28
132
107
145
121
84
34
115
127
22
23
11
135
113
82
140
119
69
77
83
36
13
37
92
133
122
99
147
112
42
62
65
40
123
139
33
129
149
68
41
16
48
109
5
27
142
81
90
9
78
103
26
100
141
59
55
120
126
1
35
2
20
114
58
54
10
51
116
93
6
134
108
47
70
91
138
63
19
64
148
106
21
98
43
30
146
46
128
73
94
87
29
"""

inp = sorted(map(int, INPUT.split()))
inp = [0] + inp  # add the outlet plug rating, which is 0
# bag_adapter_rating = inp[-1] + 3
one_diff = 0
three_diff = 1  # add the bag adpater diff, which is always 3
current_joltage = 0

for i in range(len(inp) - 1):
    diff = inp[i + 1] - inp[i]
    if diff == 1:
        one_diff += 1
    if diff == 3:
        three_diff += 1

print(one_diff * three_diff)

# part 2 #####################################################################################
nb_arrangements = 0
inp = sorted(map(int, INPUT.split()))
inp = [0] + inp  # add the outlet plug rating, which is 0
inp.append(inp[-1] + 3)

# def recur_adapter_array(current_rating: int, arr: list[int], last_value: int = inp[-1]) -> None:
#     """`Recursively` explores and counts all possible adapter arrays

#     Args:
#         current_rating (int): self-explanatory...
#         arr (list[int]): the array of adapters
#         last_value (int, optional):  Defaults to inp[-1].
#     """
#     global nb_arrangements
#     # base case
#     if arr == [last_value]:
#         nb_arrangements += 1
#     else:
#         candidates = [nb for nb in arr if current_rating + 1 <= nb <= current_rating + 3]
#         for candidate in candidates:
#             recur_adapter_array(candidate, arr[arr.index(candidate):])


# if __name__ == '__main__':
#     recur_adapter_array(0, inp)
#     print(nb_arrangements)

# the above works but is too slow, because many subpaths are computed over and over again
# i="""16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""
# print(sorted(map(int, i.split())))

# plan: identify sequences with crossing points
# compute possibilities there (increasing number series)
# multiply all those values (e.g. function reduce with lambda x,y : x*y)

# def recur_adapter_array(arr: list[int]) -> None:
#     """`Recursively` explores and counts all possible increasing sequences of joltage ratings

#     Args:
#         current_rating (int): self-explanatory...
#         arr (list[int]): the array of adapters
#         last_value (int, optional):  Defaults to inp[-1].
#     """
#     global nb_arrangements
#     # base case
#     if len(arr) == 1:
#         nb_arrangements += 1
#     else:
#         candidates = [nb for nb in arr if arr[0] + 1 <= nb <= arr[0] + 3]
#         for candidate in candidates:
#             recur_adapter_array(arr[arr.index(candidate):])


multiple_choices = []

for i in range(len(inp)):
    if len([elem for elem in inp[i + 1 :] if elem <= inp[i] + 3]) > 1:
        multiple_choices.append(True)
    else:
        multiple_choices.append(False)

sequences = zip(inp, multiple_choices)

seqs = []
current_seq = []
for ind, multiple_choice in sequences:
    if multiple_choice:
        current_seq.append(ind)
    elif current_seq:
        seqs.append(current_seq)
        current_seq = []

possibilities = []
for item in seqs:
    s = set()
    for elem in item:
        for nb in [_ for _ in inp if _ <= elem + 3 and _ >= elem + 1][:-1]: # here the perf can be improved
            s.add(nb)
    possibilities.append(s)
    s = set()

# print(inp, possibilities, sep='\n')
nb_increasing_sequences = {1: 2, 2: 4, 3: 7}

# print(possibilities)
# print(list(map(len, possibilities)))
r = reduce(
    lambda x, y: x * y, map(lambda x: nb_increasing_sequences.get(len(x)), possibilities)
)
print(r)
