import extraction_donnee
from Module import liste_mot, place_alphabet_reverse, table_donnee, place_alphabet

"""Fonction qui met au propre les résultats traités dans l'extraction dans un .txt"""
"""VOIR : resultats.txt"""

def mise_en_forme():
    PROBA = table_donnee.creation_table_donnee()
    JEU_DE_MOT = liste_mot.lecture_fic('Texte\dictionnaire_traite.txt')
    donnee = extraction_donnee.donnee_brut(JEU_DE_MOT, PROBA)
    with open('Texte/resultats.txt', 'w') as filout:
        for key in donnee:
            if key == 'Total':
                break
            filout.write(f"On traite ici le cas de {key} :\n")
            lettre_1 = place_alphabet.place_alpha(key)
            for i in range(27):
                lettre_2 = place_alphabet_reverse.place_alphabet_reverse(i)
                filout.write(f"Il y a '{donnee.get(key)[i]}' '{key}' suivies de {lettre_2}\n")
            if lettre_1 != 27 :
                filout.write(f"Pour un total de : {donnee.get('Total')[lettre_1]} {key}")
                filout.write(f'\n\n\n\n')


mise_en_forme()