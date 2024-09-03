import os

# Chemin de base où l'arborescence sera créée
base_path = "./Exercices"

# Dictionnaire des exercices par page
exercices = {
    "Page 6": ["P6_Ex1.py", "P6_Ex2.py", "P6_Ex3.py", "P6_Ex4.py", "P6_Ex5.py", "P6_Ex6.py", "P6_Ex7.py", "P6_Ex8.py", "P6_Ex9.py"],
    "Page 7": ["P7_Ex1.py", "P7_Ex2.py", "P7_Ex3.py", "P7_Ex4.py", "P7_Ex5.py"],
    "Page 8": ["P8_Ex1.py"],
    "Page 9": ["P9_Ex1.py"],
    "Page 11": ["P11_Ex1.py", "P11_Ex2.py", "P11_Ex3.py", "P11_Ex4.py", "P11_Ex5.py"],
    "Page 12": ["P12_Ex1.py", "P12_Ex2.py", "P12_Ex3.py", "P12_Ex4.py"],
    "Page 13": ["P13_Ex1.py"],
    "Page 14": ["P14_Ex1.py"],
    "Page 15": ["P15_Ex1.py"],
    "Page 16": ["P16_Ex1.py", "P16_Ex2.py", "P16_Ex3.py", "P16_Ex4.py", "P16_Ex5.py", "P16_Ex6.py", "P16_Ex7.py", "P16_Ex8.py"],
    "Page 17": ["P17_Ex1.py", "P17_Ex2.py", "P17_Ex3.py", "P17_Ex4.py", "P17_Ex5.py", "P17_Ex6.py", "P17_Ex7.py", "P17_Ex8.py"],
    "Page 19": ["P19_Ex1.py", "P19_Ex2.py"],
    "Page 20": ["P20_Ex1.py", "P20_Ex2.py", "P20_Ex3.py", "P20_Ex4.py", "P20_Ex5.py"],
    "Page 21": ["P21_Ex1.py"],
    "Page 22": ["P22_Ex1.py"],
    "Page 23": ["P23_Ex1.py"],
    "Page 24": ["P24_Ex1.py", "P24_Ex2.py", "P24_Ex3.py", "P24_Ex4.py", "P24_Ex5.py"],
    "Page 25": ["P25_Ex1.py", "P25_Ex2.py", "P25_Ex3.py", "P25_Ex4.py", "P25_Ex5.py"],
    "Page 26": ["P26_Ex1.py", "P26_Ex2.py", "P26_Ex3.py", "P26_Ex4.py"]
}

# Création des dossiers et fichiers
for page, files in exercices.items():
    page_path = os.path.join(base_path, page.replace(" ", "_"))
    os.makedirs(page_path, exist_ok=True)
    for file_name in files:
        file_path = os.path.join(page_path, file_name)
        with open(file_path, 'w') as f:
            f.write(f"# Code par Elvin Mouyart 5Tb\nFini = False\n# {file_name.split('.')[0]}\n")

print("Arborescence des exercices créée avec succès!")
