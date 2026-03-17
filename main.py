import tkinter as tk
import random

# Création de la fenêtre principale
window = tk.Tk()
window.title("Pierre Papier Ciseaux - Phase 2")
window.geometry("400x350")
window.config(bg="lightblue")

# Labels pour le titre et les instructions
title_label = tk.Label(window, text="Pierre Papier Ciseaux", font=("Arial", 16), bg="lightblue")
title_label.pack(pady=10)

instruction_label = tk.Label(window, text="Choisis : Pierre, Papier ou Ciseaux", bg="lightblue")
instruction_label.pack(pady=5)

# Champ de saisie pour l'utilisateur
user_entry = tk.Entry(window)
user_entry.pack(pady=5)

# Label pour afficher le résultat
result_label = tk.Label(window, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=10)

# Fonction pour jouer un tour
def play():
    user_choice = user_entry.get().capitalize()
    choices = ["Pierre", "Papier", "Ciseaux"]

    if user_choice not in choices:
        result_label.config(text="❌ Choix invalide !")
        return

    comp_choice = random.choice(choices)

    # Déterminer le gagnant
    if user_choice == comp_choice:
        result = "⚖️ Égalité"
    elif (user_choice == "Pierre" and comp_choice == "Ciseaux") or \
         (user_choice == "Ciseaux" and comp_choice == "Papier") or \
         (user_choice == "Papier" and comp_choice == "Pierre"):
        result = "🎉 Tu gagnes !"
    else:
        result = "💻 L'ordinateur gagne !"

    # Affichage du résultat
    result_label.config(text=f"Toi : {user_choice}  |  Ordi : {comp_choice}\n{result}")

# Fonction pour réinitialiser le jeu
def Reset():
    user_entry.delete(0, tk.END)
    result_label.config(text="")

# Fonction pour quitter l'application
def Exit():
    window.destroy()

# Boutons
play_button = tk.Button(window, text="Jouer", command=play)
play_button.pack(pady=5)

reset_button = tk.Button(window, text="Réinitialiser", command=Reset)
reset_button.pack(pady=5)

exit_button = tk.Button(window, text="Quitter", command=Exit)
exit_button.pack(pady=5)

window.mainloop()
