import random

"""
Fonction qui part d'un tableau t qui contient 4 images et qui renvoie l'indice de l'intrus : 0, 1, 2 ou 3
"""
def donneIntrus(t):
    # Pour simplifier, on échnage les lignes et les colonnes de la matrices pour retrouver dans la même
    # sous liste les caractéristiques communes
    somme = [[], [], []]
    for l in range(3):
        somme[l].append(t[0][l])
        somme[l].append(t[1][l])
        somme[l].append(t[2][l]) 
        somme[l].append(t[3][l]) 
    res = []

    # Pour chaque caractéristique on compte le nombre de fois qu'elle apparait. Si c'est 1, elle est unique
    for i in range(3):
        for carac in list(set(somme[i])):
            if somme[i].count(carac) == 1:
                res.append(somme[i].index(carac))

    return(res)

"""
Fonction qui génère toutes les possibilités de combinaison à partir de 3 critères binaires
"""
def combinaison(possible):
    combi = []
    for i in range(len(possible)):
        for j in range(i+1, len(possible)):
            for k in range(j+1, len(possible)):
                for l in range(k+1, len(possible)):
                    combi.append([possible[i], possible[j], possible[k], possible[l]])
    return combi

"""
Génère une énigme aléatoire à partir de l'ensemble des énigmes correctes
"""
def genereEnigme(e):
    enigme = random.choice(e)
    random.shuffle(enigme)
    return enigme


possible = []
for i in ("Entoure", "Vide"):
    for j in ("Feuille", "Fleur"):
        for k in ("Plein", "Vide"):
            possible.append([i, j, k])
print(possible)

combi = combinaison(possible)
enigmesValides = []
cpt = 0
for ele in combi:
    lstIntrus = donneIntrus(ele)
    print(ele)
    cpt += 1
    print("Intrus : ", donneIntrus(ele))
    if len(lstIntrus) == 1:
        enigmesValides.append(ele)
print(cpt)
print(enigmesValides)
e = genereEnigme(enigmesValides)
print(e)
print(donneIntrus(e))