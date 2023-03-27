def look_and_say(nb: str):
    blocks = []
    while nb != '':
        n = nb[0]
        for i in range(1, len(nb)):
            if nb[i] != nb[0]:
                blocks.append(nb[:i])
                nb = nb[i:]
                break
        if len(nb) == 1:
            blocks.append(nb)
            break
    lens = [str(len(block)) for block in blocks]
    blocks = [block[0] for block in blocks]
    answer = ''
    for item in zip(lens, blocks):
        answer += item[0] + item[1]
    return answer
    
a='1113222113'  

for i in range(50):
    a = look_and_say(a)
print(len(a))