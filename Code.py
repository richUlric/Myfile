import csv

def ajouter_identifiant(id, mdp):
    with open('identifiants.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, mdp])

# Exemple d'utilisation :
ajouter_identifiant("john.doe", "password123")

def verifier_identifiants(id_utilisateur, mot_de_passe):
    with open('fichier_identifiants.csv', mode='r') as fichier:
        lecteur_csv = csv.reader(fichier)
        for ligne in lecteur_csv:
            if ligne[0] == id_utilisateur and ligne[1] == mot_de_passe:
                return True
    return False
