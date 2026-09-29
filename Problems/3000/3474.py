'''Resistor'''
f1_2 = {'Black':'0', 'Brown':"1", 'Red':'2'
      , 'Orange':'3', 'Yellow':'4', 'Green':'5'
      , 'Blue':'6', 'Purple':'7', 'Grey':'8', 'White':'9'}
f3 = {'Black':1, 'Brown':10, 'Red':10**2
      , 'Orange':10**3, 'Yellow':10**4, 'Green':10**5
      , 'Blue':10**6, 'Purple':10**7, 'Grey':10**8, 'White':10**9
      ,'Gold':0.1, 'Silver':0.01}
f4 = {'Brown':1/100, 'Red':2/100, 'Green':0.5/100, 'Blue':0.25/100
      , 'Purple':0.1/100, 'Grey':0.05/100, 'Gold':5/100, 'Silver':10/100}

key1,key2,key3,key4 = input(), input(), input(), input()
if key1 in f1_2 and key2 in f1_2 and key3 in f3 and key4 in f4:
    total = int(int(f1_2[key1]+f1_2[key2])*f3[key3]*100)
    totalpos = int((total + total*f4[key4])*10000)
    totalneg = int((total - total*f4[key4])*10000)
    print(f"{totalneg//1000000}.{totalneg%10000000:04d}")
    print(f"{totalpos//1000000}.{totalpos%10000000:04d}")
else:
    print("Error")
