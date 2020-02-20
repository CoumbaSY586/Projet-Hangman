# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:16:51 2020

@author: ALmamy Youssouf LY
         Coumba SY
"""



def jouer():
    #Cette partie a été co-écrite.
    """Programmme principal du jeu Hangman.
    """
    
    import data
    import functions
    
    #cette variable permet de savoir quand arrêter la partie.
    continuer = "o" 
    
    #cette variable permet de stocker la partie.
    partie = 0
    
    #on récupère la liste des scores dechaque partie.
    liste_scores = functions.recuperer_scores()
    
    #cette variable permet de stocker le score obtenu dans chaque partie
    score = 0
    
    
    while continuer != "n":
        partie += 1
        print("Chargement de la liste de mots à partir du fichier words.txt")
        print(len(functions.recuperer_liste_de_mots()), " mots chargés")
        print("Bienvenue dans le jeu Hangman!")
        niv = functions.choisir_niveau()
        mot_secret = functions.choisir_mot(niv)
        lettres_trouvees = []
        mot_masquer = functions.placerLettre(mot_secret, lettres_trouvees)
        tentative = data.tentative
        point_erreur = data.point_erreur
        alphabet = data.alphabet
        
        print("Vous avez choisi le niveau ", niv)
        print("Je pense à un mot de ", len(mot_secret), "lettres, à vous de deviner.")
        while mot_masquer != mot_secret and tentative > 0 :
            print("Il vous reste ", point_erreur, "point erreur(s)")
            print("Il vous reste ", tentative, "tentative(s)")
            print("lettres disponibles : ", alphabet )
            lettre = functions.saisir_lettre()
            if(lettre in lettres_trouvees):    #la lettre a été déjà devinée
                print("Oups, vous avez déjà deviné cette lettre")
                point_erreur -= 1  
                if point_erreur == 0: 
                    tentative -= 1
                alphabet = alphabet.replace(lettre, "")
                print("lettres disponibles : ", alphabet)
            elif lettre in mot_secret:        #la lettre est dans le mot à deviner;
                lettres_trouvees.append(lettre)
                alphabet = alphabet.replace(lettre, "")
                mot_masquer = functions.placerLettre(mot_secret, lettres_trouvees)
                print("Bon essai : ", mot_masquer)
                print("**************************************************************")
            elif lettre not in mot_secret and lettre in data.voyelle: 
                #la lettre est une voyelle qui n'est pas le mot à deviner. 
                print("Oups! Cette lettre n'est pas dans le mot secret : ", mot_masquer)
                if tentative > 1:
                  tentative -= 2
                else:
                  tentative = 0
                alphabet = alphabet.replace(lettre, "")
                print("Vous avez perdu 2 tentatives")
                print("lettres disponibles : ", alphabet)
                print("**************************************************************")
            elif not lettre.isalpha(): 
                #la lettre est un chiffre ou un symbole.
                print("Oups! Ce n'est pas une lettre valide : ", mot_masquer)
                if point_erreur > 0:
                  point_erreur -= 1
                else:
                  point_erreur = 0
                if point_erreur == 0:
                    if tentative > 0:s
                        tentative -= 1
                alphabet = alphabet.replace(lettre, "")
                print("Il vous reste ", point_erreur, " avertissement(s)")
                print("lettres disponibles : ", alphabet)
                print("**************************************************************")
            elif lettre not in mot_secret and lettre not in data.voyelle:
                #la lettre est une consonne qui n'est pas le mot à deviner
                print("Oups! Cette lettre n'est pas dans le mot secret : ", mot_masquer)
                tentative -= 1
                alphabet = alphabet.replace(lettre, "")
                print("Il vous reste ", tentative, " tentative(s)")
                print("lettres disponibles : ", alphabet)
                print("**************************************************************")
           
            mot_masquer = functions.placerLettre(mot_secret, lettres_trouvees)
            
            # A-t-on trouvé le mot ou le nombre de tentatives est épuisées?
            if(mot_masquer == mot_secret and tentative > 0):
                print("Félicitations! Vous avez gagné.")
                score = functions.calculer_score(tentative, mot_secret)
                print("score = ", score)
                break
            if tentative == 0:
                print("Pendu!!! vous avez perdu")
                print("le mot secret était : ", mot_secret)
                score = 0
        liste_scores[partie] = score        
        continuer = input("Voulez-vous jouer une autre partie ? (O/N): ")
        continuer = continuer.lower()
        
    # la partie est finie, on enregistre le score  
    functions.enregistrer_scores(liste_scores)
    
    # On  affiche les scores dans chaque partie
    print("\n\t\t Score final obtenu")
    print("\n\t\t**********************")
    for partie, score in liste_scores.items():
        print("\t\t     partie ", partie, ":", score,)        
    print("\t\t**********************")
            
            
            
             
        
