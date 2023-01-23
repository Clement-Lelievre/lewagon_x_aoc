# thanks to anthonywritescode for this one! (I'm sick and cannot think clearly)

from collections import defaultdict

def compute(s: str) -> int:
    edges = defaultdict(set)
    for line in s.splitlines():
        src, dst = line.split('-')
        edges[src].add(dst)
        edges[dst].add(src)

    done = set()

    todo: list[tuple[str, ...]] = [('start',)]
    while todo:
        path = todo.pop()
        if path[-1] == 'end':
            done.add(path)
            continue

        for choice in edges[path[-1]]:
            if choice.isupper() or choice not in path:
                todo.append((*path, choice))

    return len(done)

INPUT = '''\
start-YY
av-rz
rz-VH
fh-av
end-fh
sk-gp
ae-av
YY-gp
end-VH
CF-qz
qz-end
qz-VG
start-gp
VG-sk
rz-YY
VH-sk
rz-gp
VH-av
VH-fh
sk-rz
YY-sk
av-gp
rz-qz
VG-start
sk-fh
VG-av
'''
#print(compute(INPUT))

# part 2
def compute(s: str) -> int:
    edges = defaultdict(set)
    for line in s.splitlines():
        src, dst = line.split('-')
        edges[src].add(dst)
        edges[dst].add(src)

    done = set()

    todo: list[tuple[tuple[str, ...], bool]] = [(('start',), False)]
    while todo:
        path, double_small = todo.pop()
        if path[-1] == 'end':
            done.add(path)
            continue

        for choice in edges[path[-1]] - {'start'}:
            if choice.isupper():
                todo.append(((*path, choice), double_small))
            elif double_small is False and path.count(choice) == 1:
                todo.append(((*path, choice), True))
            elif choice not in path:
                todo.append(((*path, choice), double_small))

    return len(done)

print(compute(INPUT))
