from bs4 import BeautifulSoup
import requests
import re

class Crawler():

    def aktueller_wert(self, link):
        suche = link
        link = requests.get("https://www.ariva.de/" + suche)
        doc = BeautifulSoup(link.text, "html.parser")
        ergebnis = doc.select(".first")[-1].text
        ergebnis = re.split(r"\s+", ergebnis)
        ergebnis = ergebnis[1]
        if "." in ergebnis:
            ergebnis = ergebnis.replace(".", "")
        if "," in ergebnis:
            ergebnis = ergebnis.replace(",", ".")
        return(ergebnis)




