"""LAst Word"""
import json
x = input()
x = json.loads(x)

for i in x:
    print(str(i)[-1])
