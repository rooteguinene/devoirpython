#Natanael Alberto Ndong MBOUYU EKO

print("***************************************")
print("* Système de contrôle des congés  *")
print("*************************************** \n")

nom_de_employe = input("Veuillez entrer le nom de l'employé : ")
cle_departement = int(input("Veuillez entrer la clé du département : "))
ancienete = float(input("Veuillez entrer les nombres d'annees d'exercices dans la fonction: "))

if cle_departement == 1 :

    if ancienete == 1 and ancienete < 2:
        print("L'employé ", nom_de_employe, " a droit à 6 jours de congés.")
    elif ancienete >= 2 and ancienete <= 6:
        print("L'employé ", nom_de_employe, " a droit à 14 jours de congés.")
    elif ancienete >= 7:
        print("L'employé ", nom_de_employe, " a droit à 20 jours de congés.")
    else:
        print("L'employé ", nom_de_employe, " n'a pas encore droit aux congés.")

elif cle_departement == 2:

    if ancienete == 1 and ancienete < 2:
        print("L'employé ", nom_de_employe, " a droit à 7 jours de congés.")
    elif ancienete >= 2 and ancienete <= 6:
        print("L'employé ", nom_de_employe, "a droit à 15 jours de congés.")
    elif ancienete >= 7:
        print("L'employé ", nom_de_employe, " a droit à 22 jours de congés.")
    else:
        print("L'employé ", nom_de_employe, " n'a pas encore droit aux congés.")

elif cle_departement == 3:

    if ancienete == 1 and ancienete < 2:
        print("L'employé ", nom_de_employe, " a droit à 10 jours de congés.")
    elif ancienete >= 2 and ancienete <= 6:
        print("L'employé ", nom_de_employe, " a droit à 20 jours de congés.")
    elif ancienete >= 7:
        print("L'employé ", nom_de_employe, " a droit à 30 jours de congés.")
    else:
        print("L'employé ", nom_de_employe, " n'a pas encore droit aux congés.")

else:
    print("La clé de département n'existe pas, veuillez réessayer.")