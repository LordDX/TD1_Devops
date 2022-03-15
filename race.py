class Race:

    "Ceci est la classe Race"


    def __init__(self, nom = 'nobody', humeur = 'nobody', Dons = '', type = '') :

        self.nom = nom
        self.humeur = humeur
        self.Dons = Dons
        self.type = type

    def presentation(self) :
        "Affichage des données de la Race"

        print(self.nom, " est plutôt d'humeur ",self.humeur)
        print("Le type de cette race est : ",self.type, "et leur dons est : ", self.Dons)


listeDons = list("lumière", "ténébre", "clairvoyance")
listehumeur = list("grognon", "méchant", "gentil", "doux", "aimante")
listetype = list("humanoïde" , "créature", "humain")

while(Race.nom != str or  Race.humeur != listehumeur or Race.Dons != listeDons or Race.type != listetype ) :
    Race.nom = input("Quel est le nom de la race ?")
    Race.humeur = input("L'humeur raciale (utilisez la liste suivante : grognon, méchant, gentil, doux, aimante)")
    Race.Dons = input("Quel est le dons de cette race (veuilliez utilisez la liste suivante : lumière, ténébre, clairvoyance)")
    Race.type = input("le type de race (liste : humanoïde , créature, humain)")


Race.presentation()