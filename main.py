import string
import random
char = list(string.ascii_lowercase)
for i in range(1,10):
    char.append(str(i))
while True:
    req = input()

    #make new key
    if req.startswith('newkey'):
        arg = req.split('-')
        newf = arg[1]+'.txt'
        open(newf,'x')
        codel = arg[2]
        with open(newf,'a') as file:
            file.write(codel)
            for i in char:
                file.write('\n' + i + ' ')
                for i in range(int(codel)):
                    file.write(random.choice(char))
        print('done')
    #encrypt
    if req.startswith('encrypt'):
        arg = req.split('-')
        emessage = ''
        ogmessage = arg[1].lower()
        with open(arg[2]+'.txt', 'r') as file:
            keysep = file.read().split('\n')
        for i in ogmessage:
            for r in keysep:
                if r.startswith(i):
                    emessage = emessage + r[2:]
                    break
            else:
                emessage = emessage + i
                continue
        print(emessage)








        