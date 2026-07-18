"""หัวจะปวด"""
def revam (x):
    """reอะไรreทำไม?"""
    text = ""
    p_text = ""
    for t in x:
        if t != " ":
            text += t
        if t == " ":
            if len(text) >= 4 :
                text = f"{text[::-1]} "
                p_text += text
                text = ""
            else :
                text = f"{text} "
                p_text += text
                text = ""
    last = len(x)-len(p_text)
    st = len(x)-last
    if last >= 4 :
        p_text += x[:st-1:-1]
    else :
        p_text += x[st:]
    print(p_text.strip())
revam(input())
