dict_febo = {0:0, 1:1, 2:1}
def febo(n):
    if n < 0 or n is float :
        return 'WTF'
    if n in dict_febo:
        return dict_febo[n]
    res = febo(n-1)+febo(n-2)
    dict_febo[n] = res
    return res
print(febo(int(input())))
