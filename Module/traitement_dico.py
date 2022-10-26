from Module import liste_alphabet

def traitement():
    """Fonction qui traite le fichier dictionnnaire en retirant les mots à accent ou tiret"""
    """VOIR : mot_supp_par_algo.txt"""
    alpha = liste_alphabet.alphabet_liste()
    with open('../Texte/dictionnaire.txt', 'r') as filin:
        with open('../Texte/dictionnaire_traite.txt', 'w') as filout:
            ligne = filin.readline()
            while ligne != "":
                cpt = 0
                liste = list(ligne)
                if liste[-1] == '\n':
                    del liste[-1]
                liste.append('Fin')
                for elem in liste:
                    if elem in alpha:
                        cpt += 1
                if cpt == len(liste):
                    filout.write(ligne)
                ligne = filin.readline()

traitement()