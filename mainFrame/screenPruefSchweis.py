from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from mainFrame.screen import Screen

from mainFrame.elements.alertWidget import AlertWidget
from mainFrame.elements.valueWidget import ValueWidget
from mainFrame.elements.setValueWidget import SetValueWidget
from mainFrame.elements.consoleWidget import ConsoleWidget


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
        
        self.layoutLeft.addStretch(1)
        self.groupLeft.setFixedWidth(1200)
        
        # Diagramm
        
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
        
        
        

        ###############
        # BOTTOM
        
        self.groupBottom = QGroupBox()
        self.mainLayout.addWidget(self.groupBottom)
        self.layoutBottom = QHBoxLayout()
        self.groupBottom.setLayout(self.layoutBottom)
        
        self.layoutBottom.addStretch(1)
        self.groupBottom.setFixedHeight(500)
        
