class Personnage:

    "Ceci est la classe Personnage"


    def __init__(self, nom = 'nobody', prenom = 'nobody', age = 0, str = 0, int = 0, luck = 0) :

        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.str = str
        self.int = int
        self.luck = luck

    def setClasse(self, classe):
        if type.lower() not in ["mage", "guerrier", "voleur", "archer", "chevalier", "lancier"]:
            raise Exception("Classe incorrecte")
        self.classe = classe

    def presentation(self) :
        "Affichage des données personnage"

        print(self.nom,'',self.prenom,"agée de ",self.age,'ans')
        print(self.classe," de niveau 1")
        print('Stat attaque : ',self.str, ' stat intelligence : ',self.int, ' stat chance : ' ,self.luck)


def creePersonnage():
    Personnage.nom = input("Quel est le nom de votre personnage ? ")
    Personnage.prenom = input("Quel est le prènom de votre personnage ? ")

    clas = input("Saissez votre classe parmis la liste suivante : Mage, Guerrier, Voleur, Archer, Chevalier, Lancier. \n")
    try:
        Personnage.setClasse(clas)
    except Exception as err:
        print(err)
    Personnage.age= input("Quel est l'age de votre personnage ")

    str = int(input("Quel est l'attaque de votre personnage "))
    try:
            Personnage.str = int(str)
    except ValueError:
            print(ValueError)

    intelligence = input("Quel est l'intelligence de votre personnage ")
    try:
            Personnage.int = int(intelligence)
    except ValueError:
            print(ValueError)

    luck = input("Quel est la chance de votre personnage ")
    try:
            Personnage.luck = int(luck)
    except ValueError:
            print(ValueError)


creePersonnage()

print("\n")
print("Présentation personnage")
Personnage.presentation(Personnage)