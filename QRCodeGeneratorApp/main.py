# By Javier Perez Mota

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Générateur de QR Code") #Titre de la fenêtre
        master.geometry("600x500")  # Taille de la fenêtre

        #Texte invitant l'utilisateur à saisir une URL
        self.label = tk.Label(master, text="Veuillez entrer une adresse URL pour générer un QR Code :", font=("Helvetica", 12))
        self.label.pack(pady=10) #Place le label avec un espacement vertical de 10 pixels
        #Créer un champ ou l'utilisateur peut saisir une URL
        self.entry = tk.Entry(master, font=("Helvetica", 12), width=40) # Font texte
        self.entry.pack(pady=5) #Espacement vertical
        #Créer un bouton permettant de générer le QR Code
        self.generate_button = tk.Button(master, text="Générer QR Code", font=("Helvetica", 12), command=self.generate_qr_code) #Si le bouton est cliqué appel la fonction generate_qr_code
        self.generate_button.pack(pady=10)

        self.image_label = tk.Label(master) #Créer un label pour afficher l'image du QR Code
        self.image_label.pack()

    #Cette méthode sera appelée lorsque l'utilisateur cliquera sur le bouton pour générer le QR Code.
    #Définition de la methode generate_qr_code
    def generate_qr_code(self):
        url = self.entry.get() # Récuperation de l'url entré par l'utilisateur
        if url: # Si URL entré par l'utilisateur, alors ...
            #Crée un objet QRCode avec des paramètres spécifiques :
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(url) # Ajoute l'URL au QR Code et ajuste la taille du QR Code pour s'adapter aux données
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white") # Crée une image du QR Code avec des couleurs spécifiques.

            img = img.resize((300, 300))  # Redimensionner l'image du QR code
            #Affichage de l'image en un format compatible
            self.qr_image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.qr_image)
        else: # Si pas de URL entré alors ...
            messagebox.showwarning("Avertissement", "Veuillez entrer une adresse URL pour générer un QR Code.") # Boîte de dialogue

def main():  #Définition de la fonction main/ Execution du programme
    root = tk.Tk() # Initialise Tkinter - root contiendra tous les éléments de l'interface graphique
    app = QRCodeGeneratorApp(root) # Création de l'instance de la classe , en passant root comme argument cela déclenche le constructeur de la classe, qui configure l'interface Utilisateur
    root.mainloop() # Boucle d'événement de tkinter permettant d'attendre les interactions de l'utilisateur clics, clavier etc...

if __name__ == "__main__": # Permet de vérifier si ce script est exécuté en tant que programme principal ou non
    main() # Si le script est exécuté directement __name__ prend la valeur __main__ ce qui signifie que la fonction main() sera appelée
    #Si la condition précédente est vraie la dernière ligne exécute la fonction main(), demarrant ainsi l'application