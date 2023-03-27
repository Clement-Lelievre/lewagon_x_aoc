import hashlib

str2hash = 'iwrupvqb'
nb = 0

while True:
    if hashlib.md5((str2hash + str(nb)).encode()).hexdigest()[:6] == '000000':
        print(nb)
        break
    nb += 1
