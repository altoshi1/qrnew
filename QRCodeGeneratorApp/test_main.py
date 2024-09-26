# POUR INSTALLER DEPUIS TERMINAL LINUX -> apt install python3-pillow

from unittest.mock import MagicMock, patch
import unittest
from main import QRCodeGeneratorApp


class TestQRCodeURL(unittest.TestCase): # création d'une nouvelle classe de test qui hérite de unittest.testcase

    def setUp(self): #configuration de l'environnement de test et de mock
        self.master_mock = MagicMock() # création d'un mock pour simuler le fichier maître - main.py
        self.app = QRCodeGeneratorApp(self.master_mock) # on insere dans master mock la class principale QRCodeGeneratorApp
        self.app.entry = MagicMock() # remplace la zone de saisie par un mock pour simuler les interactions avec celle-ci

    def test_valid_url(self): # déclaration de la méthode test_valid_url
        self.app.entry.get.return_value = 'http://esgi.com' # simule le retour de l'entrée clavier de l'utilisateur pour retourner une url valide

        #
        with patch('PIL.ImageTk.PhotoImage') as mock_photo_image: # On utilise patch pour remplacer ImageTk.PhotoImage par mock_photo_image pour éviter d'exectuer le code réel et eviter les erreurs
            self.app.generate_qr_code() #appel de la méthode qui génère le QR Code

        self.assertEqual(self.app.entry.get(), 'http://esgi.com') #Vérifie que la valeur renvoyée par entry.get() est bien l'url que nous avons simulée
        mock_photo_image.assert_called_once()  # vérifie que la méthode PhotoImage a été appelée une fois pendant le test

    @patch('tkinter.messagebox.showwarning') # on remplace showwarning et on simule les avertissement
    def test_empty_url(self, mock_warning): # Déclaration de la méthode URL Vide
        self.app.entry.get.return_value = '' # Simule le retour clavier utilisateur pour qu'il soit vide

        with patch('PIL.ImageTk.PhotoImage'):  #on re-simule PhotoImage pour eviter les erreurs
            self.app.generate_qr_code() # On génère le Qr Code
        #On vérifie que showwarning a été appelé une fois avec le message identique spécifié ci-dessous
        mock_warning.assert_called_once_with("Avertissement",
                                             "Veuillez entrer une adresse URL pour générer un QR Code.")

    def test_image_taille(self):
        # Remplace l'objet PhotoImage de PIL par un mock pour éviter de charger de vraies images
        with patch('PIL.ImageTk.PhotoImage') as mock_photo_image:
            # Crée un mock pour simuler un objet image
            mock_image = MagicMock()
            # Configure le mock PhotoImage pour renvoyer notre mock d'image
            mock_photo_image.return_value = mock_image

            # Définit le comportement du mock d'image pour renvoyer une largeur de 300 pixels
            mock_image.width.return_value = 300
            # Définit le comportement du mock d'image pour renvoyer une hauteur de 300 pixels
            mock_image.height.return_value = 300

            # Appelle la méthode qui génère le QR Code, ce qui devrait utiliser le mock d'image
            self.app.generate_qr_code()
            self.assertIsNotNone(self.app.qr_image) #Verifie que l'image du qr code a été crée
            # Vérifie que la largeur de l'image générée est bien de 300 pixels
            self.assertEqual(mock_image.width(), 300)
            # Vérifie que la hauteur de l'image générée est bien de 300 pixels
            self.assertEqual(mock_image.height(), 300)

    def test_couleur_QRCode(self):
        with patch('PIL.ImageTk.PhotoImage') as mock_photo_image:

            mock_image = MagicMock()
            mock_photo_image.return_value = mock_image

            mock_image.fill_color.return_value = "black"
            # Définit le comportement du mock d'image pour renvoyer une hauteur de 300 pixels
            mock_image.back_color.return_value = "white"

            self.app.generate_qr_code()
            self.assertIsNotNone(self.app.qr_image)

            self.assertEqual(mock_image.fill_color(), "black")
            self.assertEqual(mock_image.back_color(), "white")

#Execution du script
if __name__ == '__main__':
    unittest.main()
