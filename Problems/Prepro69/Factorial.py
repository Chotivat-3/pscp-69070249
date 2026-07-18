"""FACTORY เอย FACTORIAL"""
def fac():
    """FAC"""
    n = int(input())
    n_ = 1

    if n < 0 :
        print("Factorial of a negative number is not defined.")
        return
    #elif n == 0 :
        #print("0! = 1")
    else :
        for i in range (1,n+1) :
            n_ *= i
            print(n_)

    print(f"{n}! = {n_}")

fac()
