import sqlite3

class Eintrag_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def neuer_eintrag(self, name, url, ausgabe, anzahl, art, zinssatz, laufzeit):
        params = (name, url, ausgabe, anzahl, art, zinssatz, laufzeit)
        sql = "INSERT INTO anlagen VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()