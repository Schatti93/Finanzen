from uebersicht.uebersicht_data import Uebersicht_Data
from uebersicht.crawler import Crawler
import re

class Uebersicht():
    def __init__(self, ui):
        self.ui = ui
        self.uebersicht_data = Uebersicht_Data()
        self.ausgaben()
        self.crawler = Crawler()
        self.aktueller_wert_und_gewinn()

    def ausgaben(self):
        ausgaben = self.uebersicht_data.ausgaben()
        text = ausgaben[0][0]
        self.ui.ausgaben.setText(str(text))

    def aktueller_wert_und_gewinn(self):
        liste = self.uebersicht_data.eigene_aktien_abfrage()
        aktueller_wert_gesamt = 0
        tabellen_werte = {}
        for i in liste:
            wert = self.crawler.aktueller_wert(i[2])
            if "," in wert:
                if "." in wert:
                   wert = wert.replace(".", "")
                wert = wert.replace(",", ".")
                wert = float(wert)
            aktueller_wert_gesamt += wert * i[4]
            tabellen_werte[i[1]] = 

        self.ui.besitz.setText(str(aktueller_wert_gesamt))

        # Gesamt ausgaben holen und gewinn berechnen
        ausgaben = self.uebersicht_data.ausgaben()
        self.ui.gewinn.setText(str(aktueller_wert_gesamt - ausgaben[0][0]))





