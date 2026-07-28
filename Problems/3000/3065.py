"""Roman"""
num = int(input())
roman = {1:"I",2:"II",3:"III",4:"IV"
         ,5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"
         }
if 0 < num <=9:
    print(roman[num])
elif num < 0:
    print("Error : Please input positive number")
else:
    print("Error : Out of range")
