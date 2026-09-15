'''pick'''
import json
x = json.loads(input())
out = ''

for i in x:
    if not i % 2:
        out += '1'
        print(i)
if not out:
    print('Nope')
