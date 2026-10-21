'''SN SN'''
my_sn = {1:'1',2:'2'}

def sn(num,s):
    '''sn sn'''
    while True:
        if num in s :
            return s[num]
        this = max(list(s.keys()))+1
        s[this] = s[this-1]+s[this-2]
print(sn(int(input()),my_sn))
