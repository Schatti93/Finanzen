import sqlite3

class Uebersicht_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database Kopie.db")
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def ausgaben(self):
        sql = "SELECT Ausgaben FROM uebersicht"
        self.c.execute(sql)
        return self.c.fetchall()

    def eigene_aktien_abfrage(self):
        sql = "Select * FROM anlagen"
        self.c.execute(sql)
        return self.c.fetchall()

    def eigene_kredite_abfragen(self):
        sql = "SELECT * FROM Kredite"
        self.c.execute(sql)
        return self.c.fetchall()

    def tageszins_abfrage(self):
        sql = "SELECT * FROM tagesgeld"
        self.c.execute(sql)
        return self.c.fetchall()

