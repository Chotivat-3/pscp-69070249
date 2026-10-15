'''imposter'''
from json import loads
def vote():
    '''vote'''
    player = {}
    who_out = {}
    while True:
        myplay = input()
        if myplay == 'Start':
            break
        player.update(loads(myplay))
    while True :
        myvote = input()
        if myvote == 'End':
            break
        myvote = {myvote:player.pop(myvote)}
        who_out.update(myvote)
    keywho = list(who_out.keys())
    keywho.sort()
    keyplay = list(player.keys())
    keyplay.sort()
    print(list(player.values()).count('Impostor'),"Impostor Remains")
    print('***Alive***')
    for i in keyplay:
        print(i,':',player[i])
    print('***Dead***')
    for i in keywho:
        print(i,':',who_out[i])
vote()
