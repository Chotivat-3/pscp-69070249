''' Flowers Boy '''

l, n = map(int,input().split())

t = 0
while True:### อันนี้คือสูตร sn = n/2(an+a1)
    bay = (l*(t+1)/2)*(l*(t+1)+1)
    t += 1
    if bay >= n:
        print(t)
        break
