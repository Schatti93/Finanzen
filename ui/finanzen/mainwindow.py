# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/finanzen/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1560, 800)
        MainWindow.setStyleSheet("background-color: rgb(128, 127, 129)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, 0, 1561, 771))
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    \n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
" border: 1px solid black;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #58AFB3, stop: 0.3 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);\n"
"    color: black;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 471, 100))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 4, 1, 1, 1)
        self.line_21 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout.addWidget(self.line_21, 3, 6, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 2, 1, 1)
        self.besitz = QtWidgets.QLabel(self.gridLayoutWidget)
        self.besitz.setObjectName("besitz")
        self.gridLayout.addWidget(self.besitz, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.gewinn = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gewinn.setObjectName("gewinn")
        self.gridLayout.addWidget(self.gewinn, 4, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 1, 0, 1, 1)
        self.prozent = QtWidgets.QLabel(self.gridLayoutWidget)
        self.prozent.setObjectName("prozent")
        self.gridLayout.addWidget(self.prozent, 4, 6, 1, 1)
        self.ausgaben = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ausgaben.setObjectName("ausgaben")
        self.gridLayout.addWidget(self.ausgaben, 4, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 4, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 2, 6, 1, 1)
        self.line_22 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.gridLayout.addWidget(self.line_22, 4, 5, 1, 1)
        self.invest_uebersicht = QtWidgets.QTableWidget(self.tab)
        self.invest_uebersicht.setGeometry(QtCore.QRect(40, 130, 471, 241))
        self.invest_uebersicht.setStyleSheet("QTableView {\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: #807F81;\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: #807F81;\n"
"background-color: #807F81;\n"
"border-bottom: 1px solid black;\n"
"}\n"
"QTableView::item{\n"
"\n"
"\n"
"border-bottom : 1px solid black;\n"
"gridline-color: #807F81;\n"
"}")
        self.invest_uebersicht.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.invest_uebersicht.setObjectName("invest_uebersicht")
        self.invest_uebersicht.setColumnCount(4)
        self.invest_uebersicht.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.invest_uebersicht.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.invest_uebersicht.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.invest_uebersicht.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.invest_uebersicht.setHorizontalHeaderItem(3, item)
        self.invest_uebersicht.horizontalHeader().setCascadingSectionResizes(True)
        self.invest_uebersicht.horizontalHeader().setDefaultSectionSize(113)
        self.invest_uebersicht.verticalHeader().setVisible(False)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(550, 20, 471, 100))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_10 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_3.addWidget(self.line_10, 3, 4, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_3.addWidget(self.line_7, 1, 0, 1, 1)
        self.prozent_kredit = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.prozent_kredit.setObjectName("prozent_kredit")
        self.gridLayout_3.addWidget(self.prozent_kredit, 4, 6, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_3.addWidget(self.line_11, 4, 1, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 3, 2, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_3.addWidget(self.line_8, 3, 0, 1, 1)
        self.summe_kredit = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.summe_kredit.setObjectName("summe_kredit")
        self.gridLayout_3.addWidget(self.summe_kredit, 4, 2, 1, 1)
        self.gewinn_kredit = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.gewinn_kredit.setObjectName("gewinn_kredit")
        self.gridLayout_3.addWidget(self.gewinn_kredit, 4, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 2, 1, 1)
        self.ausgaben_kredit = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.ausgaben_kredit.setObjectName("ausgaben_kredit")
        self.gridLayout_3.addWidget(self.ausgaben_kredit, 4, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 2, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 4, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_3.addWidget(self.line_12, 4, 3, 1, 1)
        self.line_23 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.gridLayout_3.addWidget(self.line_23, 4, 5, 1, 1)
        self.line_25 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.gridLayout_3.addWidget(self.line_25, 3, 6, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1060, 20, 471, 100))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tages_prozent = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.tages_prozent.setObjectName("tages_prozent")
        self.gridLayout_6.addWidget(self.tages_prozent, 4, 6, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_6.addWidget(self.line_13, 3, 0, 1, 1)
        self.tages_ausgaben = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.tages_ausgaben.setObjectName("tages_ausgaben")
        self.gridLayout_6.addWidget(self.tages_ausgaben, 4, 0, 1, 1)
        self.tages_hoehe = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.tages_hoehe.setObjectName("tages_hoehe")
        self.gridLayout_6.addWidget(self.tages_hoehe, 4, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 2, 2, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_6.addWidget(self.line_16, 4, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 2, 4, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_36.setObjectName("label_36")
        self.gridLayout_6.addWidget(self.label_36, 2, 6, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_6.addWidget(self.line_17, 4, 3, 1, 1)
        self.tages_gewinn = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.tages_gewinn.setObjectName("tages_gewinn")
        self.gridLayout_6.addWidget(self.tages_gewinn, 4, 4, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 0, 0, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout_6.addWidget(self.line_14, 3, 4, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_6.addWidget(self.line_15, 3, 2, 1, 1)
        self.line_18 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gridLayout_6.addWidget(self.line_18, 1, 0, 1, 1)
        self.line_24 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.line_24.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.gridLayout_6.addWidget(self.line_24, 4, 5, 1, 1)
        self.line_26 = QtWidgets.QFrame(self.gridLayoutWidget_6)
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.gridLayout_6.addWidget(self.line_26, 3, 6, 1, 1)
        self.line_19 = QtWidgets.QFrame(self.tab)
        self.line_19.setGeometry(QtCore.QRect(520, 20, 20, 101))
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.tab)
        self.line_20.setGeometry(QtCore.QRect(1030, 20, 20, 101))
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.kredit_uebersicht = QtWidgets.QTableWidget(self.tab)
        self.kredit_uebersicht.setGeometry(QtCore.QRect(550, 130, 471, 241))
        self.kredit_uebersicht.setStyleSheet("QTableView {\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: #807F81;\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: #807F81;\n"
"background-color: #807F81;\n"
"border-bottom: 1px solid black;\n"
"}\n"
"QTableView::item{\n"
"\n"
"\n"
"border-bottom : 1px solid black;\n"
"gridline-color: #807F81;\n"
"}")
        self.kredit_uebersicht.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.kredit_uebersicht.setObjectName("kredit_uebersicht")
        self.kredit_uebersicht.setColumnCount(5)
        self.kredit_uebersicht.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.kredit_uebersicht.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.kredit_uebersicht.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.kredit_uebersicht.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.kredit_uebersicht.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.kredit_uebersicht.setHorizontalHeaderItem(4, item)
        self.kredit_uebersicht.horizontalHeader().setDefaultSectionSize(90)
        self.kredit_uebersicht.verticalHeader().setVisible(False)
        self.tages_uebersicht = QtWidgets.QTableWidget(self.tab)
        self.tages_uebersicht.setGeometry(QtCore.QRect(1060, 130, 471, 241))
        self.tages_uebersicht.setStyleSheet("QTableView {\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: #807F81;\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: #807F81;\n"
"background-color: #807F81;\n"
"border-bottom: 1px solid black;\n"
"}\n"
"QTableView::item{\n"
"\n"
"\n"
"border-bottom : 1px solid black;\n"
"gridline-color: #807F81;\n"
"}")
        self.tages_uebersicht.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tages_uebersicht.setObjectName("tages_uebersicht")
        self.tages_uebersicht.setColumnCount(5)
        self.tages_uebersicht.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tages_uebersicht.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tages_uebersicht.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tages_uebersicht.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tages_uebersicht.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tages_uebersicht.setHorizontalHeaderItem(4, item)
        self.tages_uebersicht.horizontalHeader().setDefaultSectionSize(90)
        self.tages_uebersicht.verticalHeader().setVisible(False)
        self.aktualisieren = QtWidgets.QPushButton(self.tab)
        self.aktualisieren.setGeometry(QtCore.QRect(710, 590, 172, 32))
        self.aktualisieren.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.aktualisieren.setObjectName("aktualisieren")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(359, 450, 871, 121))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gesamt_ausgaben = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.gesamt_ausgaben.setStyleSheet("color:#ffffff; font-size:64pt; border: 2px solid black; border-radius: 5px; align= center")
        self.gesamt_ausgaben.setObjectName("gesamt_ausgaben")
        self.gridLayout_7.addWidget(self.gesamt_ausgaben, 1, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_33.setObjectName("label_33")
        self.gridLayout_7.addWidget(self.label_33, 0, 1, 1, 1)
        self.gesamt_prozent = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.gesamt_prozent.setStyleSheet("color:#ffffff; font-size:64pt; border: 2px solid black; border-radius: 5px; align= center")
        self.gesamt_prozent.setObjectName("gesamt_prozent")
        self.gridLayout_7.addWidget(self.gesamt_prozent, 1, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_31.setObjectName("label_31")
        self.gridLayout_7.addWidget(self.label_31, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_30.setObjectName("label_30")
        self.gridLayout_7.addWidget(self.label_30, 0, 2, 1, 1)
        self.gesamt_gewinn = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.gesamt_gewinn.setStyleSheet("color:#ffffff; font-size:64pt; border: 2px solid black; border-radius: 5px; align= center")
        self.gesamt_gewinn.setObjectName("gesamt_gewinn")
        self.gridLayout_7.addWidget(self.gesamt_gewinn, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(360, 20, 381, 248))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.aktie_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.aktie_layout.setContentsMargins(0, 0, 0, 0)
        self.aktie_layout.setObjectName("aktie_layout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.aktie_layout.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.aktie_layout.addWidget(self.label_7, 5, 1, 1, 1)
        self.error_eintrag = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.error_eintrag.setText("")
        self.error_eintrag.setObjectName("error_eintrag")
        self.aktie_layout.addWidget(self.error_eintrag, 7, 0, 1, 2)
        self.text_name = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.text_name.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.text_name.setObjectName("text_name")
        self.aktie_layout.addWidget(self.text_name, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.aktie_layout.addWidget(self.label_4, 1, 1, 1, 1)
        self.eintrag_speichern = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.eintrag_speichern.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.eintrag_speichern.setObjectName("eintrag_speichern")
        self.aktie_layout.addWidget(self.eintrag_speichern, 8, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.aktie_layout.addWidget(self.label_6, 4, 1, 1, 1)
        self.url_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.url_label.setObjectName("url_label")
        self.aktie_layout.addWidget(self.url_label, 3, 1, 1, 1)
        self.text_ausgabe = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.text_ausgabe.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.text_ausgabe.setObjectName("text_ausgabe")
        self.aktie_layout.addWidget(self.text_ausgabe, 4, 0, 1, 1)
        self.combo_art = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.combo_art.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid teal;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: pink;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"     padding-left: 10px;\n"
" }\n"
"\n"
"\n"
"")
        self.combo_art.setObjectName("combo_art")
        self.combo_art.addItem("")
        self.combo_art.addItem("")
        self.aktie_layout.addWidget(self.combo_art, 0, 0, 1, 1)
        self.text_anzahl = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.text_anzahl.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.text_anzahl.setObjectName("text_anzahl")
        self.aktie_layout.addWidget(self.text_anzahl, 5, 0, 1, 1)
        self.text_url = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.text_url.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.text_url.setObjectName("text_url")
        self.aktie_layout.addWidget(self.text_url, 3, 0, 1, 1)
        self.url_combobox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.url_combobox.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid teal;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: pink;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"     padding-left: 10px;\n"
" }\n"
"\n"
"\n"
"")
        self.url_combobox.setObjectName("url_combobox")
        self.aktie_layout.addWidget(self.url_combobox, 2, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName("label_35")
        self.aktie_layout.addWidget(self.label_35, 2, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(780, 10, 379, 341))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.kredit_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.kredit_layout.setContentsMargins(0, 0, 0, 0)
        self.kredit_layout.setObjectName("kredit_layout")
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_19.setObjectName("label_19")
        self.kredit_layout.addWidget(self.label_19, 7, 1, 1, 1)
        self.kredit_kosten = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.kredit_kosten.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.kredit_kosten.setObjectName("kredit_kosten")
        self.kredit_layout.addWidget(self.kredit_kosten, 8, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.kredit_layout.addWidget(self.label_17, 4, 1, 1, 1)
        self.kredit_name = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.kredit_name.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.kredit_name.setObjectName("kredit_name")
        self.kredit_layout.addWidget(self.kredit_name, 1, 0, 1, 1)
        self.combo_art_2 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.combo_art_2.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid teal;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: pink;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"     padding-left: 10px;\n"
" }\n"
"\n"
"\n"
"")
        self.combo_art_2.setObjectName("combo_art_2")
        self.combo_art_2.addItem("")
        self.combo_art_2.addItem("")
        self.combo_art_2.addItem("")
        self.kredit_layout.addWidget(self.combo_art_2, 0, 0, 1, 1)
        self.kredit_hoehe = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.kredit_hoehe.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.kredit_hoehe.setObjectName("kredit_hoehe")
        self.kredit_layout.addWidget(self.kredit_hoehe, 2, 0, 1, 1)
        self.kredit_invest = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.kredit_invest.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.kredit_invest.setObjectName("kredit_invest")
        self.kredit_layout.addWidget(self.kredit_invest, 3, 0, 1, 1)
        self.label_zinssatz_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_zinssatz_2.setObjectName("label_zinssatz_2")
        self.kredit_layout.addWidget(self.label_zinssatz_2, 5, 1, 1, 1)
        self.kredit_datum = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.kredit_datum.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.kredit_datum.setObjectName("kredit_datum")
        self.kredit_layout.addWidget(self.kredit_datum, 7, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.kredit_layout.addWidget(self.label_18, 0, 1, 1, 1)
        self.kredit_speichern = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.kredit_speichern.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.kredit_speichern.setObjectName("kredit_speichern")
        self.kredit_layout.addWidget(self.kredit_speichern, 11, 0, 1, 2)
        self.label_laufzeit_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_laufzeit_2.setObjectName("label_laufzeit_2")
        self.kredit_layout.addWidget(self.label_laufzeit_2, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_15.setObjectName("label_15")
        self.kredit_layout.addWidget(self.label_15, 3, 1, 1, 1)
        self.kredit_rate = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.kredit_rate.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.kredit_rate.setObjectName("kredit_rate")
        self.kredit_layout.addWidget(self.kredit_rate, 6, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.kredit_layout.addWidget(self.label_20, 8, 1, 1, 1)
        self.kredit_laufzeit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.kredit_laufzeit.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.kredit_laufzeit.setObjectName("kredit_laufzeit")
        self.kredit_layout.addWidget(self.kredit_laufzeit, 5, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.kredit_layout.addWidget(self.label_14, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_16.setObjectName("label_16")
        self.kredit_layout.addWidget(self.label_16, 1, 1, 1, 1)
        self.kredit_zins = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.kredit_zins.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.kredit_zins.setObjectName("kredit_zins")
        self.kredit_layout.addWidget(self.kredit_zins, 4, 0, 1, 1)
        self.error_kredit = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.error_kredit.setText("")
        self.error_kredit.setObjectName("error_kredit")
        self.kredit_layout.addWidget(self.error_kredit, 10, 0, 1, 2)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(360, 290, 381, 206))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.tagesgeld_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.tagesgeld_layout.setContentsMargins(0, 0, 0, 0)
        self.tagesgeld_layout.setObjectName("tagesgeld_layout")
        self.tages_speichern = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.tages_speichern.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.tages_speichern.setObjectName("tages_speichern")
        self.tagesgeld_layout.addWidget(self.tages_speichern, 6, 0, 1, 2)
        self.tages_wert = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.tages_wert.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.tages_wert.setObjectName("tages_wert")
        self.tagesgeld_layout.addWidget(self.tages_wert, 2, 0, 1, 1)
        self.tages_datum = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.tages_datum.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.tages_datum.setObjectName("tages_datum")
        self.tagesgeld_layout.addWidget(self.tages_datum, 4, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_22.setObjectName("label_22")
        self.tagesgeld_layout.addWidget(self.label_22, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_24.setObjectName("label_24")
        self.tagesgeld_layout.addWidget(self.label_24, 3, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_25.setObjectName("label_25")
        self.tagesgeld_layout.addWidget(self.label_25, 4, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_21.setObjectName("label_21")
        self.tagesgeld_layout.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_23.setObjectName("label_23")
        self.tagesgeld_layout.addWidget(self.label_23, 2, 1, 1, 1)
        self.tages_name = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.tages_name.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.tages_name.setObjectName("tages_name")
        self.tagesgeld_layout.addWidget(self.tages_name, 1, 0, 1, 1)
        self.tages_zins = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.tages_zins.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.tages_zins.setObjectName("tages_zins")
        self.tagesgeld_layout.addWidget(self.tages_zins, 3, 0, 1, 1)
        self.tages_error = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.tages_error.setText("")
        self.tages_error.setObjectName("tages_error")
        self.tagesgeld_layout.addWidget(self.tages_error, 5, 0, 1, 1)
        self.auswahl_neuer_eintrag_combo = QtWidgets.QComboBox(self.tab_2)
        self.auswahl_neuer_eintrag_combo.setGeometry(QtCore.QRect(10, 20, 301, 31))
        self.auswahl_neuer_eintrag_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid teal;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: pink;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"     padding-left: 10px;\n"
" }\n"
"\n"
"\n"
"")
        self.auswahl_neuer_eintrag_combo.setObjectName("auswahl_neuer_eintrag_combo")
        self.auswahl_neuer_eintrag_combo.addItem("")
        self.auswahl_neuer_eintrag_combo.addItem("")
        self.auswahl_neuer_eintrag_combo.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1560, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.invest_uebersicht)
        MainWindow.setTabOrder(self.invest_uebersicht, self.tages_name)
        MainWindow.setTabOrder(self.tages_name, self.tages_wert)
        MainWindow.setTabOrder(self.tages_wert, self.tages_zins)
        MainWindow.setTabOrder(self.tages_zins, self.tages_datum)
        MainWindow.setTabOrder(self.tages_datum, self.tages_speichern)
        MainWindow.setTabOrder(self.tages_speichern, self.combo_art)
        MainWindow.setTabOrder(self.combo_art, self.text_name)
        MainWindow.setTabOrder(self.text_name, self.text_url)
        MainWindow.setTabOrder(self.text_url, self.text_ausgabe)
        MainWindow.setTabOrder(self.text_ausgabe, self.text_anzahl)
        MainWindow.setTabOrder(self.text_anzahl, self.eintrag_speichern)
        MainWindow.setTabOrder(self.eintrag_speichern, self.combo_art_2)
        MainWindow.setTabOrder(self.combo_art_2, self.kredit_name)
        MainWindow.setTabOrder(self.kredit_name, self.kredit_hoehe)
        MainWindow.setTabOrder(self.kredit_hoehe, self.kredit_invest)
        MainWindow.setTabOrder(self.kredit_invest, self.kredit_zins)
        MainWindow.setTabOrder(self.kredit_zins, self.kredit_laufzeit)
        MainWindow.setTabOrder(self.kredit_laufzeit, self.kredit_rate)
        MainWindow.setTabOrder(self.kredit_rate, self.kredit_datum)
        MainWindow.setTabOrder(self.kredit_datum, self.kredit_kosten)
        MainWindow.setTabOrder(self.kredit_kosten, self.kredit_speichern)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Derzeitiger Wert</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Ausgaben</span></p></body></html>"))
        self.besitz.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gewinn</span></p></body></html>"))
        self.gewinn.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Währungen</span></p></body></html>"))
        self.prozent.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.ausgaben.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Prozent</span></p></body></html>"))
        item = self.invest_uebersicht.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Wertpapier"))
        item = self.invest_uebersicht.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Anzahl im Depot"))
        item = self.invest_uebersicht.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kaufpreis"))
        item = self.invest_uebersicht.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Aktueller Wert"))
        self.prozent_kredit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.summe_kredit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.gewinn_kredit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gesamt Summe</span></p></body></html>"))
        self.ausgaben_kredit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Prozent</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Kredite</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Ausgaben</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gewinn</span></p></body></html>"))
        self.tages_prozent.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.tages_ausgaben.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.tages_hoehe.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Derzeitiger Wert</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gewinn</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Prozent</span></p></body></html>"))
        self.tages_gewinn.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Ausgaben</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Tageszins</span></p></body></html>"))
        item = self.kredit_uebersicht.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.kredit_uebersicht.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Investiert"))
        item = self.kredit_uebersicht.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Laufzeit"))
        item = self.kredit_uebersicht.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Zinssatz"))
        item = self.kredit_uebersicht.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gewinn"))
        item = self.tages_uebersicht.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tages_uebersicht.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Investiert"))
        item = self.tages_uebersicht.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Zinssatz"))
        item = self.tages_uebersicht.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gewinn"))
        item = self.tages_uebersicht.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Dauer"))
        self.aktualisieren.setText(_translate("MainWindow", "Aktualisieren"))
        self.gesamt_ausgaben.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:64pt; color:#00ff00;\">+</span><span style=\" font-size:64pt; color:#ffffff;\">0</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">Rendite Durschnitt</span></p></body></html>"))
        self.gesamt_prozent.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:64pt; color:#ffffff;\">0%</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Gesamt Ausgaben</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Gesamt Gewinn</span></p></body></html>"))
        self.gesamt_gewinn.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:64pt; color:#00ff00;\">+</span><span style=\" font-size:64pt; color:#ffffff;\">0</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Übersicht"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Art</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Anzahl</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.eintrag_speichern.setText(_translate("MainWindow", "Speichern"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Ausgabe</span></p></body></html>"))
        self.url_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">URL</span></p></body></html>"))
        self.combo_art.setItemText(0, _translate("MainWindow", "Aktie"))
        self.combo_art.setItemText(1, _translate("MainWindow", "Währung/Kryptowährung"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">URL</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Datum beginn Rückzahlung</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Zinssatz</span></p></body></html>"))
        self.combo_art_2.setItemText(0, _translate("MainWindow", "Privat Kredit"))
        self.combo_art_2.setItemText(1, _translate("MainWindow", "Kredit"))
        self.combo_art_2.setItemText(2, _translate("MainWindow", "Immobilien"))
        self.label_zinssatz_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Laufzeit</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Art</span></p></body></html>"))
        self.kredit_speichern.setText(_translate("MainWindow", "Speichern"))
        self.label_laufzeit_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Monatliche Rate</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Invest Summe</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Kosten für Abschluss</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Kredit Höhe</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.tages_speichern.setText(_translate("MainWindow", "Speichern"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Zinssatz</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Datum</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Tagesgeld</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Wert</span></p></body></html>"))
        self.auswahl_neuer_eintrag_combo.setItemText(0, _translate("MainWindow", "Tagesgeld"))
        self.auswahl_neuer_eintrag_combo.setItemText(1, _translate("MainWindow", "Aktien / Währungen"))
        self.auswahl_neuer_eintrag_combo.setItemText(2, _translate("MainWindow", "Kredite "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Neuer Eintrag"))
