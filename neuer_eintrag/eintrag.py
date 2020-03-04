from PyQt5 import QtWidgets
from neuer_eintrag.eintrag_data import Eintrag_Data
from uebersicht.uebersicht import Uebersicht

class Eintrag():
    def __init__(self, ui):
        self.eintrag_data = Eintrag_Data()
        self.ui = ui
        self.ui.eintrag_speichern.clicked.connect(self.speichern)
        self.ui.combo_art.currentTextChanged.connect(self.combo_eintraege)


    def combo_eintraege(self):
        auswahl = self.ui.combo_art.currentText()
        if auswahl == "Aktie" or auswahl == "Währung/Kryptowährung":
            self.ui.text_laufzeit.setVisible(False)
            self.ui.text_zinssatz.setVisible(False)
            self.ui.label_zinssatz.setVisible(False)
            self.ui.label_laufzeit.setVisible(False)
        else:
            self.ui.text_laufzeit.setVisible(True)
            self.ui.text_zinssatz.setVisible(True)
            self.ui.label_zinssatz.setVisible(True)
            self.ui.label_laufzeit.setVisible(True)

    def speichern(self):
        name = self.ui.text_name.text()
        url = self.ui.text_url.text()
        ausgabe = self.ui.text_ausgabe.text()
        anzahl = self.ui.text_anzahl.text()
        art = self.ui.combo_art.currentText()
        zinssatz = self.ui.text_zinssatz.text()
        laufzeit = self.ui.text_laufzeit.text()
        if zinssatz == "":
            zinssatz = 0
        if laufzeit == "":
            laufzeit = 0
        if "," in ausgabe:
            ausgabe = ausgabe.replace(",", ".")
        if "," in anzahl:
            anzahl = anzahl.replace(",", ".")

        self.eintrag_data.neuer_eintrag(name, url, ausgabe, anzahl, art, zinssatz, laufzeit)
        Uebersicht(self.ui).tabelle_fuellen()
        Uebersicht(self.ui).uebersicht_fuellen()