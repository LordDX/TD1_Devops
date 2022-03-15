class quest:
    def __init__(self, id_npc, desc, reward):
        if not type(id_npc) is int:
            raise TypeError("L'id NPC doit être un nombre")
        self.id_npc = id_npc

        if not type(desc) is str:
            raise TypeError("La description doit être une chaine de caractère")
        self.desc = desc
        if not type(id_npc) is int:
            raise TypeError("La variable reward doit contenir un nombre")
        self.reward = reward
    
    def showInfo(self):
        print(self.id_npc,";",self.desc,";",self.reward)


def generate_quest_list_on_start_game(id_npc):
    if not type(id_npc) is int:
        raise TypeError("L'id NPC doit être un nombre")
            
    try:
        open('quests.txt')
    except TypeError as ex:
        print('Nom de fichier de quête incorrect',str(ex))    
        raise
    with open('quests.txt','r') as tf:
        quest_list = []
        line = tf.readline()
        

        while line:
            # utilisez readline() pour lire la ligne suivante
            if(line.split(";")[0] == str(id_npc)):
                print("\n On passe dedans")
                quete = quest(id_npc, line.split(";")[1], line.split(";")[2])
                quest_list.append(quete)
            line = tf.readline()
    tf.close()
    return quest_list

listNPC0 = generate_quest_list_on_start_game(0)
listNPC1 = generate_quest_list_on_start_game(1)
listNPC2 = generate_quest_list_on_start_game(2)

print("\nListe de quete du NPC 0 : ")
for i in range(0,len(listNPC0)):
    listNPC0[i].showInfo()
    print("\n")
print("\nListe de quete du NPC 1 : ")
for i in range(0,len(listNPC1)):
    listNPC1[i].showInfo()
    print("\n")
print("\nListe de quete du NPC 2 : ")
for i in range(0,len(listNPC2)):
    listNPC2[i].showInfo()
    print("\n")

with open(listNPC0,'r')as suisse:
    line = suisse.readline()
