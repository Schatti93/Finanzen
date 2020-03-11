from PyQt5 import QtWidgets
from neuer_eintrag.eintrag_data import Eintrag_Data
from uebersicht.uebersicht import Uebersicht
import time

class Eintrag():
    def __init__(self, ui):
        self.eintrag_data = Eintrag_Data()
        self.ui = ui
        self.ui.eintrag_speichern.clicked.connect(self.aktien_speichern)
        self.ui.kredit_speichern.clicked.connect(self.kredit_speichern)
        self.ui.tages_speichern.clicked.connect(self.tagesgeld_speichern)
        self.combobox_url_auswahl()
        self.ui.url_combobox.currentTextChanged.connect(self.combo_changed)


    def combobox_url_auswahl(self):
        daten_holen = self.eintrag_data.eigene_aktien_abfrage()
        dict = {}
        liste = []

        for i in range(0, len(daten_holen)):
            if daten_holen[i][1] not in dict:
                eintrag = daten_holen[i][1] + ": " + daten_holen[i][2]
                liste.append(eintrag)

            dict[daten_holen[i][1]] = daten_holen[i][2]
        liste.append("andere")
        self.ui.url_combobox.addItems(liste)
        if len(liste) == 1:
            self.ui.url_label.setVisible(True)
            self.ui.text_url.setVisible(True)
        else:
            self.ui.url_label.setVisible(False)
            self.ui.text_url.setVisible(False)
            aktuelle_auswahl = self.ui.url_combobox.currentText()
            self.ui.text_url.setText(aktuelle_auswahl.split(": ")[1])

    def combo_changed(self):
        aktuelle_auswahl =  self.ui.url_combobox.currentText()
        if aktuelle_auswahl == "andere":
            self.ui.url_label.setVisible(True)
            self.ui.text_url.setVisible(True)
        else:
            self.ui.url_label.setVisible(False)
            self.ui.text_url.setVisible(False)
            self.ui.text_url.setText(aktuelle_auswahl.split(": ")[1])

    def aktien_speichern(self):
        name = self.ui.text_name.text()
        url = self.ui.text_url.text()
        ausgabe = self.ui.text_ausgabe.text()
        anzahl = self.ui.text_anzahl.text()
        art = self.ui.combo_art.currentText()

        if "," in ausgabe:
            ausgabe = ausgabe.replace(",", ".")
        if "," in anzahl:
            anzahl = anzahl.replace(",", ".")

        self.eintrag_data.neuer_eintrag(name, url, ausgabe, anzahl, art)
        Uebersicht(self.ui).uebersicht_waehrung()
        self.ui.error_eintrag.setText("Eintrag Gespeichert und Übersicht Aktualisiert")
        self.ui.error_eintrag.setStyleSheet("color:#ffffff; font-size:13pt; border: 2px solid green; border-radius: 5px; align= center")


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
        self.ui.error_kredit.setText("Eintrag Gespeichert und Übersicht Aktualisiert")
        self.ui.error_kredit.setStyleSheet("color:#ffffff; font-size:13pt; border: 2px solid green; border-radius: 5px; align= center")
        Uebersicht(self.ui).uebersicht_kredite()
        Uebersicht(self.ui).tabelle_fuellen_kredite()
        Uebersicht(self.ui).gesamt_anzeigen()


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
        self.ui.tages_error.setText("Eintrag Gespeichert und Übersicht Aktualisiert")
        self.ui.tages_error.setStyleSheet("color:#ffffff; font-size:13pt; border: 2px solid green; border-radius: 5px; align= center")
        Uebersicht(self.ui).uebersicht_tageszins()
        Uebersicht(self.ui).tabelle_fuellen_tages()
        Uebersicht(self.ui).gesamt_anzeigen()




