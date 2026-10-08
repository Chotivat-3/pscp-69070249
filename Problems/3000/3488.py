'''Song Kob'''
def theme_park(n):
    '''Song Kob'''
    ligt_pit = []
    add_light = []
    for i in range(n):
        x, y = map(int,input().split())
        ligt_pit.append([x,y])
        if i:
            for mylp in ligt_pit[i-1:]:
                if x<y and  x >= mylp[0] and x <= mylp[1] and y > mylp[1]:
                    add_light.append([mylp[0],y])
                if x<y and  y >= mylp[0] and y <= mylp[1] and x < mylp[0]:
                    add_light.append([y,mylp[1]])
                if x>y and  x >= mylp[0] and x <= mylp[1] and y > mylp[1]:
                    add_light.append([mylp[0],y])
                if x>y and  y >= mylp[0] and y <= mylp[1] and x < mylp[0]:
                    add_light.append([y,mylp[1]])
    out = ligt_pit + add_light
    print(out)
    out = list(map(lambda x:x[1]-x[0],out))
    print(out)
    for i,num in enumerate(out):
        if num < 0 :
            out[i] = 360+num
    print(out)
    out.sort(reverse=True)
    return out[0]
print(theme_park(int(input())))
