from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject

import pyqtgraph as pg

from mainFrame.screen import Screen

from mainFrame.elements.alertWidget import AlertWidget
from mainFrame.elements.valueWidget import ValueWidget
from mainFrame.elements.setValueWidget import SetValueWidget
from mainFrame.elements.consoleWidget import ConsoleWidget

from datenerfassung.messdatenGraphWidget import MessdatenGraphWidget

class ScreenPruefSchweis(Screen):

    _sig_start = pyqtSignal()
    _sig_quit = pyqtSignal()
    
    
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        
        ################
        # TOP

        self.groupTop = QGroupBox()
        self.mainLayout.addWidget(self.groupTop)
        self.layoutTop = QHBoxLayout()
        self.groupTop.setLayout(self.layoutTop)
        
        #-----
        # Links
        self.groupLeft = QGroupBox()
        self.layoutTop.addWidget(self.groupLeft)
        self.layoutLeft = QVBoxLayout()
        self.groupLeft.setLayout(self.layoutLeft)
        
        # self.layoutLeft.addStretch(1)
        self.groupLeft.setFixedWidth(1200)
        
        # Diagramm
        
        self.graphWidget = MessdatenGraphWidget(self)
        # self.graphWidget = pg.PlotWidget()
        self.layoutLeft.addWidget(self.graphWidget)
        # self.graphWidget.set_floatingWindowEnabled(False)
        
        
        #-----
        # Rechts
        self.groupRight = QGroupBox()
        self.layoutTop.addWidget(self.groupRight)
        self.layoutRight = QVBoxLayout()
        self.groupRight.setLayout(self.layoutRight)
        
        # Alarme
        self.groupAlerts = QGroupBox()
        self.layoutRight.addWidget(self.groupAlerts)
        self.layoutAlerts = QVBoxLayout()
        self.groupAlerts.setLayout(self.layoutAlerts)
        
        self.alertV3 = AlertWidget("Alarm: V3 zu niedrig")
        self.layoutAlerts.addWidget(self.alertV3)
        self.alertP3 = AlertWidget("Alarm: P3 zu hoch")
        self.layoutAlerts.addWidget(self.alertP3)
        
        # Rauminfos
        self.groupRaum = QGroupBox()
        self.layoutRight.addWidget(self.groupRaum)
        self.layoutRaum = QVBoxLayout()
        self.groupRaum.setLayout(self.layoutRaum)
        
        self.valueRaumTemp = ValueWidget("Raumtemperatur: ", "°C")
        self.layoutRaum.addWidget(self.valueRaumTemp)
        
        self.valueRaumFeuchte = ValueWidget("Feuchtigkeit: ", "\%rh")
        self.layoutRaum.addWidget(self.valueRaumFeuchte)
        
        # HW-Settings
        self.groupHW = QGroupBox()
        self.layoutRight.addWidget(self.groupHW)
        self.layoutHW = QVBoxLayout()
        self.groupHW.setLayout(self.layoutHW)
        
        self.setValueSchlauchDM = SetValueWidget("Schlauchdurchmesser: ", "mm")
        self.layoutHW.addWidget(self.setValueSchlauchDM)
        
        # Messeinstellungen
        self.groupMess = QGroupBox()
        self.layoutRight.addWidget(self.groupMess)
        self.layoutMess = QVBoxLayout()
        self.groupMess.setLayout(self.layoutMess)
        
        self.setValueSollV2 = SetValueWidget("Sollwert V2: ", "m/s")
        self.layoutMess.addWidget(self.setValueSollV2)
        
        self.setValueMessdauer = SetValueWidget("Messdauer: ", " (hh:mm)")
        self.layoutMess.addWidget(self.setValueMessdauer)
        
        self.setValueWartezeit = SetValueWidget("Wartezeit: ", "min")
        self.layoutMess.addWidget(self.setValueWartezeit)
        
        
        # Prüfungsteuerung
        
        self.pbStart = QPushButton("Messung starten")
        self.layoutMess.addWidget(self.pbStart)
        
        self.pbStop = QPushButton("STOP")
        self.layoutMess.addWidget(self.pbStop)
        
        # Console
        
        self.console = ConsoleWidget([])
        self.layoutRight.addWidget(self.console)
        
        # Zurück
        
        self.pbZuruck = QPushButton("Zurück zum Menü")
        self.layoutRight.addWidget(self.pbZuruck)
        self.pbZuruck.clicked.connect(self._sig_quit.emit)
        
        
        

        ###############
        # BOTTOM
        
        self.groupBottom = QGroupBox()
        self.mainLayout.addWidget(self.groupBottom)
        self.layoutBottom = QVBoxLayout()
        self.groupBottom.setLayout(self.layoutBottom)
        
        # self.layoutBottom.addStretch(1)
        # self.groupBottom.setFixedHeight(500)
        
        self.groupV = QGroupBox()
        self.layoutBottom.addWidget(self.groupV)
        self.layoutV = QHBoxLayout()
        self.groupV.setLayout(self.layoutV)
        
        self.valueV1 = ValueWidget("Ist V1", unit="m/s", widthLabel= 100, widthUnit=50)
        self.layoutV.addWidget(self.valueV1)
        self.valueV2 = ValueWidget("Ist V2", unit="m/s", widthLabel= 100, widthUnit=50)
        self.layoutV.addWidget(self.valueV2)
        self.valueV3 = ValueWidget("Ist V3", unit="m/s", widthLabel= 100, widthUnit=50)
        self.layoutV.addWidget(self.valueV3)
        self.valueV4 = ValueWidget("Ist V4", unit="m/s", widthLabel= 100, widthUnit=50)
        self.layoutV.addWidget(self.valueV4)
        
        self.groupP = QGroupBox()
        self.layoutBottom.addWidget(self.groupP)
        self.layoutP = QHBoxLayout()
        self.groupP.setLayout(self.layoutP)
        
        self.valueP1 = ValueWidget("Unterdruck P1", unit="kPa", widthLabel= 100, widthUnit=50)
        self.layoutP.addWidget(self.valueP1)
        self.valueP2 = ValueWidget("Unterdruck P2", unit="kPa", widthLabel= 100, widthUnit=50)
        self.layoutP.addWidget(self.valueP2)
        self.valueP3 = ValueWidget("Unterdruck P3", unit="kPa", widthLabel= 100, widthUnit=50)
        self.layoutP.addWidget(self.valueP3)
        self.valueP4 = ValueWidget("Unterdruck P4", unit="kPa", widthLabel= 100, widthUnit=50)
        self.layoutP.addWidget(self.valueP4)
        
        
        
        
        
    def closeMessdatenUI(self):
        self.graphWidget.set_openedExtern(False)
        self.layoutLeft.insertWidget(0, self.graphWidget)




    def on_setActive(self):
        # self.mainWindow.setWindowFlags(Qt.Hint)
        self.mainWindow.showMaximized()
        # self.mainWindow.showFullScreen()