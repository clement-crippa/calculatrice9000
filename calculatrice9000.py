from tkinter import *


# Résultat des calculs
def calculer(formule):
    try:
        formule = formule.replace("²`", "**2")
        formule = formule.replace("%", "/100")
        formule = formule.replace("√", "**0.5")
        resultat = str(eval(formule))
        with open("historique.txt", "a") as file:
            file.write(formule + " = " + resultat + "\n")
        return resultat
    except:
        return "Erreur"


# Configuration des boutons pour les opérationq
def bouton_special(calcule):
    global formule
    if calcule == "C":
        formule = ""
    elif calcule == "<-":
        formule = formule[0:-1]
    elif calcule == "²":
        formule += "**2"
    elif calcule == "%":
        formule += "/100"
    elif calcule == "=":
        formule = calculer(formule)
    elif calcule == "√":
        formule += "**0.5"
    else:
        if formule == "0":
            formule = ""
        formule += calcule
    actualisation()


# Remet a zéro l'affichage après avoir effacé un calcul
def actualisation():
    global formule, label_principal
    if formule == "":
        formule = "0"
    label_principal.configure(text=formule)


# Fenêtre Historique
def historique():
    fenetre_historique = Tk()
    fenetre_historique.title("Historique")
    with open("historique.txt", "r") as file:
        historique = file.read()
    historique_label = Label(fenetre_historique, text=historique)
    historique_label.pack()

    # Bouton pour effacer l'historique
    def effacer_historique():
        with open("historique.txt", "w") as file:
            file.write("")
        historique_label.config(text="")

    bouton_effacer = Button(fenetre_historique, text="Effacer l'historique", bg="Red", font=("", 15),
                            command=effacer_historique)
    bouton_effacer.pack()
    fenetre_historique.mainloop()


# Calculatrice
root = Tk()
root["bg"] = "Black"
root.geometry("485x630")
root.title("Calculatrice")
root.resizable(False, False)
formule = "0"
# Affichage des calcule
label_principal = Label(text=formule, font=("", 21), bg="Black", foreground="White")
label_principal.place(x=11, y=50)
# Boutons de la calculatrice
boutons = [
    "C", "<-", "*", "=",
    "1", "2", "3", "/",
    "4", "5", "6", "+",
    "7", "8", "9", "-",
    "(", "0", ")", "²",
    "%", "√", "."
]

x = 10
y = 140
# Positionnement des boutons
for bouton in boutons:
    z = lambda bouton=bouton: bouton_special(bouton)
    Button(text=bouton, bg="Orange", font=("", 20), command=z).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 10
        y += 81
# Bouton Historique
bouton_historique = Button(root, text="Historique", bg="Gray", font=("", 15), command=historique)
bouton_historique.place(x=360, y=50, width=115, height=79)



# Fonction pour fermer la calculatrice via un bouton
def fermer():
    root.destroy()


# Bouton pour fermer la calculatrice
z = lambda bouton="Fermer": fermer()
Button(text="Fermer", bg="Red", font=("", 20), command=z).place(x=x, y=y, width=115, height=79)

root.mainloop()
