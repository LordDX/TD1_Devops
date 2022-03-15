###############################################################################################
###
###  Author : SINDIC Mathieu
###  Projet : DEVOPS TD1
###  File   : lieu.py
###
###############################################################################################

liste_lieux = ["stormwind", "orgrimar", "durotar", "the_void", "oribos", "bastion", "ardenweald"]
lieu = input("Dans quel lieu voulez vous aller ? : ")

def deplacement_lieu(lieu):
    if len(lieu) == 0:
        print("Vous n'avez rien entrer ")
        return -1
    elif lieu.isdigit():
        print("Votre entrée est invalide : Entrée de chiffre")
        return -1
    else:
        if lieu not in liste_lieux:
            print("Lieu non conforme, veuillez resaisir un lieu provenant de la liste suivante :")
            print(liste_lieux)
            return -1
        else:
            print("Allons à", lieu.capitalize(), "mon ami. Cela me semble etre un bon choix ! ")
            return 0

res = deplacement_lieu(lieu)
while (res != 0):
    lieu = input("Dans quel lieu voulez vous aller ? : ")
    res = deplacement_lieu(lieu)

input("Fin du code")