class Skill:
    def __init__(self, nom):
        self.nom = nom

    def setLvl(self, lvl):
        self.lvl = lvl

    def setType(self, type):
        self.type = type

    def setCategorie(self, cat):
        self.categorie = cat


def creerSkill():
    nom = input("Donnez un nom à votre skill : ")
    skill = Skill(nom)
    lvl = int(input("A quel niveau se débloque votre skill ? "))
    skill.setLvl(lvl)
    type = input('Quel type ? (Magique ou physique)')
    skill.setType(type)
    cat = input("Quelle catégorie ? (Attaque, soutien ou malus)")
    skill.setCategorie(cat)
    return skill
