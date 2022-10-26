import string


def place_alphabet_reverse(place):
    """Fonction qui renvoie la lettre quand on lui donne la place"""
    alpha = list(string.ascii_lowercase)
    alpha.append('Fin')
    return alpha[place]