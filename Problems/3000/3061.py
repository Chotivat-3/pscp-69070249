"""PASS NOT PASS"""
mid = int(input())
final = int(input())
mpf = mid + final
out = ""
if mpf >= 50:
    out+="pass"
else:
    out+="fail"
print(mpf)
print(out)
