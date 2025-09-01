#!/usr/bin/python3

def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 5)

def verifier_gagnant(plateau):
    for ligne in plateau:
        if ligne.count(ligne[0]) == len(ligne) and ligne[0] != " ":
            return True

    for col in range(len(plateau[0])):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] and plateau[0][col] != " ":
            return True

    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] != " ":
        return True

    if plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] != " ":
        return True

    return False

def morpion():
    plateau = [[" "]*3 for _ in range(3)]
    joueur = "X"
    while not verifier_gagnant(plateau):
        afficher_plateau(plateau)
        ligne = int(input("Choisis la ligne (0, 1 ou 2) pour le joueur " + joueur + " : "))
        colonne = int(input("Choisis la colonne (0, 1 ou 2) pour le joueur " + joueur + " : "))
        if plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = joueur
            if joueur == "X":
                joueur = "O"
            else:
                joueur = "X"
        else:
            print("Cette case est déjà prise ! Réessaie.")

    afficher_plateau(plateau)
    print("Le joueur " + joueur + " a gagné !")

morpion()

