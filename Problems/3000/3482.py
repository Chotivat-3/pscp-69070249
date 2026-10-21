'''MAMI POKO WHAT A DEMON HUH?'''
demon = {'Spider Demon': 1, 'Swamp Demon': 2, 'Arrow Demon': 1,
         'Hand Demon': 2, 'Drum Demon': 3,  'Mugen Train': 2, 'Upper Moon': 3}
keydemo = list(demon.keys())
turn = 0
kill = 0

run = 0

while True:
    if kill == 5 :
        print(turn)
        break
    win = False
    for _ in range(2):
        act = int(input())
        turn += 1
        if act == demon[keydemo[run]]:
            win = True
            break
    print(keydemo[run])
    if win :
        kill += 1
        print('kill')
    else:
        keydemo.append(keydemo[run])
        print('back')

    run += 1
