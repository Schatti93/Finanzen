from uebersicht.uebersicht_data import Uebersicht_Data
from uebersicht.crawler import Crawler
from PyQt5 import QtWidgets

class Uebersicht():
    def __init__(self, ui):
        self.ui = ui
        self.uebersicht_data = Uebersicht_Data()
        self.crawler = Crawler()
        self.uebersicht_fuellen()
        self.tabelle_fuellen()

    def uebersicht_fuellen(self):
        liste_der_anlagen = self.uebersicht_data.eigene_aktien_abfrage()
        ausgaben = 0.0
        wert = 0.0
        gewinn = 0.0
        for i in range(0, len(liste_der_anlagen)):
            if liste_der_anlagen[i][5] == "Währung/Kryptowährung" or liste_der_anlagen[i][5] == "Aktie":
                aktueller_wert = self.crawler.aktueller_wert(liste_der_anlagen[i][2])
                wert += float(aktueller_wert) * float(liste_der_anlagen[i][4])
            ausgaben += float(liste_der_anlagen[i][3])
        wert = round(wert, 2)
        ausgaben = round(ausgaben, 2)
        gewinn = round((wert - ausgaben), 2)
        self.ui.besitz.setText(str(wert))
        self.ui.besitz.setStyleSheet("color:#ffffff")
        self.ui.ausgaben.setText(str(ausgaben))
        self.ui.ausgaben.setStyleSheet("color:#ffffff")
        self.ui.gewinn.setText(str(gewinn))
        self.ui.gewinn.setStyleSheet("color:#ffffff")


    ### index bauen um das staendige webcrawling zu vermeiden
    def tabelle_fuellen(self):
        liste_der_anlagen = self.uebersicht_data.eigene_aktien_abfrage()
        liste_der_eintraege = []
        for i in range(0, len(liste_der_anlagen)):
            for p in range(0, len(liste_der_eintraege)):
                if liste_der_anlagen[i][2] in liste_der_anlagen[p]:
                    liste_der_eintraege[p][1] = liste_der_eintraege[p][1] + liste_der_anlagen[i][3]
                    liste_der_eintraege[p][2] = liste_der_eintraege[p][2] + liste_der_anlagen[i][4]
                    aktueller_wert = float(self.crawler.aktueller_wert(liste_der_anlagen[i][2])) * float(liste_der_anlagen[i][4])
                    aktueller_wert = round(aktueller_wert, 2)
                    liste_der_eintraege[p][3] += aktueller_wert
                else:
                    liste = []
                    liste.append(liste_der_anlagen[i][1])
                    liste.append(liste_der_anlagen[i][3])
                    liste.append(liste_der_anlagen[i][4])
                    aktueller_wert = float(self.crawler.aktueller_wert(liste_der_anlagen[i][2])) * float(liste_der_anlagen[i][4])
                    aktueller_wert = round(aktueller_wert, 2)
                    liste.append(aktueller_wert)
                    liste_der_eintraege.append(liste)
            if len(liste_der_eintraege) == 0:
                liste = []
                liste.append(liste_der_anlagen[i][1])
                liste.append(liste_der_anlagen[i][3])
                liste.append(liste_der_anlagen[i][4])
                aktueller_wert = float(self.crawler.aktueller_wert(liste_der_anlagen[i][2])) * float(liste_der_anlagen[i][4])
                aktueller_wert = round(aktueller_wert, 2)
                liste.append(float(aktueller_wert))
                liste_der_eintraege.append(liste)


        for i in range(0, len(liste_der_eintraege)):
            row = self.ui.invest_uebersicht.rowCount()
            self.ui.invest_uebersicht.insertRow(row)
            self.ui.invest_uebersicht.setItem(row, 0, QtWidgets.QTableWidgetItem(str(liste_der_eintraege[i][0])))
            self.ui.invest_uebersicht.setItem(row, 1, QtWidgets.QTableWidgetItem(str(liste_der_eintraege[i][2])))
            self.ui.invest_uebersicht.setItem(row, 2, QtWidgets.QTableWidgetItem(str(liste_der_eintraege[i][1])))
            self.ui.invest_uebersicht.setItem(row, 3, QtWidgets.QTableWidgetItem(str(liste_der_eintraege[i][3])))


