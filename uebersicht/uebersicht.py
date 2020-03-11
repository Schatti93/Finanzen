from uebersicht.uebersicht_data import Uebersicht_Data
from uebersicht.crawler import Crawler
from PyQt5 import QtWidgets
from datetime import datetime



class Uebersicht():
    def __init__(self, ui):
        self.ui = ui
        self.uebersicht_data = Uebersicht_Data()
        self.crawler = Crawler()
        self.uebersicht_waehrung()
        self.uebersicht_tageszins()
        self.uebersicht_kredite()
        self.tabelle_fuellen_waehrung()
        self.tabelle_fuellen_kredite()
        self.tabelle_fuellen_tages()
        self.gesamt_anzeigen()
        self.ui.aktualisieren.clicked.connect(self.neu_laden)


    def general_abfrage_crawler(self):
        liste_der_anlagen = self.uebersicht_data.eigene_aktien_abfrage()
        anlagen_dictionary = {}
        for i in range(0, len(liste_der_anlagen)):
            if liste_der_anlagen[i][1] in anlagen_dictionary:
                pass
            else:
                aktueller_wert = self.crawler.aktueller_wert(liste_der_anlagen[i][2])
                anlagen_dictionary[liste_der_anlagen[i][1]] = aktueller_wert
        return anlagen_dictionary, liste_der_anlagen


    def uebersicht_waehrung(self):
        daten_holen = self.general_abfrage_crawler()
        liste_der_anlagen = daten_holen[1]
        dictionary = daten_holen[0]

        ausgaben = 0.0
        wert = 0.0
        gewinn = 0.0
        for i in range(0, len(liste_der_anlagen)):
            if liste_der_anlagen[i][5] == "Währung/Kryptowährung" or liste_der_anlagen[i][5] == "Aktie":
                aktueller_wert = dictionary[liste_der_anlagen[i][1]]
                wert += float(aktueller_wert) * float(liste_der_anlagen[i][4])
                ausgaben += float(liste_der_anlagen[i][3])

        wert = round(wert, 2)
        ausgaben = round(ausgaben, 2)
        gewinn = round((wert - ausgaben), 2)
        prozent = gewinn / (wert / 100)
        prozent = round(prozent, 2)
        self.ui.prozent.setText(str(prozent) + "%")
        self.ui.prozent.setStyleSheet("color:#ffffff")
        self.ui.besitz.setText(str(wert))
        self.ui.besitz.setStyleSheet("color:#ffffff")
        self.ui.ausgaben.setText(str(ausgaben))
        self.ui.ausgaben.setStyleSheet("color:#ffffff")
        self.ui.gewinn.setText(str(gewinn))
        self.ui.gewinn.setStyleSheet("color:#ffffff")

    def uebersicht_kredite(self):
        liste_der_kredite = self.uebersicht_data.eigene_kredite_abfragen()
        wert_kredit = 0.0
        ausgaben_kredit = 0.0
        gewinn_kredit = 0.0

        for i in range(0, len(liste_der_kredite)):
            ausgaben_kredit += liste_der_kredite[i][3]
            wert_kredit += (liste_der_kredite[i][6] / (liste_der_kredite[i][2] / liste_der_kredite[i][3])) * \
                           liste_der_kredite[i][5]
            if liste_der_kredite[i][8] == None:
                pass
            else:
                wert_kredit = wert_kredit - liste_der_kredite[i][8]


        gewinn_kredit += wert_kredit - ausgaben_kredit

        ausgaben_kredit = round(ausgaben_kredit, 2)
        wert_kredit = round(wert_kredit, 2)
        gewinn_kredit = round(gewinn_kredit, 2)
        prozent = gewinn_kredit / (wert_kredit / 100)
        prozent = round(prozent, 2)

        self.ui.prozent_kredit.setText(str(prozent) + "%")
        self.ui.prozent_kredit.setStyleSheet("color:#ffffff")
        self.ui.ausgaben_kredit.setText(str(ausgaben_kredit))
        self.ui.ausgaben_kredit.setStyleSheet("color:#ffffff")
        self.ui.summe_kredit.setText(str(wert_kredit))
        self.ui.summe_kredit.setStyleSheet("color:#ffffff")
        self.ui.gewinn_kredit.setText(str(gewinn_kredit))
        self.ui.gewinn_kredit.setStyleSheet("color:#ffffff")


    def uebersicht_tageszins(self):
        liste_der_tagesgelder = self.uebersicht_data.tageszins_abfrage()
        ausgaben = 0.0
        gesamt = 0.0
        gesamt_wert = 0.0
        gewinn = 0.0
        ausgaben_gesamt = 0.0
        for i in range(0, len(liste_der_tagesgelder)):
            ausgaben += liste_der_tagesgelder[i][2]
            datums_liste = liste_der_tagesgelder[i][4].split(".")
            zins = liste_der_tagesgelder[i][3]
            invest_datum = datetime(year = int(datums_liste[2]),
                                             month = int(datums_liste[1]),
                                             day = int(datums_liste[0]))

            differenz = datetime.now() - invest_datum

            for i in range(0, int(str(differenz.days))):
                if gesamt == 0.0:
                    gesamt = ((ausgaben * zins) / (100 * 360)) + ausgaben
                else:

                    zwischensumme = ((gesamt * zins) / (100 * 360)) + gesamt
                    gesamt = round(zwischensumme, 2)

            gesamt_wert += gesamt
            ausgaben_gesamt += ausgaben
            gesamt = 0.0
            ausgaben = 0.0



        gewinn = gesamt_wert - ausgaben_gesamt
        ausgaben_gesamt = round(ausgaben_gesamt, 2)
        gewinn = round(gewinn, 2)
        prozent = gewinn / (gesamt_wert / 100)
        prozent = round(prozent, 2)

        self.ui.tages_prozent.setText(str(prozent) + "%")
        self.ui.tages_prozent.setStyleSheet("color:#ffffff")
        self.ui.tages_ausgaben.setText(str(ausgaben_gesamt))
        self.ui.tages_ausgaben.setStyleSheet("color:#ffffff")
        self.ui.tages_hoehe.setText(str(gesamt_wert))
        self.ui.tages_hoehe.setStyleSheet("color:#ffffff")
        self.ui.tages_gewinn.setText(str(gewinn))
        self.ui.tages_gewinn.setStyleSheet("color:#ffffff")


    def tabelle_fuellen_waehrung(self):
        self.ui.invest_uebersicht.setRowCount(0)
        liste_der_eintraege = []
        daten_holen = self.general_abfrage_crawler()
        liste_der_anlagen = daten_holen[1]
        dict = daten_holen[0]


        for i in range(0, len(liste_der_anlagen)):

            liste = []
            liste.append(liste_der_anlagen[i][1])
            liste.append(liste_der_anlagen[i][3])
            liste.append(liste_der_anlagen[i][4])
            aktueller_wert = float(dict[liste_der_anlagen[i][1]]) * float(liste_der_anlagen[i][4])
            aktueller_wert = round(aktueller_wert, 2)
            liste.append(aktueller_wert)
            liste_der_eintraege.append(liste)

            if len(liste_der_eintraege) == 0:
                liste = []
                liste.append(liste_der_anlagen[i][1])
                liste.append(liste_der_anlagen[i][3])
                liste.append(liste_der_anlagen[i][4])
                aktueller_wert = float(dict[liste_der_anlagen[i][2]]) * float(liste_der_anlagen[i][4])
                aktueller_wert = round(aktueller_wert, 2)
                liste.append(float(aktueller_wert))
                liste_der_eintraege.append(liste)

            else:
                pass


        for i in range(0, len(liste_der_eintraege)):
            row = self.ui.invest_uebersicht.rowCount()
            self.ui.invest_uebersicht.insertRow(row)
            anzahl = round(liste_der_eintraege[i][2], 4)
            wert = round(liste_der_eintraege[i][1], 2)
            self.ui.invest_uebersicht.setItem(row, 0, QtWidgets.QTableWidgetItem(str(liste_der_eintraege[i][0])))
            self.ui.invest_uebersicht.setItem(row, 1, QtWidgets.QTableWidgetItem(str(anzahl)))
            self.ui.invest_uebersicht.setItem(row, 2, QtWidgets.QTableWidgetItem(str(wert)))
            self.ui.invest_uebersicht.setItem(row, 3, QtWidgets.QTableWidgetItem(str(liste_der_eintraege[i][3])))


    def tabelle_fuellen_kredite(self):
        self.ui.kredit_uebersicht.setRowCount(0)
        liste_der_daten = self.uebersicht_data.eigene_kredite_abfragen()
        wert_kredit = 0.0
        for i in range(0, len(liste_der_daten)):
            row = self.ui.kredit_uebersicht.rowCount()
            self.ui.kredit_uebersicht.insertRow(row)
            self.ui.kredit_uebersicht.setItem(row, 0, QtWidgets.QTableWidgetItem(str(liste_der_daten[i][1])))
            self.ui.kredit_uebersicht.setItem(row, 1, QtWidgets.QTableWidgetItem(str(liste_der_daten[i][3])))
            self.ui.kredit_uebersicht.setItem(row, 2, QtWidgets.QTableWidgetItem(str(liste_der_daten[i][5])))
            self.ui.kredit_uebersicht.setItem(row, 3, QtWidgets.QTableWidgetItem(str(liste_der_daten[i][4])))
            wert_kredit += (liste_der_daten[i][6] / (liste_der_daten[i][2] / liste_der_daten[i][3])) * \
                           liste_der_daten[i][5]
            wert_kredit = wert_kredit - liste_der_daten[i][3]
            wert_kredit = round(wert_kredit, 2)
            self.ui.kredit_uebersicht.setItem(row, 4, QtWidgets.QTableWidgetItem(str(wert_kredit)))
            wert_kredit = 0.0



    def tabelle_fuellen_tages(self):
        self.ui.tages_uebersicht.setRowCount(0)
        liste_der_daten = self.uebersicht_data.tageszins_abfrage()
        ausgaben = 0.0
        gesamt = 0.0
        gesamt_wert = 0.0
        gewinn = 0.0
        ausgaben_gesamt = 0.0
        for i in range(0, len(liste_der_daten)):
            ausgaben += liste_der_daten[i][2]
            datums_liste = liste_der_daten[i][4].split(".")
            zins = liste_der_daten[i][3]
            invest_datum = datetime(year=int(datums_liste[2]),
                                    month=int(datums_liste[1]),
                                    day=int(datums_liste[0]))

            differenz = datetime.now() - invest_datum

            for p in range(0, int(str(differenz.days))):
                if gesamt == 0.0:
                    gesamt = ((ausgaben * zins) / (100 * 360)) + ausgaben
                else:

                    zwischensumme = ((gesamt * zins) / (100 * 360)) + gesamt
                    gesamt = round(zwischensumme, 2)

            gewinn = gesamt - ausgaben
            gewinn = round(gewinn, 2)
            row = self.ui.tages_uebersicht.rowCount()
            self.ui.tages_uebersicht.insertRow(row)
            self.ui.tages_uebersicht.setItem(row, 0, QtWidgets.QTableWidgetItem(str(liste_der_daten[i][1])))
            self.ui.tages_uebersicht.setItem(row, 1, QtWidgets.QTableWidgetItem(str(liste_der_daten[i][2])))
            self.ui.tages_uebersicht.setItem(row, 2, QtWidgets.QTableWidgetItem(str(liste_der_daten[i][3])))
            self.ui.tages_uebersicht.setItem(row, 3, QtWidgets.QTableWidgetItem(str(gewinn)))
            self.ui.tages_uebersicht.setItem(row, 4, QtWidgets.QTableWidgetItem(str(differenz.days)))

            gesamt = 0.0
            ausgaben = 0.0

    def gesamt_anzeigen(self):
        waehrung_gewinn = self.ui.gewinn.text()
        kredit_gewinn = self.ui.gewinn_kredit.text()
        tages_gewinn = self.ui.tages_gewinn.text()

        gewinn_gesamt = float(waehrung_gewinn) + float(kredit_gewinn) + float(tages_gewinn)
        gewinn_gesamt = round(gewinn_gesamt, 2)
        self.ui.gesamt_gewinn.setText(str(gewinn_gesamt) + "€")
        if gewinn_gesamt >= 0:
            self.ui.gesamt_gewinn.setStyleSheet("color:#ffffff; font-size:64pt; border: 2px solid green; border-radius: 5px; align= center")
        else:
            self.ui.gesamt_gewinn.setStyleSheet("color:#ffffff; font-size:64pt; border: 2px solid red; border-radius: 5px; align= center")

        ausgaben_waehrung = self.ui.ausgaben.text()
        ausgaben_kredite = self.ui.ausgaben_kredit.text()
        ausgaben_tages = self.ui.tages_ausgaben.text()
        ausgaben_gesamt = float(ausgaben_kredite) + float(ausgaben_tages) + float(ausgaben_waehrung)
        ausgaben_gesamt = round(ausgaben_gesamt, 2)
        self.ui.gesamt_ausgaben.setText(str(ausgaben_gesamt) + "€")
        self.ui.gesamt_ausgaben.setStyleSheet("color:#ffffff; font-size:64pt; border: 2px solid black; border-radius: 5px; align= center")

        prozent_tages = self.ui.tages_prozent.text().split("%")
        prozent_kredit = self.ui.prozent_kredit.text().split("%")
        prozent_waehrung = self.ui.prozent.text().split("%")

        gesamt_prozent = (float(prozent_tages[0]) + float(prozent_kredit[0]) + float(prozent_waehrung[0])) / 3
        gesamt_prozent = round(gesamt_prozent, 2)
        self.ui.gesamt_prozent.setText(str(gesamt_prozent) + "%")
        self.ui.gesamt_prozent.setStyleSheet("color:#ffffff; font-size:64pt; border: 2px solid black; border-radius: 5px; align= center")

    def neu_laden(self):

        self.tabelle_fuellen_waehrung()
        self.uebersicht_waehrung()
        self.gesamt_anzeigen()

