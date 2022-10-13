import string

"""Fonction qui renvoie un dictionnaire de liste """

def creation_table_donnee():
    table = {}
    alphabet = string.ascii_lowercase
    for i in range(26):
        table[alphabet[i]] = [0*i for i in range(27)]
    table['Total'] = [0*i for i in range(27)]
    return table