from tkinter import *

maFenetre = Tk()
maFenetre.title("Morpion")

largeur = 300
hauteur = 300
Canevas = Canvas(maFenetre, width=largeur, height=hauteur, bg="white")
Canevas.pack(padx=5, pady=5)
Canevas.create_line(0, 100, 300, 100, fill="black", width=4)
Canevas.create_line(0, 200, 300, 200, fill="black", width=4)
Canevas.create_line(100, 300, 300, -100000, fill="black", width=4)
Canevas.create_line(200, 300, 300, -100000, fill="black", width=4)
Button(maFenetre, text="Quitter", command=maFenetre.destroy).pack(side=LEFT, padx=5, pady=5)
maFenetre.mainloop()

