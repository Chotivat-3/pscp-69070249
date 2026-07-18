"""BOX BOX"""
def string_box(x):
    """String_Ting!!"""
    n = len(x)
    q = ""
    for _ in range(n):
        q += "*"
    print(q+"**")
    print(f"*{x}*")
    print(q+"**")
string_box(input())
