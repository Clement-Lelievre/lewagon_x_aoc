"""https://adventofcode.com/2024/day/1"""

with open("day1_input.txt", "r") as f:
    inp = f.read()
s = [r for r in inp.splitlines() if r.strip()]
a, b = [], []
for e in s:
    r, t = e.split()
    a.append(int(r))
    b.append(int(t))

print(f"part 1: {sum(abs(a-b) for (a,b) in zip(sorted(a),sorted(b)))}")

# part 2

ans = 0
for elem in a:
    ans += b.count(elem) * elem
print(f"part  2: {ans}")
