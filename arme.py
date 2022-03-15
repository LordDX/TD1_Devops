import random
armes = ["DAGUE", "ARC", "BOUCLIER", "M4", "EPEE"]

class Arme:
    def __init__(self):
        self.ATK = 0
        self.durabilité = 0
        self.arme = ""

    def Random(weapon):
        random_arme = random.choice(armes)
        weapon.arme = random_arme
        if random_arme == "DAGUE" :
            weapon.ATK = 10
            weapon.durabilité = 10
        elif random_arme == "ARC" :
            weapon.ATK = 15
            weapon.durabilité = 10
        elif(random_arme == "BOUCLIER"):
            weapon.ATK = 0
            weapon.durabilité = 100
        elif(random_arme == "M4"):
            weapon.ATK = 1000
            weapon.durabilité = 90
        elif(random_arme == "EPEE"):
            weapon.ATK = 50
            weapon.durabilité = 80
        return weapon
    
    def Detail(weapon):
        print("Arme equipee :",weapon.arme," ",weapon.ATK,"/",weapon.durabilité,"\n")

    def Pick(weapon):
        print("Pick a weapon :")
        for i in armes :
            print("-"+i.title())
        pick = input("Quel arme voulez vous utiliser ? : ").upper()
        while(pick not in armes):
            print("Arme inexistante")
            pick = input("Quel arme voulez vous utiliser ? : ").upper()
        weapon.arme = pick
        if (pick == "DAGUE") :
            weapon.ATK = 10
            weapon.durabilité = 10
        elif (pick == "ARC") :
            weapon.ATK = 15
            weapon.durabilité = 10
        elif(pick == "BOUCLIER"):
            weapon.ATK = 0
            weapon.durabilité = 100
        elif(pick == "M4"):
            weapon.ATK = 1000
            weapon.durabilité = 90
        elif(pick == "EPEE"):
            weapon.ATK = 50
            weapon.durabilité = 80
            
        weapon.Detail()
        
        print("\n")
        


