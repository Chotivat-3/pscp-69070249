"""PICKME?"""
x = list(map(int,input().split()))
x.reverse()
out = False
for i in x:
    if not i%3 or not i%5 :
        print(i)
        out = True
if not out:
    print("Nope")
