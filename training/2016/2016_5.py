import hashlib

INPUT = 'wtnhxymk'


password = ''
i = 0

# while len(password) < 8:
#     trial = INPUT + str(i)
#     md5_hash = hashlib.md5()
#     md5_hash.update(bytes(trial, 'ascii'))
#     if (hash := md5_hash.hexdigest()).startswith('00000'):
#         password += hash[5]
#         print(password)
#     i += 1

# part 2
password = ['_'] * 8
i = 0

valid_pos = ('0','1','2','3','4','5','6','7')
while '_' in password:
    trial = INPUT + str(i)
    md5_hash = hashlib.md5()
    md5_hash.update(bytes(trial, 'ascii'))
    hash = md5_hash.hexdigest()
    if hash.startswith('00000') and hash[5] in valid_pos and password[(ind := int(hash[5]))] == '_':
        password[ind] = hash[6]
        print(''.join(password))
    i += 1