"""Exchange"""

def b () :
    """BAHT"""
    m=str(input()).upper()
    p=float(input())
    total=0
    if m == "USD": 
        total = p*32.50
        print(f"You will receive {total:.2f} Thai Baht")
    elif m == "JPY" :
        total = p*0.29
        print(f"You will receive {total:.2f} Thai Baht")
    elif m == "EUR" :
        total = p*35.70
        print(f"You will receive {total:.2f} Thai Baht")
    elif m == "CNY" :
        total = p*4.90
        print(f"You will receive {total:.2f} Thai Baht")
    elif m == "GBP" :
        total = p*41.20
        print(f"You will receive {total:.2f} Thai Baht")
    else :
        print("The currency you entered is not supported in the system")
b ()
