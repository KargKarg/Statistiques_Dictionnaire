import matplotlib.pyplot as plt
from Module import table_donnee, liste_mot, liste_alphabet, extraction_donnee, \
    place_alphabet_reverse

PROBA = table_donnee.creation_table_donnee()
JEU_DE_MOT = liste_mot.lecture_fic('dictionnaire_traite.txt')

donne = extraction_donnee.donnee_brut(JEU_DE_MOT, PROBA)

def graphe():
    """Fonction qui trace des graphes pour chaque lettre"""
    alphabet = liste_alphabet.alphabet_liste()
    for i in range(26):
        cle = place_alphabet_reverse.place_alphabet_reverse(i)
        liste = donne[cle]
        plt.figure(figsize=(12, 6), dpi=80)
        plt.bar(alphabet, liste, align='center')
        plt.xlabel(f'Lettres qui suivent {cle}')
        plt.ylabel(f'Apparition après {cle}')
        plt.title(f"Graphique représentant le nombre d'apparition d'une lettre qui suit {cle}")
        for elem, place in zip(liste, alphabet):
            plt.annotate(xy=[place, elem], text=str(elem))
        plt.savefig(f'graphe_{cle}.pdf', format='pdf')
graphe()