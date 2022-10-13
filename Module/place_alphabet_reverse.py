import string

"""Fonction qui renvoie la lettre quand on lui donne la place"""

def place_alphabet_reverse(place):
    alpha = list(string.ascii_lowercase)
    alpha.append('Fin')
    return alpha[place]