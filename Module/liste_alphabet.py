import string


def alphabet_liste():
    """Fonction qui renvoie une liste contenant l'alphabet + 'Fin' en 26eme position"""
    alphabet = [string.ascii_lowercase[i] for i in range(26)]
    alphabet.append('Fin')
    return alphabet
