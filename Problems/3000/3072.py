"""AEIOU AGAIN"""
text = input().lower()
a = text.count("a")
e = text.count("e")
i = text.count("i")
o = text.count("o")
u = text.count("u")
def out(x,x_):
    """out"""
    if x :
        print(f"{x_} : {x}")
out(a,"a")
out(e,"e")
out(i,"i")
out(o,"o")
out(u,"u")
