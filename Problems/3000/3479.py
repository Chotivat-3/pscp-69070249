'''Taro'''
pick = input().lower()

boxhead = {'a':'Ace', 'j':'Jack', 'q':'Queen', 'k':'King'}
boxbot = {'d':'Diamonds', 'h':'Hearts', 's':'Spades', 'c':'Clubs'}

if pick[0].isdigit():
    if pick[:2].isdigit():
        print(pick[:2], end=" ")
    else:
        print(pick[0], end=" ")
else:
    print(boxhead[pick[0]], end=" ")
print('of', boxbot[pick[-1]])
