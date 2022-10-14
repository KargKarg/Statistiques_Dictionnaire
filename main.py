import extraction_donnee
from Module import liste_mot, table_donnee, place_alphabet_reverse

PROBA = table_donnee.creation_table_donnee()
JEU_DE_MOT = liste_mot.lecture_fic('Texte\dictionnaire_traite.txt')
donne = extraction_donnee.donnee_brut(JEU_DE_MOT, PROBA)

def stats():
    with open("Texte/stats.txt", 'w') as filout:
        for i in range(26):
            somme_lettre = 0
            for k in range(26):
                somme_lettre += donne['Total'][k]
            proba_brut1 = (donne["Total"][i] / somme_lettre) * 100
            proba_1 = round(proba_brut1, 2)
            filout.write(f"Il y'a {proba_1}% que un mot commence par "
                         f"'{place_alphabet_reverse.place_alphabet_reverse(i)}'"
                         f","
                         f"on traite le cas de '{place_alphabet_reverse.place_alphabet_reverse(i)}' maitenant : \n")
            for j in range(27):
                proba_brut2 = (donne[place_alphabet_reverse.place_alphabet_reverse(i)][j] / donne["Total"][i]) * 100
                proba_2 = round(proba_brut2, 2)
                filout.write(f"Les chances que '{place_alphabet_reverse.place_alphabet_reverse(j)}' "
                             f"suive '{place_alphabet_reverse.place_alphabet_reverse(i)}'"
                             f" sont de {proba_2}%\n")
            filout.write(f"\n\n\n")


stats()