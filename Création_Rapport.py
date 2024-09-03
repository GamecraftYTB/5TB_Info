import os

# Chemin de base où l'arborescence est créée
base_path = "./Exercices"
rapport_file = "rapport_exercices.txt"

# Fonction pour vérifier l'état d'un exercice
def verifier_etat_exercice(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("Fini"):
                return "✅ Terminé" if "True" in line else "❌ Non terminé"
    return "❌ Non trouvé"

# Fonction pour trier les dossiers par numéro de page
def trier_par_numero(dossier):
    numero = dossier.split('_')[1]
    return int(numero)

# Création du rapport
with open(rapport_file, 'w', encoding='utf-8') as rapport:
    rapport.write("===== 📊 Rapport des Exercices 📊 =====\n\n")
    
    # Récupérer et trier les dossiers par numéro de page
    dossiers = sorted(next(os.walk(base_path))[1], key=trier_par_numero)
    
    for dossier in dossiers:
        rapport.write(f"📂 **{dossier}**\n")
        rapport.write("=" * (len(dossier) + 6) + "\n")
        chemin_dossier = os.path.join(base_path, dossier)
        fichiers = os.listdir(chemin_dossier)
        
        for file_name in sorted(fichiers):
            file_path = os.path.join(chemin_dossier, file_name)
            etat = verifier_etat_exercice(file_path)
            rapport.write(f"   • {file_name}: {etat}\n")
        
        rapport.write("\n")

rapport.write("\n===== Fin du Rapport =====\n")

print(f"Rapport des exercices généré avec succès dans {rapport_file}!")
