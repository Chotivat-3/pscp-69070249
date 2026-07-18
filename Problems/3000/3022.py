"""Temperature"""
T = float(input())
T1 = input()
T2 = input()
def c ():
    """celsius"""
    t_cout = 0
    match T1 :
        case "C":
            t_cout += T
        case "F":
            t_cout += (T-32)/(9/5)
        case "K":
            t_cout += T-273.15
        case "R":
            t_cout += (T/(9/5))-273.15
    return t_cout
def tem (c_=c()):
    """cal Tem"""
    t_out = 0
    match T2 :
        case "C":
            t_out += c_
        case "K":
            t_out += c_+273.15
        case "F":
            t_out += c_*(9/5)+32
        case "R":
            t_out += (c_+273.15)*(9/5)
    t_out = round(t_out,2)
    t_out = f"{t_out:.2f}"
    return t_out
tem_out = tem()
print(tem_out)
