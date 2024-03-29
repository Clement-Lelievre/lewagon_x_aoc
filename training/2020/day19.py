import re
INPUT = """44: 91 71 | 77 109
94: 15 77 | 129 91
73: 113 77 | 24 91
125: 77 38 | 91 37
25: 77 24 | 91 112
37: 105 77 | 50 91
47: 22 91 | 105 77
67: 91 109 | 77 45
130: 58 91 | 6 77
2: 19 77 | 10 91
48: 77 76 | 91 7
20: 10 91 | 65 77
65: 22 77 | 115 91
29: 77 126 | 91 79
105: 77 91 | 91 91
102: 87 77 | 114 91
38: 50 77 | 50 91
56: 91 107 | 77 106
9: 77 101 | 91 73
21: 77 72 | 91 54
35: 22 77 | 112 91
101: 91 115 | 77 34
122: 77 105 | 91 14
108: 77 111 | 91 52
66: 3 91 | 27 77
112: 91 28 | 77 91
61: 91 24 | 77 34
77: "a"
64: 77 99 | 91 119
106: 77 68 | 91 22
107: 24 77 | 113 91
39: 91 22
31: 53 91 | 127 77
8: 42
88: 34 91 | 113 77
27: 49 91 | 25 77
99: 91 87 | 77 58
10: 77 113 | 91 50
123: 91 100 | 77 68
1: 14 91 | 50 77
51: 112 91 | 34 77
42: 77 36 | 91 69
0: 8 11
76: 77 130 | 91 63
110: 91 100 | 77 124
46: 91 15 | 77 35
95: 120 91 | 23 77
50: 91 91
41: 28 4
57: 91 50 | 77 115
72: 91 46 | 77 125
30: 91 116 | 77 128
24: 28 77 | 91 91
109: 77 24 | 91 115
85: 91 113 | 77 68
87: 14 91
22: 91 77
45: 91 84 | 77 113
18: 77 12 | 91 20
98: 77 110 | 91 96
53: 77 92 | 91 90
120: 77 68 | 91 105
93: 77 115 | 91 34
126: 43 77 | 118 91
79: 77 47 | 91 83
89: 106 91 | 51 77
4: 68 91 | 105 77
62: 77 33 | 91 44
23: 91 115 | 77 113
32: 91 40 | 77 39
54: 59 91 | 74 77
52: 91 75 | 77 5
75: 77 104 | 91 15
104: 22 91 | 68 77
91: "b"
11: 42 31
90: 91 82 | 77 26
111: 117 91 | 41 77
63: 91 123 | 77 10
82: 89 91 | 80 77
6: 91 50 | 77 14
129: 84 28
55: 56 91 | 94 77
70: 77 93 | 91 88
58: 22 77 | 22 91
81: 22 77 | 68 91
3: 77 16 | 91 78
40: 34 91 | 84 77
36: 121 91 | 30 77
127: 91 21 | 77 48
115: 91 91 | 91 77
96: 77 97
71: 77 84 | 91 105
83: 22 77 | 100 91
118: 84 77
84: 28 77 | 77 91
43: 77 84 | 91 22
69: 77 60 | 91 108
68: 91 77 | 77 77
97: 77 77
100: 77 91
28: 77 | 91
113: 91 77 | 77 91
33: 77 61 | 91 103
5: 91 1 | 77 87
78: 34 91 | 97 77
74: 58 91 | 129 77
16: 14 77 | 84 91
26: 95 77 | 32 91
34: 28 28
92: 55 77 | 66 91
116: 77 102 | 91 70
7: 98 91 | 2 77
59: 61 91 | 17 77
121: 64 91 | 18 77
60: 91 29 | 77 62
12: 77 13 | 91 122
49: 124 28
124: 77 91 | 77 77
114: 77 115 | 91 24
80: 86 77 | 81 91
128: 67 77 | 9 91
86: 14 77 | 105 91
119: 77 85 | 91 4
14: 91 91 | 77 77
19: 91 68 | 77 34
15: 84 77 | 115 91
117: 73 77 | 57 91
103: 91 105 | 77 24
13: 91 14 | 77 50
17: 22 91 | 115 77

aabbbbbabaaaaabbbbabaabb
ababaabababaababbababaaa
aaaababaabbabbaabaaabaab
bbaababaabbababaabbbabab
baaabbbbabbabaabbababbba
ababbbaaaabaabbaabbbabbababbbabbbaabbbabaaaabaab
abbbabbbbbbbbabaaabaaaaabaabababaaabbaab
bbbbbbbbababbababaababaa
aabaabbabbbbaaaaaababaab
aababbabababbbbababaabaabaaababaabbbbabbaabbabaaabaaabab
bbbabbbaababbbaabaabbbba
bbabbbaaaaabaabbaababbba
abbabaababbaabaabaabbbabbabaababbabbaaaa
aabbabbaabababababaaaaab
baaaabbbbbaabbaaaabbbaba
abbaabaabbaabbbbbbbaaaba
aabbaaabaaaaaabaababbaab
abaaabbbabaabaabbbaaabbbbaababaabababbbb
abbbabaaabababbbabbaaabababbabaa
bbabaaabbaabaaaaabbbaabbabaabaab
abbbabaabbaabbababaabaaabababaaabbaabaaa
abaababababbabababaaaaaa
abbbabbbabbababbbbabbabababaaaaababaabbb
aabaababaabbaabaabaabbaa
aabaababbbaabbbabbabbaaa
aaabaaaaabbbabaaaaabbaab
aaaabbbabaabaabaabbbaabb
baaaaabbabbbbabbbabababb
abbababbbbbbbbbbbabababa
aabababababaaabaabaabbaa
bbbaabbbbbbaabbbabbabaaabbaaaaaa
bbabbaabbaabbaababbaabbbbababaabbaaabababbaaabbb
bbaaaabaababaabaabababaa
abbababbbbbbabababbbbaaabababbaaabbaabbaabbbabaaabaabaaa
bbaabbaabbbbbabaaaaabaab
babbaaabababbbabbaaabbaa
aaababbbbababaababbbaabb
baaaaababbabbbaaabbbabbbabaabaaa
babaaabaabbabbaaabbbaaaa
aabaaaaabaaaaaaabbaababbbaaaabbabaabababaababbbb
baaaaabbabaaabaababaaaaabbabbbbb
bbbbaaaaaabaabbababbabaa
abbaabaabbbbbbaabaaabbabbbbbbbaababbbbab
baaaabbabbabbbabaabbaabb
aababaaaaabaababbabbbbbb
baaabaaabbaaaabaababbabbbbababaabbaabbbababbbbbb
abababbbaabaabbabaababbabbbbababbbbbbaaaababbaaa
babbababaaababbbabaababbaababbaaabbabaaaaabbababbbbaaaaabaaabbba
aabbbbbaababbbaaabaababbabbabaaabbbabbbbbbabbaaaababbbbbabbbaaabaababbba
bbabbaaabaabaaabbaaabbaa
ababbbabaaabbababbabaabaaababbabbabbaabbbababbbbbbaaaaba
aababbababbbbaaaabaaaaab
bbbbabbbaaabbabbbbabaaababababbabbaaaaaaababaaabaaabbbaaababaaaababbabbaabaaaaab
abaababbbabbbbbbaaabbaabbbaaaaaa
baabbaaaabbabaaaaababbba
bbabbababbabbabbbaaaaaaabaabbbbbaabbababaaaababa
abbabaaaabaababaaaaababaabbababbbbaababaaabaabbbbabbbbbbbbbbabbbabbbaabb
abbabbabaaaaabaaaabbabbaaaaaabaabbabbbaabbbbabbaabbabababaabaababbbbbbbbabbbaaabbaaabbbb
bbaabbbbababbbbabbbbabba
abaabbabbaabbbabbbbaaaba
aaaaaababababbaaaabaabbaabbbaaaa
abaababababaaababbbbaaba
abaaabaaaaabaaabaabbbbaaababaabaaaabaaaaabbaabbabbbabbabaababbba
aabbbbbbabbabbbabbbbaaab
bbbbbaaaaabbbbabaabbaaabbabaabbb
abaaaabbbbbabbbbbbbababb
baababbbbaaaaabbbaaabbaa
abbbbbabbaaaabbbbbbabbaa
bbbaaabaabbbabababbaaaba
abbbbbbaabaabbabbbbbaabb
baababaaaabaabbbabbaaaaaaaaabaabbabbbbbbaababaaaabbababaababaaabaaabaabbaaaaaabaaaababab
bababaabbaababbabababbba
baaaaabbaabbaabaaaaaaaaa
babbaabaabbbbaabaabbbbbbaabbbbbaababaaaaaaabaaba
aababbabbaaababaaabbbaba
babaabaaabaabbabbabaababbbbbbbaabbaabaababaabaaabaabaaabbaabbbaa
aaaabababaaabaaabbabbaaa
bbbbbbaabbaabbbbbbbbaaaabbaaaabb
bbabbaabaaaaababbaabaabbbaababbababbaaabbaaabaababaaaaabbbbbbaababbaaaba
baaaabbbabbabaaabbbaabba
abaaaabbbaababbabbaabbbbabbbbbababaabaab
abbbbbbabaaaababaaabaabaaaabbbaa
aaabaaababbaabbbbaabaababbabaaaa
abbaabbabaabbabaabaabbbb
bbabbababbabaabbaaabbaabbbbaabbabbbbabbbaaabaaababbabbaabbbabbab
baaababbbbbbbaaababbbbbb
ababaababaabaabaaaaabbbb
baabaaaaabbbbbbabbaaaabb
aaabaababbbbaabaaaaaaaabaababaabababababbabbabaaabbaabba
abbabaaaaaaabaaabbbababb
aababbaabbababaababbaaab
abaabababbbabbbabbbbaaba
ababbbaaaabaaaaababbbaab
aabbbbaaaabaabbbbabbbaab
bbbabbbaaabaaaaaaababbaaabbabbabaabababbaabbbaba
abbbabaabbaabbbbbbaaaaaaaabbbbabbbaababbabbbbbbabaabbaba
ababababbaababbabbaaabab
bbbbababbbbabaabbbabababbbababbbabbababbbaababbb
aaabaaaabaababbaaaababbbbbbaaaaabaaaaaaababbabaaababaabababbabaaabaabbba
aaaaaababaaaaaabbbbbaabb
aaaaaabaabbabbbaaabaaaaabaabbbba
aabbbbbaaaaaaababaababaa
bbaaaabaabbaabbbabbaaabb
baabbaabbbbaaaabbabaabaa
baabaabaababbbbaabaaabbb
ababbabbaaabbbabaabbaabb
ababababababbbaaaabbaaaa
bbbaaaababbbaabaaaaabbaa
aaababbbbbbbbaaaabbabbbbbbaaaabbaababbba
bbbbbbbbbbabababaaabbbaa
bababbaaabaaaabbabbabbbb
aaaaabbabbabaabbbbbababaaaaababbababbaab
aabbabbabbaabbbbabaaaaab
bbaabaabaaababaababbbbbbaaaaabbaabaaaaaaabbbabaaabbabbbbbbabbbbb
aaaabbbabaabbabaaaabbaaabbabaabaaabababbbababaaa
baabbbbbabbbbababbbaaaba
abbabbaaabaababbbbbbbaaabbbbababbbbbaaab
abbbaababbabbabaaababaab
aababbababbaabbbbbababbb
baaaaabbbbbbabbbaaabaabbababbabbbbbaabab
aabbaaabbbbbbbbbaababbaaaaabaaba
abbbbaaabbbbababbbbbabbb
bbaabbbbbaaaabbbaaaabbbb
bbabbbbbbabbbbaaaaaaabbabababbaabbabbaabbabaabba
babaaabaaabbabbabbbaaabaaabaaababbbabaaa
baabaaaabbababbababbbbbaaababbba
aabbbbbabbabababaaaabaab
aaaaaabaabababababbbabab
babaababbaaaabbabbbabbab
ababbbaababaaaaaaabbabbb
bbaabbbbaabbbaaaabbbabbabaaaaabababbaabb
baaaaabaaabbbbabbababbbb
aabaaaaabaaaaaaaaabbbbbababbaabbaababbbabaabaaababbbabab
bbaaaabaabbbbaaabababbbb
aababbaababaababaabaabaa
aaaaaababbaaabaaaabaaabb
bbbabbbababbaabaaabbaababbaabbbbaababbba
aaabbbbaabbababbaababbbb
baabbbabbbaabbabbbbaabaabbbaaabbbbbaabaabaaabbaa
aabaababaaaaabbaaaaabbbb
baaaaaaaabbbbababbbbabaabbaaaababaaaaaaaaabbbbbabbbaababbbaabbabbbaaabbb
aabbbbaabaaababaaabaabbabbbbbabbbababbbb
babbaaabbbbbbaababbbabab
aabbbaaabaabababaabaabbbabbaaaabaabaababbabaabbabbabbbbbbabbabbaababbaaa
abbbabaaabbaaaabbabbabbb
aababaaaabaabbbababaababbaabaababaaabbbbaabababb
aaaabaaabbaabaabaabaababaaaaaaba
baaabbabbbaabbaaaababaab
aaaabbabbbbbbabaabbaaaababbbaabb
bbabaaabbbabbababbbabbbaaaabbaab
baaaaabaabbababbabaababbaabaaaab
babaaaabbabababbbbaaaabaabababaaaaabbbbbaaababbbabaaabaaababbaba
baaabbabbabbababbabbbbba
aaabbaaabbabaaabbbbbbaab
abbbbaaaaaaaabbabaabbbba
aabababaaaaabaaabbbaaaaa
aaaaaababaaaabbbbabbabaa
abaabaabbaaaaaababbbabba
baaabababaaaaaabbabaaabb
bbbbbababaaababbbbbaaaaa
aabaabbbbbaabababbbbabbb
bababaabbabaabaaabbbabba
bbbabbbabbabaababbbbaabb
aabbaababbbabaabbabbabbb
baababbaabbaaaabbabababaababbbbaaababaaaaaabbbab
abbbaababbaabababbbbaabb
bbbabbbabbbbababaabbabab
abbbbaababbbabaaaabbbbbbbbabbbabbabababbaaabbbaabbaaabba
abbbbaaabaababbbaaaaaaab
abababbbaabbbbabababbaab
babbabaabbababbbababbbbbababaaab
babbbbaaaabaababaaabbbbb
aaabbaaabbaababbabbbbbbaaabbbbaaaababababbbaabab
abaaaabbbabaabababbbbbbababaaaaaaabaaaab
aabbbbbaaabababaaaabbbbb
babbabaabbbaabababaaaaaa
bbbbbbaabbbabbbababbbbbb
aabbbbaabbabaabaabbbbbbaabaababa
babbaabbabbaabbaabaabbaababbabbbaababbbaaaababbbbabaabab
abbbbabbbabaaabaabbaabab
baabbababbaabbaaabababababbbbabaabbbbaabbabbabbbabbabbbb
abbababbabababaabbabbaabaaabaaaaabbbabaaababbbbbaaabbbbabbbbabbbbabbbbaa
abbaabbaababbbbababbaabb
abbaabbabaaaaabaaaaaabbabababbab
aabbabbabbaaabababaaabab
aabbbaaaaaababaaaaaaaaaa
bbbaaaababbaaabbbbaaabba
aabababaaabaabbababaabba
bbbbaaaababbababababbaaa
babbabbaabbbbbabbaabbbbbbabbaabb
abbbbbabaaaabaaaaaaaaaab
bbabbabababaaabaaababaab
baaaabbabbbbaaaababbaaaa
baaaaabaaabababaaababaab
abbaabaaabbbbaaabbabaaabaababbaaaaaabbbaabaaaabaaaaabbaa
babbbbaaaaaabbaaaabbbbbbaaaaaabbbbbbabaa
aababbaabaaaaaabbbbbaaaaabaaaaba
abbaabaaaabaabbbaaaaabab
abaabbabbaababbaabbaaaabbbaabbab
bbabbbabbabaaabaababbaab
baaabbabaabbaabaabababaa
bbbabbbabaabbbabbaaabbaa
bbbbbbbbabbaabbbababaaab
bbabababbbbbbbabbaaabaab
abbbaabaaaabbbbabbababbbaababbbb
bbababababbbbbbaabbbaaab
abbababaaabbbbabbababbbb
babbabaabaaabbaabbbbbabbbaaabbbbaabababa
abaaaabbaababaaabbbbbabaaabaaabbabbbbbaa
bbaaaababaaababbbbbbabba
abbaaaababbabaaababaabababaababaaabaabbbababaaab
bbaaabaabaaaaaaabaabaaab
babaabaaaaaaabaaabababaa
baabbbbbabbabababababbab
ababbbbbbbbbaaaabaababbababbbbbbaabaabbbbabaabba
babaaababaabaaaaaabbaaabbbaaababaaaaaaab
abbabbbabbbbabaaabaaabba
abbababbababbbbaabbaaaba
abbbabaaaaaaabaabbbaabab
abbabbaaabbbbbabaaabbaab
babbbabbbbbbbbabbbbbbbba
ababbbbaaabbbaaaaaababab
bbbabaabbaabbbabbbbbbbabbaabaaab
baaaaabbbaaaaabaabbaaaba
aabaabbabaaaaabbaaababbbbaabbababababbab
bbaaababbaabbbbbabaaabbb
aaaaabbaabbabbbaabbabbbb
aaabaabbbbabbbbbbababbaa
bbaabbaabaabbababbbbbbba
bababaabbbbaaaababababbbaaababbbbbbbbababaabbaabbabaabbb
abbbbaabaabbbbbbbbabbbaaaaababbbbaaaaaabbabbbaababbabbab
abbbbabaaaabbbbaabbabbbaabbbbaababbbbaababbaaaaaaabbaaaa
baababaaabaabaaabaababbabbaaaabbabaabbaababbbbbb
baabaabbabbabaaaaaabbaab
babbababaaaabbbbaabaabaababbaabbababaaab
aaabaaabbaababbabbaaabba
babaabababbbabbabbabbaaa
aaaaabaaabbaabbaabababaa
aabaaaaaabababbbaabaabaaabaabaaa
babbabbabaabbbabababaaaa
aabbbbbbabababbbabbaabbaabbababaabaaabbbbaabbabbbabbbbab
baaaaaaabbbabbbbbabbaabb
abaaaabbbaaabaaabbababababababba
abbaaaabbaabaaaaaabbaaaa
aaababbabababbbaabaabbabbababbaaaababbbabbbbabaa
aaaaaababbbbabaaabbbbaaababbbbba
babbabababbbbbbaaaabbbbababbbaab
abbaaaabaaabbbaabbbaaaaaaabaaaaabbbbbbabbaabbbaaaaabbabaaabbaaba
baabaababaabbbbbbaabaaaa
baaababbbaabaaaabbbbabba
bbabbabaaaaaabbaaaababab
abbaabaabbabbbababaaabbb
baabaaaaabbbabaaababaaaaababbabaaababaabaabaaaab
bbbbabaaaaabaaabaabbabaa
abbbaabaabaabaaaabaaababaabbabaabaabbabaababbbaaabaaabbb
bbaabbbaababbbbababaaabaaaabaababbabbaaaaaabbbaaaaabaaabaababbbbaaabbbbb
aaababaaabbaabbbababaabb
abbbbabababbbbaaaababbababbabaaaaaababbbbaaabbab
baabaabaaabaababbbbbabba
bbabbbbbabbbabbbbbaabaaa
bbbbababbbabbababbabaaaa
abaaabaabbbaaaabaaaabaab
abbbbabaababbababbbbabbb
aabaaaaabbbbaaaabaabbabaaaaababb
abbababbbbabbababababbba
aaabbababaaaabbabaabbbbbbaabaaabbbaaaaaa
aabbaaabaaabaabababababaabbaabbaaabbababababbaabbbbbaabbbbbabaaaabbaaaababbabaabaabbbbaa
abbabbbaaabbaaabbbbbaaab
bbbbbaaababaababbabbaabbbbbabababaaaabab
abaabbbabbaaaabababbabbaabaabbaa
baaaabbababaababbbbaaabb
bbbaaabbbaaaaaaaabababababbaaaabbbaababbbabababa
babaaabaabaabbbaabbabbbb
aabbbbbbabaabbbaaabaaaaaaabbbbbabbabbbabbaaabbaa
bbaabababbaaaabaabaaabbb
aabbabaabbbbbabbbaabaaabababbbbbabbbaaaa
aaabaaaaabaabbbaabaaaaab
baabaabbaaabbababaababaa
bbbaaaabbabaaaabbababbbb
aabbbbabbabbabbaaaaababb
abaabbbabaabaabaabababbbababbbabbaaaaaab
abbbabaaabbabbaaaabbaaaa
aaaabababbbbabaaabbbaabaabbababbabbbabababaaababbbaaabbb
aaaaabaabaabbaaababaaabb
abababbbbbaabbaaababaaab
bbabbbaaaabbabbaabbbbabbaaaabbbaaabbababbbbabbaa
aababbaabaaabbbbbabababb
bbaababbaaaabbbaabbbbabababbaababbbbbaaa
babaaaaaaaabaaababbabbbb
bbbbabaabbbbaaaaaabbaabb
ababaabaaabbabbabbbaababababbbaaaabbaaabbbbbbbaa
bbabbababbbbababbbbaabba
bbbabaaabbbabbaaaababbba
baaababbababbbbaababbaaa
abaabbbababaababbbaababaaaaabababbbaaaabbbbbababaaaaaabbaaabbaab
babbbbabaabbbbbbaabababbbaabbbbbbabaaaaababaaaabaabbbabababaaaaaabbabbaabbaaaaab
ababaaabbbabbbaaabbabbabaaabbaab
bbabbbbbaababaaababaabba
aabaabbbbbbabaabaababbabbbaabbba
abbabaabbabbbbaaaaabbabababbbaab
baaaabaabaaaabbbbaaaaaabbbbaabab
aaabbbbaaabbaaabbbaaaaab
babaabaaabbaabaabaaabaab
baabbbbbbbbbababaaaababababaabbb
baaabaaaaaabbaabaaababbbbaaabbbbaaabbbbb
aaaaabaaabbababaaaaaabababbaaaaaaabbbaaabbbaaabbaaaaabaaaaabbaba
baaaaaabbaaaaabaaaaabaab
ababbbbaababbabbabaabbaa
abbbbaabbababaabbbabababababbbaaabaaabab
abbbbabaaaabaaabaaababab
abbabaaabaaaabbbabaababb
baabaaaabbbbbbababaabbbb
aabbbaaaaabbaabaabbbbaaabbbbbabababbabaabbbbabbabbbbaabb
baabaababbbbaaaaaabaababaabaababaabaabbaaababbaaaabbabaa
bbaabbaabbbbabaaaaababbbbababbba
abbbabaaabababbbbbaaaaaa
abbababbabbababaaaabababbbaaaaabbbbbaabbaababbbbaaabbaab
abbabbaabaaababbbabbbbba
aabaabbabaaabbbbbbabbabb
bbbbaaaaababaabaaabaaabb
abaaababbabbbbbabbbbbabaababababababababbaabbbbbbababaabbbbbbababaaaabbaabaaabbb
abbbabbabbbabaabbababbba
baabaaababaaababbabbbbbbaabbaababbaaabaabbbababaabaaaabb
baaababbabbabbaaaabbbbaaababbabbbbaababbabaabaaa
babaaaaaababbababbabaaaa
babbabbabbaababaaaaabaab
bbaabbbbaabbaaababbbbbbabababaaa
baaaaabbbabaaaabaaababba
bbbaaaababbababbabbbabab
bbaabaabababbabbbbbbabbb
aabbbbaaabaabbabaaaaabbaaaabaaababbaaaba
ababaabaaababababbabbbabbbbbbbaababaabbbabaaababbabbaaab
bbbabbbabaabbabaaabbaaaa
bbabbabaabbbabbbbbbbaabb
baaaaabbbbbbbabaaabaabbbbbbbbbbbabbabbbaabaabbaa
aaabaaaaababbabaaaababab
baabaabaaaaaaabaaabbbbababbbaababbaabbababbaababbabababa
abbbabbaaaabbaaabbbaabaa
bbbbababbbaabbaaaaaaaaab
aabbaaabbbbabbbaabbbbabababaabbb
bbaabababaabbaabbababbab
abbabababbbbababbaaaaabbbbbaabaa
babaabbbaaabbaaabbabbabbaaabbbbabbbaabbbababaaabbaababaa
abaaaabbababababbabababb
baaaaababababbaababbbaab
aabaaaaaaabaabbabbaabbba
baaaabaabaabaabbaababbabbabaabbaaababbbbbbbaaababbabaabb
aaaaabbabbbaaaabbabbbabbaaababba
baaaaababaabbaabbbabbaab
abbbabbbaaababaaabaaabab
aaabbbababbababbababbbab
baaaaaaaaaaaaabaabababaa
aaabbaaaaababbbbabbbaaaaabbbbbbabaaabbabaaabbbbaabbabaaa
abbaabbbabbabaabbbbababb
baaaaaaaaaabbaaaaabbbaab
abbaabbabaaaaaaaabaaaabbaabbbaababbbbbaa
bbabababaaabaaabbbabaabaabbbbbabaaaaaabb
babbabbaabaababbbbbbbbbbbbabaaaa
babbbbaabbbbabaaabaabaab
bbbabaababbbabbabaaabbbbbbaabaabbababbba
bbababaabaaaabaaabaababbbababaaa
bbbbbaaabaabbabaaaaabaaaaabaaaab
abbbaababbbbabababbaabbbbbabbaab
abababababbabbbababbaabaaabaabaabaaaabab
aaababbbbbabababbaaabababaaabbababbaababbbaabbab
abaaabaaababababbabbaaaa
aaababbbaabbaababbaaaaaa
abababbbbbaabaabbbabbaaa
baabbabaabbababbbbaabaabbbbaabbaaaaabbaa
aababbaabaaababbababaaab
abaabbabaaaaabbaababaaab
aaaaaababaaabbabaaabbaab
aabbbaaabababbbabbaaaabaabbbbbabbbbbbaaaaababbaaaabaabaaabbbaaaabbbbbaabbbaabaaa
aabaabbabaaababaababaaab
baaabababaabbbbbababbbbb
abaaabaaabbababbabbbbbbababbabbb
ababababbaabaabaabbbbabbababbbaabbbbbabbaaaabbbb
babbaabaaaabaabbbbbaaaabaabababaabaabaaa
aaabbabaabbaabbababbbaba
ababbabaaabbbbabbbbabbaa
aaaaabaaaaabaabbbbabaabaabbabbbaaaaabbaababbbabababaabbb
bbbbbaaabbabbbbbabbbaaab
bbbbbabbbabbaaaaaababbbbaaaaabababbbbabbbbabbbaaaaababab
baaabbaaababababababbbbababababbabaabaabbabbaabaaaababbb
baabbabaaaabbbbbaabbbaba
ababbbbabaaabababbbbbaaaabbbbbababaaabab
baaaaabbabaababaabbbabab
abbabbbabaababbbaabababb
aaabaabbbbbabaabbbbaabba
aaabbbabababbabaabababba
bbbbbbabbaaababbbbabbbbbbabaaaabbaaabaab
aaaaaabbbabababaaabbbabb
baabaabbaabbbaaabbaaaaaa
bbababaaabbbbaabbabbbbbb
bababaabaaabaaabbbbbaaba
bbbabbbbbabaaaabaaabbbabaabaaaaabababbba
aaabaabbabaababbbbbbbaab
bbbababbabaabaabababbbabbbabbbabbbbaaaaabbbabbbabababbba
aabbbbababbabbbaaababbbbbaabababaabaaabbbabbbbbbabbabbbaabbaabbb
abbaaaabbaaaabaabaabaaab
baabbabaababbabbbbabaabb
bbbbababbaabbababbaabaaa
abbbbaaabaaaabbbbbabbbbbaaaabbaa
abbabababaaaabaaabababbbabaabbabbbbbaabbbaabbabb
baabaaaaaababababbaaaaaa
abbaabaabbbbbabaaabaaaab
aabaababbbbbbaaabbaaababbbaaababaabbaaaa
aabbaaabaabbaabaaaaabbbb
bbabaaabaababaaaabbbabbaababbbbb
aaaabbbaababbbbaabbbbbabbbaabbab
abbaabaaabbabababaabbaabaaababaaababbbbb
bbabbaaababbaabbbaaabbaabbaaaaaababaaabbabbabbabbaaaabbb
aabbbbabaaaaaabaaabaaabb
baabaabababbababbbaaabababaabbaababbaaaa
bbbabbbbabaabababaabbbbbaaababaabbabbababbabbaababaaabbbaababaab
bbbaabaaabbabbbbabaabbaaaabaaaaaaaabaaabaabbbababbaaaababaabaaba
ababbababbabbbbbabbaaaaa
babbbbaabbaabababbaabbba
abbaabbbbbabbbaaabbabaabbabbaabaababbabbaababbaaabaaabbaaaaaababaabbabab
ababaababbabaabbbbabaaabbbabababbababbab
aababaaaaaaaabbabbbbbbbbbbaaabba
bbaabbbbbbaababaabaabaaa
bbbaabbbaaaabbabaababaab
bbabababababbbbaabaaabab
aaabbabaabbaabbbaabababb
ababababbaabbaaababbaabb
bbbbaaaabaaaaabbaabaabbabaabbabaabaabbbabbabbbbabbababbbbbbbabba
abbbabbbbbabbbaababaabbb
aabbaaabbbaababaababaababbbabbbabababaaabbaaabbb
abbbabaabbbaaaabaaababaabbbabaabbaababbabaabaabbabaabaabbabbaaabaababbba
abbabbaaaaabbbbababbbbba
aabbabbababaabaabbabaababbbabaabaababbaa
abbbbbabaaabbaaabbbaabaa
"""


# INPUT="""42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31 | 42 11 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42 | 42 8
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1

# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""
inp = [e.replace('"', "") for e in INPUT.split("\n") if e]  # drop the " in "a" and "b"
rules = [row for row in inp if row[0].isdigit()]
rules_dict = {
    int(e[: e.index(":")].strip()): e[e.index(":") + 1 :].strip() for e in rules
}
messages = [row for row in inp if row[0].isalpha()]

rule_0 = (
    " " + rules_dict.get(0) + " "
)  # surround it with spaces so that below I can correctly identify numbers
rule_nb_pattern = re.compile(r"\d+")

while any(map(str.isdigit, rule_0)):  # while there is at least one digit in the rule
    rule_numbers = set(rule_nb_pattern.findall(rule_0))  # take a set to go faster
    for nb in rule_numbers:
        rule = rules_dict.get(int(nb))
        rule_0 = re.sub(
            rf"(\D){nb}(\D)",
            rf"(\1){rule}(\2)" if "|" not in rule else rf"(\1)({rule})(\2)",
            rule_0,
        )


rule_0 = rule_0.replace(" ", "").replace("()", "").replace("()", "")
print(rule_0)


msg_validator = re.compile(rule_0)
print(sum(msg_validator.fullmatch(msg) is not None for msg in messages))

# part 2
INPUT = """44: 91 71 | 77 109
94: 15 77 | 129 91
73: 113 77 | 24 91
125: 77 38 | 91 37
25: 77 24 | 91 112
37: 105 77 | 50 91
47: 22 91 | 105 77
67: 91 109 | 77 45
130: 58 91 | 6 77
2: 19 77 | 10 91
48: 77 76 | 91 7
20: 10 91 | 65 77
65: 22 77 | 115 91
29: 77 126 | 91 79
105: 77 91 | 91 91
102: 87 77 | 114 91
38: 50 77 | 50 91
56: 91 107 | 77 106
9: 77 101 | 91 73
21: 77 72 | 91 54
35: 22 77 | 112 91
101: 91 115 | 77 34
122: 77 105 | 91 14
108: 77 111 | 91 52
66: 3 91 | 27 77
112: 91 28 | 77 91
61: 91 24 | 77 34
77: "a"
64: 77 99 | 91 119
106: 77 68 | 91 22
107: 24 77 | 113 91
39: 91 22
31: 53 91 | 127 77
8: 42 | 42 8
88: 34 91 | 113 77
27: 49 91 | 25 77
99: 91 87 | 77 58
10: 77 113 | 91 50
123: 91 100 | 77 68
1: 14 91 | 50 77
51: 112 91 | 34 77
42: 77 36 | 91 69
0: 8 11
76: 77 130 | 91 63
110: 91 100 | 77 124
46: 91 15 | 77 35
95: 120 91 | 23 77
50: 91 91
41: 28 4
57: 91 50 | 77 115
72: 91 46 | 77 125
30: 91 116 | 77 128
24: 28 77 | 91 91
109: 77 24 | 91 115
85: 91 113 | 77 68
87: 14 91
22: 91 77
45: 91 84 | 77 113
18: 77 12 | 91 20
98: 77 110 | 91 96
53: 77 92 | 91 90
120: 77 68 | 91 105
93: 77 115 | 91 34
126: 43 77 | 118 91
79: 77 47 | 91 83
89: 106 91 | 51 77
4: 68 91 | 105 77
62: 77 33 | 91 44
23: 91 115 | 77 113
32: 91 40 | 77 39
54: 59 91 | 74 77
52: 91 75 | 77 5
75: 77 104 | 91 15
104: 22 91 | 68 77
91: "b"
11: 42 31 | 42 11 31
90: 91 82 | 77 26
111: 117 91 | 41 77
63: 91 123 | 77 10
82: 89 91 | 80 77
6: 91 50 | 77 14
129: 84 28
55: 56 91 | 94 77
70: 77 93 | 91 88
58: 22 77 | 22 91
81: 22 77 | 68 91
3: 77 16 | 91 78
40: 34 91 | 84 77
36: 121 91 | 30 77
127: 91 21 | 77 48
115: 91 91 | 91 77
96: 77 97
71: 77 84 | 91 105
83: 22 77 | 100 91
118: 84 77
84: 28 77 | 77 91
43: 77 84 | 91 22
69: 77 60 | 91 108
68: 91 77 | 77 77
97: 77 77
100: 77 91
28: 77 | 91
113: 91 77 | 77 91
33: 77 61 | 91 103
5: 91 1 | 77 87
78: 34 91 | 97 77
74: 58 91 | 129 77
16: 14 77 | 84 91
26: 95 77 | 32 91
34: 28 28
92: 55 77 | 66 91
116: 77 102 | 91 70
7: 98 91 | 2 77
59: 61 91 | 17 77
121: 64 91 | 18 77
60: 91 29 | 77 62
12: 77 13 | 91 122
49: 124 28
124: 77 91 | 77 77
114: 77 115 | 91 24
80: 86 77 | 81 91
128: 67 77 | 9 91
86: 14 77 | 105 91
119: 77 85 | 91 4
14: 91 91 | 77 77
19: 91 68 | 77 34
15: 84 77 | 115 91
117: 73 77 | 57 91
103: 91 105 | 77 24
13: 91 14 | 77 50
17: 22 91 | 115 77

aabbbbbabaaaaabbbbabaabb
ababaabababaababbababaaa
aaaababaabbabbaabaaabaab
bbaababaabbababaabbbabab
baaabbbbabbabaabbababbba
ababbbaaaabaabbaabbbabbababbbabbbaabbbabaaaabaab
abbbabbbbbbbbabaaabaaaaabaabababaaabbaab
bbbbbbbbababbababaababaa
aabaabbabbbbaaaaaababaab
aababbabababbbbababaabaabaaababaabbbbabbaabbabaaabaaabab
bbbabbbaababbbaabaabbbba
bbabbbaaaaabaabbaababbba
abbabaababbaabaabaabbbabbabaababbabbaaaa
aabbabbaabababababaaaaab
baaaabbbbbaabbaaaabbbaba
abbaabaabbaabbbbbbbaaaba
aabbaaabaaaaaabaababbaab
abaaabbbabaabaabbbaaabbbbaababaabababbbb
abbbabaaabababbbabbaaabababbabaa
bbabaaabbaabaaaaabbbaabbabaabaab
abbbabaabbaabbababaabaaabababaaabbaabaaa
abaababababbabababaaaaaa
abbbabbbabbababbbbabbabababaaaaababaabbb
aabaababaabbaabaabaabbaa
aabaababbbaabbbabbabbaaa
aaabaaaaabbbabaaaaabbaab
aaaabbbabaabaabaabbbaabb
baaaaabbabbbbabbbabababb
abbababbbbbbbbbbbabababa
aabababababaaabaabaabbaa
bbbaabbbbbbaabbbabbabaaabbaaaaaa
bbabbaabbaabbaababbaabbbbababaabbaaabababbaaabbb
bbaaaabaababaabaabababaa
abbababbbbbbabababbbbaaabababbaaabbaabbaabbbabaaabaabaaa
bbaabbaabbbbbabaaaaabaab
babbaaabababbbabbaaabbaa
aaababbbbababaababbbaabb
baaaaababbabbbaaabbbabbbabaabaaa
babaaabaabbabbaaabbbaaaa
aabaaaaabaaaaaaabbaababbbaaaabbabaabababaababbbb
baaaaabbabaaabaababaaaaabbabbbbb
bbbbaaaaaabaabbababbabaa
abbaabaabbbbbbaabaaabbabbbbbbbaababbbbab
baaaabbabbabbbabaabbaabb
aababaaaaabaababbabbbbbb
baaabaaabbaaaabaababbabbbbababaabbaabbbababbbbbb
abababbbaabaabbabaababbabbbbababbbbbbaaaababbaaa
babbababaaababbbabaababbaababbaaabbabaaaaabbababbbbaaaaabaaabbba
aabbbbbaababbbaaabaababbabbabaaabbbabbbbbbabbaaaababbbbbabbbaaabaababbba
bbabbaaabaabaaabbaaabbaa
ababbbabaaabbababbabaabaaababbabbabbaabbbababbbbbbaaaaba
aababbababbbbaaaabaaaaab
bbbbabbbaaabbabbbbabaaababababbabbaaaaaaababaaabaaabbbaaababaaaababbabbaabaaaaab
abaababbbabbbbbbaaabbaabbbaaaaaa
baabbaaaabbabaaaaababbba
bbabbababbabbabbbaaaaaaabaabbbbbaabbababaaaababa
abbabaaaabaababaaaaababaabbababbbbaababaaabaabbbbabbbbbbbbbbabbbabbbaabb
abbabbabaaaaabaaaabbabbaaaaaabaabbabbbaabbbbabbaabbabababaabaababbbbbbbbabbbaaabbaaabbbb
bbaabbbbababbbbabbbbabba
abaabbabbaabbbabbbbaaaba
aaaaaababababbaaaabaabbaabbbaaaa
abaababababaaababbbbaaba
abaaabaaaaabaaabaabbbbaaababaabaaaabaaaaabbaabbabbbabbabaababbba
aabbbbbbabbabbbabbbbaaab
bbbbbaaaaabbbbabaabbaaabbabaabbb
abaaaabbbbbabbbbbbbababb
baababbbbaaaaabbbaaabbaa
abbbbbabbaaaabbbbbbabbaa
bbbaaabaabbbabababbaaaba
abbbbbbaabaabbabbbbbaabb
baababaaaabaabbbabbaaaaaaaaabaabbabbbbbbaababaaaabbababaababaaabaaabaabbaaaaaabaaaababab
bababaabbaababbabababbba
baaaaabbaabbaabaaaaaaaaa
babbaabaabbbbaabaabbbbbbaabbbbbaababaaaaaaabaaba
aababbabbaaababaaabbbaba
babaabaaabaabbabbabaababbbbbbbaabbaabaababaabaaabaabaaabbaabbbaa
aaaabababaaabaaabbabbaaa
bbbbbbaabbaabbbbbbbbaaaabbaaaabb
bbabbaabaaaaababbaabaabbbaababbababbaaabbaaabaababaaaaabbbbbbaababbaaaba
baaaabbbabbabaaabbbaabba
abaaaabbbaababbabbaabbbbabbbbbababaabaab
abbbbbbabaaaababaaabaabaaaabbbaa
aaabaaababbaabbbbaabaababbabaaaa
abbaabbabaabbabaabaabbbb
bbabbababbabaabbaaabbaabbbbaabbabbbbabbbaaabaaababbabbaabbbabbab
baaababbbbbbbaaababbbbbb
ababaababaabaabaaaaabbbb
baabaaaaabbbbbbabbaaaabb
aaabaababbbbaabaaaaaaaabaababaabababababbabbabaaabbaabba
abbabaaaaaaabaaabbbababb
aababbaabbababaababbaaab
abaabababbbabbbabbbbaaba
ababbbaaaabaaaaababbbaab
aabbbbaaaabaabbbbabbbaab
bbbabbbaaabaaaaaaababbaaabbabbabaabababbaabbbaba
abbbabaabbaabbbbbbaaaaaaaabbbbabbbaababbabbbbbbabaabbaba
ababababbaababbabbaaabab
bbbbababbbbabaabbbabababbbababbbabbababbbaababbb
aaabaaaabaababbaaaababbbbbbaaaaabaaaaaaababbabaaababaabababbabaaabaabbba
aaaaaababaaaaaabbbbbaabb
aaaaaabaabbabbbaaabaaaaabaabbbba
aabbbbbaaaaaaababaababaa
bbaaaabaabbaabbbabbaaabb
baabbaabbbbaaaabbabaabaa
baabaabaababbbbaabaaabbb
ababbabbaaabbbabaabbaabb
ababababababbbaaaabbaaaa
bbbaaaababbbaabaaaaabbaa
aaababbbbbbbbaaaabbabbbbbbaaaabbaababbba
bbbbbbbbbbabababaaabbbaa
bababbaaabaaaabbabbabbbb
aaaaabbabbabaabbbbbababaaaaababbababbaab
aabbabbabbaabbbbabaaaaab
bbaabaabaaababaababbbbbbaaaaabbaabaaaaaaabbbabaaabbabbbbbbabbbbb
aaaabbbabaabbabaaaabbaaabbabaabaaabababbbababaaa
baabbbbbabbbbababbbaaaba
abbabbaaabaababbbbbbbaaabbbbababbbbbaaab
abbbaababbabbabaaababaab
aababbababbaabbbbbababbb
baaaaabbbbbbabbbaaabaabbababbabbbbbaabab
aabbaaabbbbbbbbbaababbaaaaabaaba
abbbbaaabbbbababbbbbabbb
bbaabbbbbaaaabbbaaaabbbb
bbabbbbbbabbbbaaaaaaabbabababbaabbabbaabbabaabba
babaaabaaabbabbabbbaaabaaabaaababbbabaaa
baabaaaabbababbababbbbbaaababbba
aabbbbbabbabababaaaabaab
aaaaaabaabababababbbabab
babaababbaaaabbabbbabbab
ababbbaababaaaaaaabbabbb
bbaabbbbaabbbaaaabbbabbabaaaaabababbaabb
baaaaabaaabbbbabbababbbb
aabaaaaabaaaaaaaaabbbbbababbaabbaababbbabaabaaababbbabab
bbaaaabaabbbbaaabababbbb
aababbaababaababaabaabaa
aaaaaababbaaabaaaabaaabb
bbbabbbababbaabaaabbaababbaabbbbaababbba
aaabbbbaabbababbaababbbb
baabbbabbbaabbabbbbaabaabbbaaabbbbbaabaabaaabbaa
aabaababaaaaabbaaaaabbbb
baaaaaaaabbbbababbbbabaabbaaaababaaaaaaaaabbbbbabbbaababbbaabbabbbaaabbb
aabbbbaabaaababaaabaabbabbbbbabbbababbbb
babbaaabbbbbbaababbbabab
aabbbaaabaabababaabaabbbabbaaaabaabaababbabaabbabbabbbbbbabbabbaababbaaa
abbbabaaabbaaaabbabbabbb
aababaaaabaabbbababaababbaabaababaaabbbbaabababb
aaaabaaabbaabaabaabaababaaaaaaba
baaabbabbbaabbaaaababaab
aaaabbabbbbbbabaabbaaaababbbaabb
bbabaaabbbabbababbbabbbaaaabbaab
baaaaabaabbababbabaababbaabaaaab
babaaaabbabababbbbaaaabaabababaaaaabbbbbaaababbbabaaabaaababbaba
baaabbabbabbababbabbbbba
aaabbaaabbabaaabbbbbbaab
abbbbaaaaaaaabbabaabbbba
aabababaaaaabaaabbbaaaaa
aaaaaababaaaabbbbabbabaa
abaabaabbaaaaaababbbabba
baaabababaaaaaabbabaaabb
bbbbbababaaababbbbbaaaaa
aabaabbbbbaabababbbbabbb
bababaabbabaabaaabbbabba
bbbabbbabbabaababbbbaabb
aabbaababbbabaabbabbabbb
baababbaabbaaaabbabababaababbbbaaababaaaaaabbbab
abbbaababbaabababbbbaabb
bbbabbbabbbbababaabbabab
abbbbaababbbabaaaabbbbbbbbabbbabbabababbaaabbbaabbaaabba
abbbbaaabaababbbaaaaaaab
abababbbaabbbbabababbaab
babbabaabbababbbababbbbbababaaab
babbbbaaaabaababaaabbbbb
aaabbaaabbaababbabbbbbbaaabbbbaaaababababbbaabab
abaaaabbbabaabababbbbbbababaaaaaaabaaaab
aabbbbbaaabababaaaabbbbb
babbabaabbbaabababaaaaaa
bbbbbbaabbbabbbababbbbbb
aabbbbaabbabaabaabbbbbbaabaababa
babbaabbabbaabbaabaabbaababbabbbaababbbaaaababbbbabaabab
abbbbabbbabaaabaabbaabab
baabbababbaabbaaabababababbbbabaabbbbaabbabbabbbabbabbbb
abbababbabababaabbabbaabaaabaaaaabbbabaaababbbbbaaabbbbabbbbabbbbabbbbaa
abbaabbaababbbbababbaabb
abbaabbabaaaaabaaaaaabbabababbab
aabbabbabbaaabababaaabab
aabbbaaaaaababaaaaaaaaaa
bbbaaaababbaaabbbbaaabba
aabababaaabaabbababaabba
bbbbaaaababbababababbaaa
babbabbaabbbbbabbaabbbbbbabbaabb
abbbbbabaaaabaaaaaaaaaab
bbabbabababaaabaaababaab
baaaabbabbbbaaaababbaaaa
baaaaabaaabababaaababaab
abbaabaaabbbbaaabbabaaabaababbaaaaaabbbaabaaaabaaaaabbaa
babbbbaaaaaabbaaaabbbbbbaaaaaabbbbbbabaa
aababbaabaaaaaabbbbbaaaaabaaaaba
abbaabaaaabaabbbaaaaabab
abaabbabbaababbaabbaaaabbbaabbab
bbabbbabbabaaabaababbaab
baaabbabaabbaabaabababaa
bbbabbbabaabbbabbaaabbaa
bbbbbbbbabbaabbbababaaab
bbabababbbbbbbabbaaabaab
abbbaabaaaabbbbabbababbbaababbbb
bbababababbbbbbaabbbaaab
abbababaaabbbbabbababbbb
babbabaabaaabbaabbbbbabbbaaabbbbaabababa
abaaaabbaababaaabbbbbabaaabaaabbabbbbbaa
bbaaaababaaababbbbbbabba
abbaaaababbabaaababaabababaababaaabaabbbababaaab
bbaaabaabaaaaaaabaabaaab
babaabaaaaaaabaaabababaa
baabbbbbabbabababababbab
ababbbbbbbbbaaaabaababbababbbbbbaabaabbbbabaabba
babaaababaabaaaaaabbaaabbbaaababaaaaaaab
abbabbbabbbbabaaabaaabba
abbababbababbbbaabbaaaba
abbbabaaaaaaabaabbbaabab
abbabbaaabbbbbabaaabbaab
babbbabbbbbbbbabbbbbbbba
ababbbbaaabbbaaaaaababab
bbbabaabbaabbbabbbbbbbabbaabaaab
baaaaabbbaaaaabaabbaaaba
aabaabbabaaaaabbaaababbbbaabbababababbab
bbaaababbaabbbbbabaaabbb
aaaaabbaabbabbbaabbabbbb
aaabaabbbbabbbbbbababbaa
bbaabbaabaabbababbbbbbba
bababaabbbbaaaababababbbaaababbbbbbbbababaabbaabbabaabbb
abbbbaabaabbbbbbbbabbbaaaaababbbbaaaaaabbabbbaababbabbab
abbbbabaaaabbbbaabbabbbaabbbbaababbbbaababbaaaaaaabbaaaa
baababaaabaabaaabaababbabbaaaabbabaabbaababbbbbb
baabaabbabbabaaaaaabbaab
babbababaaaabbbbaabaabaababbaabbababaaab
aaabaaabbaababbabbaaabba
babaabababbbabbabbabbaaa
aaaaabaaabbaabbaabababaa
aabaaaaaabababbbaabaabaaabaabaaa
babbabbabaabbbabababaaaa
aabbbbbbabababbbabbaabbaabbababaabaaabbbbaabbabbbabbbbab
baaaaaaabbbabbbbbabbaabb
abaaaabbbaaabaaabbababababababba
abbaaaabbaabaaaaaabbaaaa
aaababbabababbbaabaabbabbababbaaaababbbabbbbabaa
aaaaaababbbbabaaabbbbaaababbbbba
babbabababbbbbbaaaabbbbababbbaab
abbaaaabaaabbbaabbbaaaaaaabaaaaabbbbbbabbaabbbaaaaabbabaaabbaaba
baabaababaabbbbbbaabaaaa
baaababbbaabaaaabbbbabba
bbabbabaaaaaabbaaaababab
abbaabaabbabbbababaaabbb
baabaaaaabbbabaaababaaaaababbabaaababaabaabaaaab
bbbbabaaaaabaaabaabbabaa
abbbaabaabaabaaaabaaababaabbabaabaabbabaababbbaaabaaabbb
bbaabbbaababbbbababaaabaaaabaababbabbaaaaaabbbaaaaabaaabaababbbbaaabbbbb
aaababaaabbaabbbababaabb
abbbbabababbbbaaaababbababbabaaaaaababbbbaaabbab
baabaabaaabaababbbbbabba
bbabbbbbabbbabbbbbaabaaa
bbbbababbbabbababbabaaaa
abaaabaabbbaaaabaaaabaab
abbbbabaababbababbbbabbb
aabaaaaabbbbaaaabaabbabaaaaababb
abbababbbbabbababababbba
aaabbababaaaabbabaabbbbbbaabaaabbbaaaaaa
aabbaaabaaabaabababababaabbaabbaaabbababababbaabbbbbaabbbbbabaaaabbaaaababbabaabaabbbbaa
abbabbbaaabbaaabbbbbaaab
bbbbbaaababaababbabbaabbbbbabababaaaabab
abaabbbabbaaaabababbabbaabaabbaa
baaaabbababaababbbbaaabb
bbbaaabbbaaaaaaaabababababbaaaabbbaababbbabababa
babaaabaabaabbbaabbabbbb
aabbbbbbabaabbbaaabaaaaaaabbbbbabbabbbabbaaabbaa
bbaabababbaaaabaabaaabbb
aabbabaabbbbbabbbaabaaabababbbbbabbbaaaa
aaabaaaaabaabbbaabaaaaab
baabaabbaaabbababaababaa
bbbaaaabbabaaaabbababbbb
aabbbbabbabbabbaaaaababb
abaabbbabaabaabaabababbbababbbabbaaaaaab
abbbabaaabbabbaaaabbaaaa
aaaabababbbbabaaabbbaabaabbababbabbbabababaaababbbaaabbb
aaaaabaabaabbaaababaaabb
abababbbbbaabbaaababaaab
bbabbbaaaabbabbaabbbbabbaaaabbbaaabbababbbbabbaa
aababbaabaaabbbbbabababb
bbaababbaaaabbbaabbbbabababbaababbbbbaaa
babaaaaaaaabaaababbabbbb
bbbbabaabbbbaaaaaabbaabb
ababaabaaabbabbabbbaababababbbaaaabbaaabbbbbbbaa
bbabbababbbbababbbbaabba
bbbabaaabbbabbaaaababbba
baaababbababbbbaababbaaa
abaabbbababaababbbaababaaaaabababbbaaaabbbbbababaaaaaabbaaabbaab
babbbbabaabbbbbbaabababbbaabbbbbbabaaaaababaaaabaabbbabababaaaaaabbabbaabbaaaaab
ababaaabbbabbbaaabbabbabaaabbaab
bbabbbbbaababaaababaabba
aabaabbbbbbabaabaababbabbbaabbba
abbabaabbabbbbaaaaabbabababbbaab
baaaabaabaaaabbbbaaaaaabbbbaabab
aaabbbbaaabbaaabbbaaaaab
babaabaaabbaabaabaaabaab
baabbbbbbbbbababaaaababababaabbb
baaabaaaaaabbaabaaababbbbaaabbbbaaabbbbb
aaaaabaaabbababaaaaaabababbaaaaaaabbbaaabbbaaabbaaaaabaaaaabbaba
baaaaaabbaaaaabaaaaabaab
ababbbbaababbabbabaabbaa
abbbbaabbababaabbbabababababbbaaabaaabab
abbbbabaaaabaaabaaababab
abbabaaabaaaabbbabaababb
baabaaaabbbbbbababaabbbb
aabbbaaaaabbaabaabbbbaaabbbbbabababbabaabbbbabbabbbbaabb
baabaababbbbaaaaaabaababaabaababaabaabbaaababbaaaabbabaa
bbaabbaabbbbabaaaaababbbbababbba
abbbabaaabababbbbbaaaaaa
abbababbabbababaaaabababbbaaaaabbbbbaabbaababbbbaaabbaab
abbabbaabaaababbbabbbbba
aabaabbabaaabbbbbbabbabb
bbbbaaaaababaabaaabaaabb
abaaababbabbbbbabbbbbabaababababababababbaabbbbbbababaabbbbbbababaaaabbaabaaabbb
abbbabbabbbabaabbababbba
baabaaababaaababbabbbbbbaabbaababbaaabaabbbababaabaaaabb
baaababbabbabbaaaabbbbaaababbabbbbaababbabaabaaa
babaaaaaababbababbabaaaa
babbabbabbaababaaaaabaab
bbaabbbbaabbaaababbbbbbabababaaa
baaaaabbbabaaaabaaababba
bbbaaaababbababbabbbabab
bbaabaabababbabbbbbbabbb
aabbbbaaabaabbabaaaaabbaaaabaaababbaaaba
ababaabaaababababbabbbabbbbbbbaababaabbbabaaababbabbaaab
bbbabbbabaabbabaaabbaaaa
bbabbabaabbbabbbbbbbaabb
baaaaabbbbbbbabaaabaabbbbbbbbbbbabbabbbaabaabbaa
aaabaaaaababbabaaaababab
baabaabaaaaaaabaaabbbbababbbaababbaabbababbaababbabababa
abbbabbaaaabbaaabbbaabaa
bbbbababbbaabbaaaaaaaaab
aabbaaabbbbabbbaabbbbabababaabbb
bbaabababaabbaabbababbab
abbabababbbbababbaaaaabbbbbaabaa
babaabbbaaabbaaabbabbabbaaabbbbabbbaabbbababaaabbaababaa
abaaaabbababababbabababb
baaaaababababbaababbbaab
aabaaaaaaabaabbabbaabbba
baaaabaabaabaabbaababbabbabaabbaaababbbbbbbaaababbabaabb
aaaaabbabbbaaaabbabbbabbaaababba
baaaaababaabbaabbbabbaab
abbbabbbaaababaaabaaabab
aaabbbababbababbababbbab
baaaaaaaaaaaaabaabababaa
aaabbaaaaababbbbabbbaaaaabbbbbbabaaabbabaaabbbbaabbabaaa
abbaabbbabbabaabbbbababb
baaaaaaaaaabbaaaaabbbaab
abbaabbabaaaaaaaabaaaabbaabbbaababbbbbaa
bbabababaaabaaabbbabaabaabbbbbabaaaaaabb
babbabbaabaababbbbbbbbbbbbabaaaa
babbbbaabbbbabaaabaabaab
bbbabaababbbabbabaaabbbbbbaabaabbababbba
bbababaabaaaabaaabaababbbababaaa
bbbbbaaabaabbabaaaaabaaaaabaaaab
abbbaababbbbabababbaabbbbbabbaab
abababababbabbbababbaabaaabaabaabaaaabab
aaababbbbbabababbaaabababaaabbababbaababbbaabbab
abaaabaaababababbabbaaaa
aaababbbaabbaababbaaaaaa
abababbbbbaabaabbbabbaaa
baabbabaabbababbbbaabaabbbbaabbaaaaabbaa
aababbaabaaababbababaaab
abaabbabaaaaabbaababaaab
aaaaaababaaabbabaaabbaab
aabbbaaabababbbabbaaaabaabbbbbabbbbbbaaaaababbaaaabaabaaabbbaaaabbbbbaabbbaabaaa
aabaabbabaaababaababaaab
baaabababaabbbbbababbbbb
abaaabaaabbababbabbbbbbababbabbb
ababababbaabaabaabbbbabbababbbaabbbbbabbaaaabbbb
babbaabaaaabaabbbbbaaaabaabababaabaabaaa
aaabbabaabbaabbababbbaba
ababbabaaabbbbabbbbabbaa
aaaaabaaaaabaabbbbabaabaabbabbbaaaaabbaababbbabababaabbb
bbbbbaaabbabbbbbabbbaaab
bbbbbabbbabbaaaaaababbbbaaaaabababbbbabbbbabbbaaaaababab
baaabbaaababababababbbbababababbabaabaabbabbaabaaaababbb
baabbabaaaabbbbbaabbbaba
ababbbbabaaabababbbbbaaaabbbbbababaaabab
baaaaabbabaababaabbbabab
abbabbbabaababbbaabababb
aaabaabbbbbabaabbbbaabba
aaabbbabababbabaabababba
bbbbbbabbaaababbbbabbbbbbabaaaabbaaabaab
aaaaaabbbabababaaabbbabb
baabaabbaabbbaaabbaaaaaa
bbababaaabbbbaabbabbbbbb
bababaabaaabaaabbbbbaaba
bbbabbbbbabaaaabaaabbbabaabaaaaabababbba
aaabaabbabaababbbbbbbaab
bbbababbabaabaabababbbabbbabbbabbbbaaaaabbbabbbabababbba
aabbbbababbabbbaaababbbbbaabababaabaaabbbabbbbbbabbabbbaabbaabbb
abbaaaabbaaaabaabaabaaab
baabbabaababbabbbbabaabb
bbbbababbaabbababbaabaaa
abbbbaaabaaaabbbbbabbbbbaaaabbaa
abbabababaaaabaaabababbbabaabbabbbbbaabbbaabbabb
baabaaaaaababababbaaaaaa
abbaabaabbbbbabaaabaaaab
aabaababbbbbbaaabbaaababbbaaababaabbaaaa
aabbaaabaabbaabaaaaabbbb
bbabaaabaababaaaabbbabbaababbbbb
aaaabbbaababbbbaabbbbbabbbaabbab
abbaabaaabbabababaabbaabaaababaaababbbbb
bbabbaaababbaabbbaaabbaabbaaaaaababaaabbabbabbabbaaaabbb
aabbbbabaaaaaabaaabaaabb
baabaabababbababbbaaabababaabbaababbaaaa
bbbabbbbabaabababaabbbbbaaababaabbabbababbabbaababaaabbbaababaab
bbbaabaaabbabbbbabaabbaaaabaaaaaaaabaaabaabbbababbaaaababaabaaba
ababbababbabbbbbabbaaaaa
babbbbaabbaabababbaabbba
abbaabbbbbabbbaaabbabaabbabbaabaababbabbaababbaaabaaabbaaaaaababaabbabab
ababaababbabaabbbbabaaabbbabababbababbab
aababaaaaaaaabbabbbbbbbbbbaaabba
bbaabbbbbbaababaabaabaaa
bbbaabbbaaaabbabaababaab
bbabababababbbbaabaaabab
aaabbabaabbaabbbaabababb
ababababbaabbaaababbaabb
bbbbaaaabaaaaabbaabaabbabaabbabaabaabbbabbabbbbabbababbbbbbbabba
abbbabbbbbabbbaababaabbb
aabbaaabbbaababaababaababbbabbbabababaaabbaaabbb
abbbabaabbbaaaabaaababaabbbabaabbaababbabaabaabbabaabaabbabbaaabaababbba
abbabbaaaaabbbbababbbbba
aabbabbababaabaabbabaababbbabaabaababbaa
abbbbbabaaabbaaabbbaabaa
"""

inp = [e.replace('"', "") for e in INPUT.split("\n") if e]  # drop the " in "a" and "b"
rules = [row for row in inp if row[0].isdigit()]
rules_dict = {
    int(e[: e.index(":")].strip()): e[e.index(":") + 1 :].strip() for e in rules
}
messages = [row for row in inp if row[0].isalpha()]

rule_0 = (
    " " + rules_dict.get(0) + " "
)  # surround it with spaces so that below I can correctly identify numbers
rule_nb_pattern = re.compile(r"\d+")

for _ in range(15): # this is my dirty solution: write down how many iterations we needed in part 1's while loop and incrementally 
# increase it until we get the right answer (to do it a bit cleaner you can look at the longest words with subsequence aaa.aa or bb.bbb))  
    rule_numbers = set(rule_nb_pattern.findall(rule_0))  # take a set to go faster
    for nb in rule_numbers:
        rule = rules_dict.get(int(nb))
        rule_0 = re.sub(
            rf"(\D){nb}(\D)",
            rf"(\1){rule}(\2)" if "|" not in rule else rf"(\1)({rule})(\2)",
            rule_0,
        )


rule_0 = rule_0.replace(" ", "").replace("()", "").replace("()", "")
print(rule_0)


msg_validator = re.compile(rule_0)
print(sum(msg_validator.fullmatch(msg) is not None for msg in messages))
