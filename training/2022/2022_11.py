import re
from operator import add, sub, mul, truediv
import math
from tqdm import tqdm

INPUT = """Monkey 0:
	Starting items: 98, 97, 98, 55, 56, 72
	Operation: new = old * 13
	Test: divisible by 11
		If true: throw to monkey 4
		If false: throw to monkey 7

Monkey 1:
	Starting items: 73, 99, 55, 54, 88, 50, 55
	Operation: new = old + 4
	Test: divisible by 17
		If true: throw to monkey 2
		If false: throw to monkey 6

Monkey 2:
	Starting items: 67, 98
	Operation: new = old * 11
	Test: divisible by 5
		If true: throw to monkey 6
		If false: throw to monkey 5

Monkey 3:
	Starting items: 82, 91, 92, 53, 99
	Operation: new = old + 8
	Test: divisible by 13
		If true: throw to monkey 1
		If false: throw to monkey 2

Monkey 4:
	Starting items: 52, 62, 94, 96, 52, 87, 53, 60
	Operation: new = old * old
	Test: divisible by 19
		If true: throw to monkey 3
		If false: throw to monkey 1

Monkey 5:
	Starting items: 94, 80, 84, 79
	Operation: new = old + 5
	Test: divisible by 2
		If true: throw to monkey 7
		If false: throw to monkey 0

Monkey 6:
	Starting items: 89
	Operation: new = old + 1
	Test: divisible by 3
		If true: throw to monkey 0
		If false: throw to monkey 5

Monkey 7:
	Starting items: 70, 59, 63
	Operation: new = old + 3
	Test: divisible by 7
		If true: throw to monkey 4
		If false: throw to monkey 3
"""

NB_MONKEYS = INPUT.count("Monkey")
ITEMS_PAT = re.compile("Starting items:\s(\d.*\d)")
OPERATION_PAT = re.compile(r"Operation: new = old ([\+\-\*\/]) (.*)")
TEST_PAT = re.compile("Test: divisible by (\d+)")
RECIPIENT_PAT = re.compile("If.*?(\d+)")
NB_ROUNDS = 20
# step 1: preparing the simulation of a round (move to utils.py in real life)

# extract the monkey starting items
monkey_items = dict(
    zip(
        range(NB_MONKEYS),
        [list(map(int, item.split(","))) for item in ITEMS_PAT.findall(INPUT)],
    )
)

# extract the monkey-specific "operations" (assuming an operation has only one operator, like - + / or *)
MONKEY_OPERATIONS = {}
operation_dict = {"+": add, "*": mul, "-": sub, "/": truediv}
MONKEY_OPERATORS = dict(enumerate([elem[0] for elem in OPERATION_PAT.findall(INPUT)]))
for monkey_ind, operation in enumerate(OPERATION_PAT.findall(INPUT)):
    op, nb = operation
    # assert op in operation_dict
    monkey_func = lambda x, op=op, nb=nb: operation_dict[op](
        x,
        (
            int(nb) if nb.isdigit() else x
        ),  # the else case if the case where second argument is <old> itself, e.g. old + old
    )  # here initially I didn't use the kwargs in my lambda function and <MONKEY_OPERATIONS> ended up containing 4 times the exact same lambda function.
    # Why? Because <nb> and <op> kept being overriden at each iteration of the for loop (see here: https://stackoverflow.com/questions/32595586/in-python-why-do-lambdas-in-list-comprehensions-overwrite-themselves-in-retrosp)
    MONKEY_OPERATIONS[monkey_ind] = monkey_func

# extract the monkey-specific tests
MONKEY_TESTS = dict(zip(range(NB_MONKEYS), map(int, TEST_PAT.findall(INPUT))))

# extract the recipient monkeys indices
recipients = map(int, RECIPIENT_PAT.findall(INPUT))
MONKEY_RECIPIENTS = {
    monkey_ind: [next(recipients), next(recipients)][::-1]
    for monkey_ind in range(NB_MONKEYS)
}
# I reverse the values of the above dict (with [::-1]) because I want to use boolean indexing and true evaluates to index 1; false to index 0

# store the number of times each monkey inspects an item
monkey_nb_inspections = {monkey_ind: 0 for monkey_ind in range(NB_MONKEYS)}

# uncomment the below block to run solution to part 1
# step 2 : simulate. Thanks to the pre-processing above, this is fairly straightforward
# for _ in range(NB_ROUNDS):
#     for monkey_ind in range(NB_MONKEYS):
#         for item_ind in range(len(monkey_items[monkey_ind])):
#             item = monkey_items[monkey_ind][item_ind]
#             item = MONKEY_OPERATIONS[monkey_ind](item) // 3
#             monkey_items[
#                 MONKEY_RECIPIENTS[monkey_ind][item % MONKEY_TESTS[monkey_ind] == 0]
#             ].append(item) # send item to the right monkey, notice the use of boolean indexing in Python!
#             monkey_nb_inspections[monkey_ind] += 1
#         monkey_items[monkey_ind] = [] # empty the current monkey's bag of items

# print(math.prod(sorted(monkey_nb_inspections.values())[-2:]))

# part 2
NB_ROUNDS = 10_000
# I can't reuse my code from part 1 as it is not efficient enough
# it seems to me that the bottleneck comes from the management of the worry levels getting really high
# I notice that the multiplications do not actually change the divisibility of the items, so I can skip them
BIG_DENOM = math.prod(MONKEY_TESTS.values())

for _ in tqdm(range(NB_ROUNDS)):
    for monkey_ind in range(NB_MONKEYS):
        monkey_multiplies = MONKEY_OPERATORS[monkey_ind] == "*"
        for item_ind in range(len(monkey_items[monkey_ind])):
            item = monkey_items[monkey_ind][item_ind]
            item = (
                MONKEY_OPERATIONS[monkey_ind](item) % BIG_DENOM
            )  # the modulo is the key to being efficient here in part 2
            monkey_items[
                MONKEY_RECIPIENTS[monkey_ind][item % MONKEY_TESTS[monkey_ind] == 0]
            ].append(
                item
            )  # send item to the right monkey, notice the use of boolean indexing in Python!
            monkey_nb_inspections[monkey_ind] += 1
        monkey_items[monkey_ind] = []  # empty the current monkey's bag of items

print(math.prod(sorted(monkey_nb_inspections.values())[-2:]))
