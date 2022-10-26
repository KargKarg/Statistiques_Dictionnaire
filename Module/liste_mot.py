

def lecture_fic(nom_fic):
    """Fonction qui renvoie la totalité d'un fichier sous forme de liste"""
    with open(nom_fic, 'r') as filin:
        ligne = filin.readline()
        mot_total = []
        while ligne != "":
            listed_mot = list(ligne)
            if listed_mot[-1] == '\n':
                del listed_mot[-1]
            listed_mot.append('Fin')
            mot_total.append(listed_mot)
            ligne = filin.readline()
        return mot_total
