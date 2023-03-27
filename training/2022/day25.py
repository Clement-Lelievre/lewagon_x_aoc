from itertools import product

INPUT = """20-==1==1212==2=
1=022102-=02=1=11
2110--=1011=
1--21=-11=2-01
1==
211--11-11001=120==
122---0-
1120020-1
1-=-0
2=-022=-110-1=020
20
21222101-
2-0-=1=0
2=0==
2=1200=0==
101211=1
100=2=0-=--20
221
1=2-22=-1-1=1-1
1-121-=1-
1-2=0=2==11=00
2=2-2==
10-0-001--==0=0
2011-1-01=22=0-
1-1=
1-=21=-111=0-
2=101212=0212=-122
12-1==0
10-122
1=1=-=
1002
112-
1-120
1--10==0-122=
1=-1
1-0===-0===01=1===
10=---=-02=1--=2-20
220-=-210
1110-0-2212
1-0--00
12-01----=0--=2-1
10202=121-0=0
2200=-022-1-=0200-=
10
10=0-20210-1-0-101
120-110=1012220=-
21
1-=----2-21-12200-
1-0121=
1-21201
1--2111200-=200
2-02=120-02
10=-011
1220
1-0-12
1--2122=2201
1=1=111-0=
1=-=1-0-=-12
1=11=20=1=12
1==01-=1222
10-210012
2=-=
1=21-2--
1-2-0010
2=-0-=11-=01-=122
1=02
2=-11
1-11---1100
11=21
1--=20==-1-0==01
1-212==2=-2-=
12=22-0012-=0-11
1==--0-==2-11
2-100=02-0-==10
1=0221
10111=00-=0=0=1
2==2-1
12-=1=0===0=-02
1-11-=-001212=
20=22
1=-112--2=020-
1=2=-0=22121===00
2-002221==1
101=022-12-=21-202
1=1
102=0121=2=01==1=
2===2-
10==-0=01-0-1-0-=1
2212
1==-10=220-22
22
1--2-=0
1-12==-1=0
2---=-=
11-=
1=
2=1==10=-=2-
12==--
21==-212=22-=
1=110=1--11
1=1==-01220
12==10--201
1--0011-210
1120-1--0
202--=0=2==1121
1===
1=00=2
1-10-=1=-=0002
10-11-21-1
1=01=111-
2--
110=02-1-221-=
20112102=0--0
1=0==222111-2220-1
2-0=10
1-=0=2=2=-=02121=2
11-2=---2
1=2
21-0=
2=-12=001--0
2-0
"""

# INPUT = """1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122"""

snafu_conversion = {"-": -1, "=": -2, "2": 2, "1": 1, "0": 0}


def snafu_to_decimal(snafu: str) -> int:
    snafu = snafu[::-1]
    dec = 0
    for i in range(len(snafu)):
        dec += snafu_conversion[snafu[i]] * 5**i
    return dec


def decimal_to_base_5(nb: int) -> str:
    result = ""
    while nb > 0:
        result = str(nb % 5) + result
        nb //= 5
    return result


def max_digit_below_2(number: int | str) -> bool:
    """Returns whether the base 5 representation corresponding to the `number` does not use a digit larger than 2
    meaning it is only made up of 0s, 1s, or 2s

    Args:
        number (int): the number in decimal representation

    Returns:
        bool: _description_
    """
    return max(map(int, set(decimal_to_base_5(number)))) <= 2


all_snafus_sum = sum(
    snafu_to_decimal(snafu) for snafu in INPUT.splitlines() if snafu.strip()
)
base5_sum = decimal_to_base_5(all_snafus_sum)
print(all_snafus_sum, base5_sum)


if max_digit_below_2(
    all_snafus_sum
):  # very unlikely else there's no point in the challenge
    print(all_snafus_sum)
else:
    first_three = e if (e := base5_sum.find("3")) != -1 else 10**10
    first_four = e if (e := base5_sum.find("4")) != -1 else 10**10
    first_forbidden_digit_ind = min(first_three, first_four)
    print(f"{first_forbidden_digit_ind=}")
    if first_forbidden_digit_ind == 0 or set(
        base5_sum[:first_forbidden_digit_ind]
    ) == set(["2"]):
        start_number = snafu_to_decimal("1" + "0" * len(base5_sum))
    else:
        before = base5_sum[:first_forbidden_digit_ind]
        last_zero_ind = e if (e := before[::-1].find("0")) != -1 else 10**10
        last_one_ind = e if (e := before[::-1].find("1")) != -1 else 10**10
        last_one_or_zero_ind = len(before) - min(last_one_ind, last_zero_ind) - 1
        print(f"{last_one_or_zero_ind=}")
        start_number_base5 = (
            before[:last_one_or_zero_ind]
            + str(int(before[last_one_or_zero_ind]) + 1)
            + "0" * len(base5_sum[last_one_or_zero_ind + 1 :])
        )
        start_number = snafu_to_decimal(start_number_base5)
    print(f"{start_number=}", decimal_to_base_5(start_number))

    init_part = before[:last_one_or_zero_ind] + str(
        int(before[last_one_or_zero_ind]) + 1
    )
    # while not (max_digit_below_2(current_nb) and max_digit_below_2(current_nb-all_snafus_sum)):
    #     current_nb += 1
    for prod_ in product(*[(0, 1, 2)] * (len(start_number_base5) - len(init_part))):
        current_nb = snafu_to_decimal(init_part + "".join(map(str, prod_))[::-1])
        if max_digit_below_2(current_nb - all_snafus_sum):
            break


a = decimal_to_base_5(current_nb)
diff_base5 = decimal_to_base_5(current_nb - all_snafus_sum)
print(a, diff_base5)
a = list(a)
for i in range(len(a) - len(diff_base5), len(a)):
    if (elem := diff_base5[i - len(a) + len(diff_base5)]) in ("1", "2"):
        a[i] = "-" if elem == "1" else "="

answer = "".join(a)
print(answer)


# part 2
