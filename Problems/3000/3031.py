"""INK"""
pit = input().split(" ")
S = int(pit[0])
N = int(pit[1])
PI = 3.1416
def cal (n=N,s=S,pi=PI):
    """cal"""
    r = s/pi
    time = 0
    while n :
        home = input().split(" ")
        x = int(home[0])
        y = int(home[1])
        x = x**2
        y = y**2
        dis = x+y
        time = dis//r
        if dis%r:
            time += 1
        print(f"{time:.0f}")
        home.clear()
        n -= 1
cal()
