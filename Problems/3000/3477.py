'''Pad Thai'''
ingre = {'Pad Thai Sauce','Tofu','Pickle Turnip',
         'Shrimp', 'Bean Sprouts', 'Noodle', 'Chives'
         ,'Lime', 'Egg', 'Oil', 'Peanuts'}
ingre_have = set()
ingreout = 0

taste = {'Sweet', 'Sour', 'Salty'}
taste_have = set()
tasteout = 0

have = ''
while True:
    have = input()
    if have == 'Cook':
        break
    if have in ingre:
        ingre_have.add(have)
    else:
        ingreout = 1

while True:
    have = input()
    if have == "End":
        break
    if have in taste:
        taste_have.add(have)
    else:
        tasteout = 1

if ingreout:
    print("This is not Pad Thai!!!")
elif len(ingre_have) != 11 :
    print("This is bad!")
elif tasteout or len(taste_have) != 3:
    print("Not Bad...")
else:
    print("Delicious!")
