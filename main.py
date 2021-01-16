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
        if len(arg) == 3:
            ogmessage = arg[1].lower()
            wbool = False
        #enfiles
        elif len(arg) == 4:
            if arg[3] == 'file':
                with open(arg[1]+'.txt', 'r') as file:
                    ogmessage = file.read()
                open('e'+arg[1]+'.txt', 'x')
                wbool = True

        with open(arg[2]+'.txt', 'r') as file:
            keysep = file.read().split('\n')
        for i in ogmessage:
            for r in keysep:
                if r.startswith(i):
                    if wbool == False:
                        emessage = emessage + r[2:]
                        break
                    elif wbool == True:
                        with open('e'+arg[1]+'.txt', 'a') as file:
                            file.write(r[2:])
                            break
            else:
                if wbool == True:
                    with open('e'+arg[1]+'.txt', 'a') as file:
                        file.write(i)
                elif wbool == False:
                    emessage = emessage + i
                continue
        if wbool == False:
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
