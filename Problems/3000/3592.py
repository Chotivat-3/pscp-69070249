'''ally'''

n = int(input())
k = input()
w = input()

if k == 'left':
    print(f"{w}"+" "*(n-len(w)))
elif k == 'right':
    print(" "*(n-len(w))+f"{w}")
elif (n-len(w))%2:
    print(" "*((n-len(w))//2)+" "+f"{w}"+" "*((n-len(w))//2))
else:
    print(" "*((n-len(w))//2)+f"{w}"+" "*((n-len(w))//2))
