'''iphone'''

def iphone(ver, ram):
    '''iphone'''
    myiphone = {'13':{'mini':{'128 GB':25900, '256 GB':29900, '512 GB':37900},
                    '':{'128 GB':29900, '256 GB':33900, '512 GB':41900},
                    'Pro':{'128 GB':38900, '256 GB':42900, '512 GB':50900, '1 TB':58900},
                    'Pro Max':{'128 GB':42900, '256 GB':46900, '512 GB':54900, '1 TB':62900}
                    }
                }
    if ver.startswith('iPhone'):
        myver = ver.split()
        vert = myver[1]
        verv = '' if len(myver) == 2 else myver[2] if len(myver)==3 else " ".join(myver[2:])
        if vert in myiphone and verv in myiphone[vert] and ram in myiphone[vert][verv] :
            return myiphone[vert][verv][ram]
    return 'Not Available'
print(iphone(input(), input()))
