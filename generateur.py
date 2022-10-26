import random
from Module import liste_mot, table_donnee, place_alphabet_reverse, extraction_donnee


PROBA = table_donnee.creation_table_donnee()
JEU_DE_MOT = liste_mot.lecture_fic('Texte\dictionnaire_traite.txt')
donne = extraction_donnee.donnee_brut(JEU_DE_MOT, PROBA)
proba_premiere_lettre = []
proba_sachant = table_donnee.creation_table_donnee()
MOT = ""
LEN_MOT = 0



def generateur():
    """Fonction qui crée une liste de mots suivants les probabilités"""
    for i in range(26):
        somme_lettre = 0
        for k in range(26):
            somme_lettre += donne['Total'][k]
        proba_brut1 = (donne["Total"][i] / somme_lettre) * 100
        proba_1 = round(proba_brut1, 2)
        proba_premiere_lettre.append(proba_1)
        for j in range(27):
            proba_brut2 = (donne[place_alphabet_reverse.place_alphabet_reverse(i)][j] / donne["Total"][i]) * 100
            proba_2 = round(proba_brut2, 2)
            proba_sachant[place_alphabet_reverse.place_alphabet_reverse(i)][j] = proba_2

def premiere_lettre(liste_prob):
    global MOT, LEN_MOT
    alea = random.uniform(0.00,99.99)
    tirage = liste_prob[0]
    for i in range(len(liste_prob)):
        if tirage < alea:
            tirage += liste_prob[i+1]
        else:
            MOT += place_alphabet_reverse.place_alphabet_reverse(i)
            LEN_MOT += 1
            return place_alphabet_reverse.place_alphabet_reverse(i)

def suite_mot(n, lettre):
    global LEN_MOT, MOT
    if LEN_MOT == n:
        return
    else:
        alea = random.uniform(0.00, 99.99)
        if lettre in proba_sachant:
            tirage = proba_sachant[lettre][0]
            for j in range(len(proba_sachant[lettre])):
                if tirage < alea:
                    tirage += proba_sachant[lettre][j]
                else:
                    MOT += place_alphabet_reverse.place_alphabet_reverse(j)
                    LEN_MOT += 1
                    return suite_mot(n, place_alphabet_reverse.place_alphabet_reverse(j))


generateur()

def ecriture():
    global MOT, LEN_MOT
    with open('Texte/resultats_generation.txt', 'a') as filout:
        for k in range(1,11):
            filout.write(f"Mots de {k} lettre(s) : \n")
            for i in range(100):
                suite_mot(k, premiere_lettre(proba_premiere_lettre))
                filout.write(f"{MOT}\n")
                MOT = ""
                LEN_MOT = 0
            filout.write('\n\n\n')

ecriture()