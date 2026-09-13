'''113'''

out = input()

while True:

    if '113' in out:
        n = out.find('113')
        out = out[:n]+out[n+3:]
    else:
        break

print(out)
