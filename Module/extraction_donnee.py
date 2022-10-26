from Module import liste_mot, place_alphabet, table_donnee


PROBA = table_donnee.creation_table_donnee()
JEU_DE_MOT = liste_mot.lecture_fic('dictionnaire_traite.txt')

def donnee_brut(jeu_de_mot, table_donnee):
    """Fonction qui renvoie un dictionnaire avec les données brutes de ''l'analyse'' du .txt """
    for i in range(len(jeu_de_mot)):
        for j in range(len(jeu_de_mot[i])):
            if jeu_de_mot[i][j] in table_donnee:
                rang = place_alphabet.place_alpha(jeu_de_mot[i][j])
                res = table_donnee.get('Total')[rang]
                table_donnee['Total'][rang] = res + 1
                rang_lettre_suivante = place_alphabet.place_alpha(jeu_de_mot[i][j + 1])
                res2 = table_donnee.get(jeu_de_mot[i][j])[rang_lettre_suivante]
                table_donnee[jeu_de_mot[i][j]][rang_lettre_suivante] = res2 + 1
            elif jeu_de_mot[i][j] == 'Fin':
                rang = place_alphabet.place_alpha(jeu_de_mot[i][j])
                res = table_donnee.get('Total')[rang]
                table_donnee['Total'][rang] = res + 1
    return table_donnee
