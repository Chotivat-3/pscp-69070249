'''cal'''

def cal():
    '''cal'''
    mycal = {1:100, 2:120, 3:200, 4:60}
    total = 0
    while True:
        n  = int(input())
        if n == 5:
            return f'Bye Bye\nTotal Calories: {total}'
        total += mycal[n]
print(cal())
