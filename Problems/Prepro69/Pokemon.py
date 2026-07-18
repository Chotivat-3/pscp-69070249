"""Pokemon"""
def pokemon () :
    """Pokemon"""
    name = str(input())
    skill = str(input())
    ee = str(input()).upper()
    e_1 = str(input()).upper()
    e_2 = str(input()).upper()
    x = 1
    if ee == "NORMAL" :
        print(f"{name} use {skill}!")
        print(f"Effectiveness x {x:.2f}")
    else :
        if e_1 == e_2  :
            if ee == "FIRE":
                if e_1 == "NORMAL" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "FIRE" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "WATER" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "ELECTRIC" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "GRASS" :
                    x = x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
            if ee == "WATER":
                if e_1 == "NORMAL" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "FIRE" :
                    x = x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "WATER" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "ELECTRIC" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "GRASS" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
            if ee == "ELECTRIC":
                if e_1 == "NORMAL" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "FIRE" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "WATER" :
                    x = x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "ELECTRIC" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "GRASS" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
            if ee == "GRASS":
                if e_1 == "NORMAL" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "FIRE" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "WATER" :
                    x = x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "ELECTRIC" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                if e_1 == "GRASS" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
        else :
            if e_1 == "FIRE" and e_2 == "WATER" or e_1 == "WATER" and e_2 == "FIRE" :
                if ee == "FIRE" :
                    x = x*1/4
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    x=x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
            if e_1 == "FIRE" and e_2 == "ELECTRIC" or e_1 == "ELECTRIC" and e_2 == "FIRE" :
                if ee == "FIRE" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    x = x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!" )
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
            if e_1 == "FIRE" and e_2 == "GRASS" or e_1 == "GRASS" and e_2 == "FIRE" :
                if ee == "FIRE" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    x = x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    x = x*1/4
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")                  
            if e_1 == "WATER" and e_2 == "ELECTRIC" or e_1 == "ELECTRIC" and e_2 == "WATER" :
                if ee == "FIRE" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    x = x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!" )
                    print(f"Effectiveness x {x:.2f}")  
            if e_1 == "WATER" and e_2 == "GRASS" or e_1 == "GRASS" and e_2 == "WATER" :
                if ee == "FIRE" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    x=x*1/4
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
            if e_1 == "ELECTRIC" and e_2 == "GRASS" or e_1 == "GRASS" and e_2 == "ELECTRIC" :
                if ee == "FIRE" :
                    x=x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    x=x*1/4
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")   
            if e_1 == "NORMAL" and e_2 == "FIRE" or e_1 == "FIRE" and e_2 == "NORMAL" :
                if ee == "FIRE" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    x=x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print( "It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
            if e_1 == "NORMAL" and e_2 == "WATER" or e_1 == "WATER" and e_2 == "NORMAL" :
                if ee == "FIRE" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print( "It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    x=x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    x=x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
            if e_1 == "NORMAL" and e_2 == "ELECTRIC" or e_1 == "ELECTRIC" and e_2 == "NORMAL" :
                if ee == "FIRE" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    print(f"{name} use {skill}!")
                    print(f"Effectiveness x {x:.2f}")
            if e_1 == "NORMAL" and e_2 == "GRASS" or e_1 == "GRASS" and e_2 == "NORMAL" :
                if ee == "FIRE" :
                    x=x*2
                    print(f"{name} use {skill}!")
                    print("It's super effective!")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "WATER" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "ELECTRIC" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")
                elif ee == "GRASS" :
                    x=x*1/2
                    print(f"{name} use {skill}!")
                    print("It's not very effective...")
                    print(f"Effectiveness x {x:.2f}")

pokemon()
