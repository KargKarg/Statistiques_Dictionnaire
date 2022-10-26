import matplotlib.pyplot as plt
from Module import table_donnee, liste_mot, liste_alphabet, extraction_donnee

PROBA = table_donnee.creation_table_donnee()
JEU_DE_MOT = liste_mot.lecture_fic('dictionnaire_traite.txt')

donne = extraction_donnee.donnee_brut(JEU_DE_MOT, PROBA)

def graphe_baton():
    """Fonction qui trace un graphe en bâton avec le nombre total de lettre"""
    valeur = donne['Total'][:-1]
    alphabet = liste_alphabet.alphabet_liste()[:-1]
    plt.figure(figsize=(12, 6), dpi=80)
    plt.bar(alphabet, valeur, align='center')
    plt.xlabel('Lettre')
    plt.ylabel('Apparition')
    plt.title("Graphique représentant le nombre d'apparition d'une lettre")
    for elem, place in zip(valeur, alphabet):
        plt.annotate(xy=[place, elem], text=str(elem))
    plt.savefig('total_stats.pdf', format='pdf')
    plt.show()

graphe_baton()

def graphe_camembert():
    """Fonction qui trace un graphe circulaire avec le nombre total de lettre"""
    valeur = donne['Total'][:-1]
    alphabet = liste_alphabet.alphabet_liste()[:-1]
    plt.figure(figsize=(12, 9), dpi=80)
    plt.pie(valeur, labels=alphabet, radius=1.25, autopct='%1.2f%%')
    plt.title("Graphique représentant la part de chaque lettre dans la langue française")
    plt.savefig('total_stats_circulaire.pdf', format='pdf')
    plt.show()

graphe_camembert()