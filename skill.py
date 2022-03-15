class Skill:
    def __init__(self, nom):
        self.nom = nom

    def setLvl(self, lvl):
        try:
            lvl = int(lvl)
        except ValueError:
            lvl = 0
        self.lvl = lvl

    def setType(self, type):
        if type.lower() not in ['magique', 'physique']:
            raise Exception("Type incorrect")
        self.type = type

    def setCategorie(self, cat):
        if type.lower() not in ['attaque', 'soutien', 'malus']:
            raise Exception("Catégorie incorrecte")
        self.categorie = cat


def creerSkill():
    nom = input("Donnez un nom à votre skill : ")
    skill = Skill(nom)
    lvl = int(input("A quel niveau se débloque votre skill ? "))
    skill.setLvl(lvl)
    type = input('Quel type ? (Magique ou physique)')
    try:
        skill.setType(type)
    except Exception as err:
        print(err)
    cat = input("Quelle catégorie ? (Attaque, soutien ou malus)")
    try:
        skill.setCategorie(cat)
    except Exception as err:
        print(err)
    return skill
