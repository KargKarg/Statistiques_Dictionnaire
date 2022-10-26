from Module import liste_alphabet


def place_alpha(carac):
    """Fonction qui renvoie la place quand on lui donne la lettre"""
    alpha = liste_alphabet.alphabet_liste()
    if carac == 'Fin':
        return 26
    elif carac == 'Total':
        return -10
    for i in range(len(alpha)):
        if carac == alpha[i]:
            return i

