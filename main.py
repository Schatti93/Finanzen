import sys
from PyQt5 import QtWidgets
from ui.finanzen.mainwindow import Ui_MainWindow
from neuer_eintrag.eintrag import Eintrag
from uebersicht.uebersicht import Uebersicht


app = QtWidgets.QApplication(sys.argv)
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Finanzen")
        self.uebersicht = Uebersicht(self.ui)
        self.eintrag = Eintrag(self.ui)


window = MainWindow()
window.show()
sys.exit(app.exec_())
