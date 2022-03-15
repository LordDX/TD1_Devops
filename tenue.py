###############################################################################################
###
###  Author : SINDIC Mathieu
###  Projet : DEVOPS TD1
###  File   : tenue.py
###
###############################################################################################

inventaire = ["robe"]
liste_tenue = ["robe", "epaulette", "plastron_leger", "plastron_moyen", "plastron_lourd", "botte_en_tissu", "botte_en_cuir", "botte_en_plaque"]
tenue = input("Quel tenue voulez vous utiliser ? : ")

def equiper_tenue(tenue):
    if len(tenue) == 0:
        print("Vous n'avez rien entrer ")
        return -1
    elif tenue.isdigit():
        print("Votre entrée est invalide : Entrée de chiffre")
        return -1
    else:
        if tenue.lower() not in liste_tenue:
            print("Tenue non conforme, veuillez resaisir une tenue provenant de la liste suivante :")
            print(liste_tenue)
            return -1
        if tenue.lower() not in inventaire:
            print("Vous ne possédez pas cette item sur vous")
            return -1
        else:
            print("Bravo ! Vous venez d'équiper", tenue)
            return 0

res = equiper_tenue(tenue)
while (res != 0):
    tenue = input("Quel tenue voulez vous utiliser ? : ")
    res = equiper_tenue(tenue)

input("Fin du code")