"""secret message"""
def secret(x):
    """message"""
    x = x.split(" ")
    text = ""
    for i in x:
        if len(i) >= 4 :
            text += f"{i[::-1]} "
        else:
            text += f"{i} "
    print(text.strip())
secret(input())   
