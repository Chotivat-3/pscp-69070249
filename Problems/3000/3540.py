'''Digit Digit'''

def mydigit(t):
    '''digit'''
    d_plus = { 'zero':0 ,'one':1 ,'two':2 , 'three':3, 'four':4,
                'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
                'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13,
                'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17,
                'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30,
                'forty':40, 'fifty':50, 'sixty':60, 'seventy':70,
                'eighty':80, 'ninety':90}

    d_multi = { 'hundred':100, 'thousand':1000 }

    mykey = t.split()

    def numnum (k):
        '''cal'''
        num,numluv = 0, 0
        for i in k:
            if i in d_plus:
                num += d_plus[i]
            elif i in d_multi and 'hundred' in k[k.index(i)+1:] :
                numluv = num*d_multi[i]
                num = 0
            else:
                num *= d_multi[i]
        return num+numluv

    out = numnum(mykey)
    return out

print(mydigit(input()))
