from PyQt5 import QtWidgets
from neuer_eintrag.eintrag_data import Eintrag_Data
from uebersicht.uebersicht import Uebersicht

class Eintrag():
    def __init__(self, ui):
        self.eintrag_data = Eintrag_Data()
        self.ui = ui
        self.ui.eintrag_speichern.clicked.connect(self.aktien_speichern)
        self.ui.combo_art.currentTextChanged.connect(self.combo_eintraege)
        self.ui.kredit_speichern.clicked.connect(self.kredit_speichern)
        self.ui.tages_speichern.clicked.connect(self.tagesgeld_speichern)


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

    def aktien_speichern(self):
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
        #Uebersicht(self.ui).tabelle_fuellen()
        Uebersicht(self.ui).uebersicht_waehrung()

    def kredit_speichern(self):
        name = self.ui.kredit_name.text()
        hoehe = self.ui.kredit_hoehe.text()
        invest = self.ui.kredit_invest.text()
        zins = self.ui.kredit_zins.text()
        laufzeit = self.ui.kredit_laufzeit.text()
        rate = self.ui.kredit_rate.text()
        datum = self.ui.kredit_datum.text()
        kosten = self.ui.kredit_kosten.text()

        if "," in hoehe:
            invest = hoehe.replace(",", ".")
        if "," in invest:
            invest = invest.replace(",", ".")
        if "," in zins:
            zins = zins.replace(",", ".")
        if "," in rate:
            rate = rate.replace(",", ".")
        if "," in kosten:
            kosten = kosten.replace(",", ".")

        self.eintrag_data.neuer_eintrag_kredit(name, hoehe, invest, zins, laufzeit, rate, datum, kosten)
        Uebersicht(self.ui).uebersicht_kredite()

    def tagesgeld_speichern(self):
        name = self.ui.tages_name.text()
        hoehe = self.ui.tages_wert.text()
        zins = self.ui.tages_zins.text()
        datum = self.ui.tages_datum.text()

        if "," in hoehe:
            invest = hoehe.replace(",", ".")
        if "," in zins:
            zins = zins.replace(",", ".")

        self.eintrag_data.tagesgeld_speichern(name, hoehe, zins, datum)
