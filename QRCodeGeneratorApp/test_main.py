# test_main.py
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
