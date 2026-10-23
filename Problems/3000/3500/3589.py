'''Recursion'''
my_feb = {0:0,1:1}
def feb(n):
    '''febo'''
    if n in my_feb:
        return my_feb[n]
    my_feb[n] = feb(n-1) + feb(n-2)
    return my_feb[n]
feb(500)
print(feb(n = int(input())))
