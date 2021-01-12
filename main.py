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
    #decrypt
    if req.startswith('decrypt'):
        arg = req.split('-')
        with open(arg[2]+'.txt', 'r') as file:
            keysep = file.read().split('\n')
        dmessage = ''
        ogmessage = arg[1]
        codel = keysep[0]
        going = True
        while going:
            if len(ogmessage) >= 1:
                if ogmessage[0] not in char:
                    dmessage += ogmessage[0]
                    ogmessage = ogmessage[1:]
                else:
                    vcode = ogmessage[:int(codel)]
                    ogmessage = ogmessage[int(codel):]
                    for i in keysep:
                        if i.endswith(vcode):
                            dmessage += i[0]
            else:
                going = False
        print(dmessage)








        