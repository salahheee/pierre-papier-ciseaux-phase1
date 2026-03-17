# 1️⃣ Importer les bibliothèques nécessaires
import tkinter as tk
import random

# 2️⃣ Initialiser la fenêtre du jeu avec dimensions et titre
window = tk.Tk()
window.title("Jeu Pierre Papier Ciseaux")  # Titre
window.geometry("400x300")                  # Dimensions

# 3️⃣ Définir la couleur d’arrière-plan
window.config(bg="lightblue")

# 4️⃣ Créer une étiquette pour le titre du jeu
title_label = tk.Label(window, text="Pierre Papier Ciseaux", font=("Arial", 16), bg="lightblue")
title_label.pack(pady=10)

# 5️⃣ Demander à l’utilisateur de choisir entre pierre, papier ou ciseaux
# On affiche simplement le texte d’instruction
instruction_label = tk.Label(window, text="Choisissez : Pierre, Papier ou Ciseaux", bg="lightblue")
instruction_label.pack(pady=5)

# 6️⃣ Créer un champ d’entrée pour que l’utilisateur puisse saisir son choix
user_entry = tk.Entry(window)
user_entry.pack(pady=5)

# 7️⃣ Générer une sélection aléatoire pour l’ordinateur
choices = ["Pierre", "Papier", "Ciseaux"]
comp_pick = random.choice(choices)  # 8️⃣ Attribuer à la variable comp_pick

# (Optionnel) afficher la sélection de l'ordi pour tester
# print("Choix de l'ordinateur:", comp_pick)

# Lancement de la fenêtre
window.mainloop()
