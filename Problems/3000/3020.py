"""Coke"""
###ทดลอง####
p = int(input())
cap = int(input())
np = int(input())
wt = int(input())
if cap:
    n_np = wt//cap
    if not wt%cap and n_np:# ผิดกรณี wt=0
        n_np -= 1
else :
    n_np = 0
n_op = wt - n_np
total = (n_op*p) + (n_np*np)
print(total)
