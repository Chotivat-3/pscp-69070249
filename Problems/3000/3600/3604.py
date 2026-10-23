'''progessive'''

def tax(m):
    '''tax'''
    t = [150000*5, 200000*10, 250000*15,250000*20, 1000000*25, 2000000*30]
    if m <= 150000:
        return 0
    if m <= 300000:
        return (m-150000)*5
    if m <= 500000:
        return (m-300000)*10+t[0]
    if m <= 750000:
        return (m-500000)*15+sum(t[:2])
    if m <= 1000000:
        return (m-750000)*20+sum(t[:3])
    if m <= 2000000:
        return (m-1000000)*25+sum(t[:4])
    if m <= 4000000:
        return (m-2000000)*30+sum(t[:5])
    return (m-4000000)*35+sum(t)
print(int(tax(int(input()))/100))
