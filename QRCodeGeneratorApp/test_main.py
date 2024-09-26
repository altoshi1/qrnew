"""# test_main.py
import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from main import QRCodeGeneratorApp

class TestQRCodeGeneratorApp(unittest.TestCase):

    @patch('tkinter.messagebox.showwarning')
    def test_generate_qr_code_empty_url(self, mock_showwarning):
        app = QRCodeGeneratorApp(tk.Tk())
        app.entry.insert(0, "")  # Pas d'URL entrée
        app.generate_qr_code()
        mock_showwarning.assert_called_once_with("Avertissement", "Veuillez entrer une adresse URL pour générer un QR Code.")

    def test_generate_qr_code_valid_url(self):
        app = QRCodeGeneratorApp(tk.Tk())
        valid_url = "https://www.example.com"
        app.entry.insert(0, valid_url)

        # Simuler image_label et PhotoImage
        app.image_label = MagicMock()
        app.qr_image = MagicMock()

        # Appeler la méthode pour générer le QR Code
        app.generate_qr_code()

        # Vérifier que l'image du QR code a été générée
        self.assertIsNotNone(app.qr_image)
        # Vérifier que l'image a été configurée
        app.image_label.config.assert_called_once()

if __name__ == '__main__':
    unittest.main()
"""


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
        self.app.entry.get.return_value = 'http://exemple.com' # simule le retour de l'entrée clavier de l'utilisateur pour retourner une url valide

        #
        with patch('PIL.ImageTk.PhotoImage') as mock_photo_image: # On utilise patch pour remplacer ImageTk.PhotoImage par mock_photo_image pour éviter d'exectuer le code réel et eviter les erreurs
            self.app.generate_qr_code() #appel de la méthode qui génère le QR Code

        self.assertEqual(self.app.entry.get(), 'http://exemple.com') #Vérifie que la valeur renvoyée par entry.get() est bien l'url que nous avons simulée
        mock_photo_image.assert_called_once()  # vérifie que la méthode PhotoImage a été appelée une fois pendant le test

    @patch('tkinter.messagebox.showwarning') # on remplace showwarning et on simule les avertissement
    def test_empty_url(self, mock_warning): # Déclaration de la méthode URL Vide
        self.app.entry.get.return_value = '' # Simule le retour clavier utilisateur pour qu'il soit vide

        with patch('PIL.ImageTk.PhotoImage'):  #on re-simule PhotoImage pour eviter les erreurs
            self.app.generate_qr_code() # On génère le Qr Code
        #On vérifie que showwarning a été appelé une fois avec le message identique spécifié ci-dessous
        mock_warning.assert_called_once_with("Avertissement",
                                             "Veuillez entrer une adresse URL pour générer un QR Code.")

#Execution du script
if __name__ == '__main__':
    unittest.main()
