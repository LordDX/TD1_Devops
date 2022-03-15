import random
items = ["POTIONHP", "POTIONMANA"]

class Consommable:
    def __init__(self):
        self.item = ""

    def Random(obj):
        random_obj = random.choice(items)
        obj.item = random_obj
        return obj
    
    def Detail(obj):
        print("Consommable utilise :",obj.item,"\n")

    def Pick(obj):
        print("Pick a weapon :")
        for i in items :
            print("-"+i.title())
        pick = input("Quel item voulez vous utiliser ? : ").upper()
        while(pick not in items):
            print("Item inexistante")
            pick = input("Quel objet ? : ").upper()
        obj.item = pick
            
        obj.Detail()
        
        print("\n")
        

o = Consommable()
o.Pick()