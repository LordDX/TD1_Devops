class Classe:
    def __init__(self, nom):
        self.nom = nom
        self.armes = set()
        self.skills = set()

    def addArme(self, arme):
        self.armes.add(arme)

    def addSkill(self, skill):
        self.skills.add(skill)

    def setAsset(self, asset):
        self.asset = asset

    def setFailing(self, fail):
        self.failing = fail


def creerClasse():
    nom = input("Donnez un nom à votre classe : ")
    classe = Classe(nom)
    arme = ''
    while arme != "x":
        arme = input(
            "Ajoutez une arme utilisable à votre classe (tapez x pour arrêter) :"
        )
        classe.addArme(arme)
    skill = ''
    while skill != "x":
        skill = input(
            "Ajoutez un skill utilisable à votre classe (tapez x pour arrêter) :"
        )
        classe.addSkill(skill)
    asset = input('Quelle est la stat la plus forte ?')
    classe.setAsset(asset)
    fail = input('Quelle est la stat la plus faible ?')
    classe.setFailing(fail)
    return classe
