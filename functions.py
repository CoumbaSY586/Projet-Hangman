# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:16:27 2020

@author: Almamy Youssouf LY
         Coumba SY
"""



#récupération de la liste de mots
 
def recuperer_liste_de_mots():
    #Auteur : Almamy Youssouf LY
    """cette fonction permet de récupèrer
    la liste des mots du fichier words.txt.
    """
    
    import ast
    with open("words.txt", "r") as file:
        d = file.read()
        liste = ast.literal_eval(d)
    return liste


#Fonctions du jeu Hangman
    
def choisir_niveau():
    #Auteur : Coumba SY
    """cette fonction permet de choisir un niveau parmi les trois
    """
    
    print("\n\t\t*******************")
    print("\t\t**   Niveau 1    ** \n\t\t**   Niveau 2    ** \n\t\t**   Niveau 3    **")
    print("\t\t*******************")
    
    niv = 0
    while niv<1 or niv>3: 
        try:   
            niv = int(input("Choisir un niveau: "))
            if  niv<1  or niv>3:
                print("le choix est invalide!")
                
        except ValueError:
            print("le choix doit être un entier.")
    return niv 

 
def choisir_mot(niv):
    #Auteur : Coumba SY
    """Cette fonction renvoie le mot choisi selon le niveau.
    """
    
    import random
    liste = recuperer_liste_de_mots()
    liste_extraite = []
    if niv==1:
        for elt in liste:
            if(len(elt)<=5):
                liste_extraite.append(elt)
        mot = random.choice(liste_extraite)
    if niv==2: 
       for elt in liste:
            if(len(elt)<=8):
                liste_extraite.append(elt)
       mot = random.choice(liste_extraite)  
    if niv==3:
        for elt in liste:
            if(len(elt)>=10):
                liste_extraite.append(elt)
        mot = random.choice(liste_extraite)
    return mot
    

def saisir_lettre():
    #Auteur : Almamy Youssouf LY
    """Cette fonction renvoie la lettre saisie.
    """
    
    lettre = input("Saisir une lettre:")
    return lettre.lower()
    

def placerLettre(mot_secret, lettres_trouvees):
    #Auteur : Almamy Youssouf LY
    """Cette fonction place la lettre saisie dans le mot secret
       et renvoie le mot masqué.
    """   
    
    mot_masquer = ""
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            mot_masquer += lettre
        else:
            mot_masquer += " _ "
    return mot_masquer


def calculer_score(tentative, mot):
    #Auteur : Coumba SY
    """Cette fonction renvoie le score calculé.
    """
    
    liste = []
    for lettre in mot:
        if lettre not in liste:
            liste.append(lettre)
    nbre = len(liste)
    score = tentative * nbre
    return score
    

def recuperer_scores(): 
    #Auteur : Almamy Youssouf Ly
    """Cette fonction récupère  et 
    renvoie la liste de scores de chaque partie. 
    """
    
    import data
    return data.scores


def enregistrer_scores(score):
    #Auteur : Coumba SY
    """Cette fonction enregistre le score dans la liste de score.
    """
    
    import data
    data.scores = score

    

    

        

            
    
    

