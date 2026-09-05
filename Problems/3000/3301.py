"""BOX"""
w,l,m,n = map(int,input().split())
#  เศษจากด้านกว้าง เศษจากด้านยาว คือพื้นที่ที่เหลือ
re = (w%m)*(l%m)
for i in range(m+1,n+1):
    rm=(w%i)*(l%i)
    if rm < re:
        re = rm
    if not re :
        break
print(re)
