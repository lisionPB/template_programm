from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QLineEdit, QDoubleSpinBox, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from style.lisionStyle import LisionStyle

import config.parameters as params

from mainFrame.screen import Screen

class ScreenCheckSchweis(Screen):

    _sig_start = pyqtSignal()
    _sig_quit = pyqtSignal()
    
    
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.checks = []
        
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        
        self.mainLayout.addStretch(1)

        self.groupCenter = QGroupBox()
        self.mainLayout.addWidget(self.groupCenter)
        self.centerLayout = QVBoxLayout()
        self.groupCenter.setLayout(self.centerLayout)
        self.groupCenter.setFixedWidth(450)

        self.centerLayout.addStretch(1)
        
        self.lTitle = QLabel("Checkliste:\nSchweißrauchtechnische Prüfung")
        self.centerLayout.addWidget(self.lTitle)
        self.lTitle.setFont(LisionStyle.LABEL_FONT_TITEL)
        
        self.centerLayout.addStretch(1)

        self.cb1 = QCheckBox("Schweißgerät eingeschalten?")
        self.centerLayout.addWidget(self.cb1)
        self.checks.append(self.cb1)
        self.cb1.stateChanged.connect(self.__checkReady)

        self.cb2 = QCheckBox("Gasflasche aufgedreht?")
        self.centerLayout.addWidget(self.cb2)
        self.checks.append(self.cb2)
        self.cb2.stateChanged.connect(self.__checkReady)

        self.cb3 = QCheckBox("Schweißrauchquelle eingeschalten?")
        self.centerLayout.addWidget(self.cb3)
        self.checks.append(self.cb3)
        self.cb3.stateChanged.connect(self.__checkReady)
        
        self.cb4 = QCheckBox("befindet sich der Umluft- / Abluftschalter in der richtigen Position?")
        self.centerLayout.addWidget(self.cb4)
        self.checks.append(self.cb4)
        self.cb4.stateChanged.connect(self.__checkReady)
        
        self.cb5 = QCheckBox("Prüfkammer geschlossen?")
        self.centerLayout.addWidget(self.cb5)
        self.checks.append(self.cb5)
        self.cb5.stateChanged.connect(self.__checkReady)
        
        self.cb6 = QCheckBox("Gasflasche aufgedreht?")
        self.centerLayout.addWidget(self.cb6)
        self.checks.append(self.cb6)
        self.cb6.stateChanged.connect(self.__checkReady)
        
        self.groupSchlauch = QGroupBox()
        self.centerLayout.addWidget(self.groupSchlauch)
        self.groupSchlauch.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        self.layoutSchlauch = QHBoxLayout()
        self.layoutSchlauch.setContentsMargins(0,0,0,0)
        self.groupSchlauch.setLayout(self.layoutSchlauch)
        self.cbSchlauch = QCheckBox("Schlauchdurchmesser [mm]")
        self.layoutSchlauch.addWidget(self.cbSchlauch)
        self.checks.append(self.cbSchlauch)
        self.cbSchlauch.stateChanged.connect(self.__checkReady)
        self.sbSchlauch = QDoubleSpinBox()
        self.sbSchlauch.valueChanged.connect(self.schlauchdurchmesserChanged)
        self.layoutSchlauch.addWidget(self.sbSchlauch)
        self.sbSchlauch.setValue(params.defaults[params.SCHLAUCHDURCHMESSER])
        self.sbSchlauch.setDecimals(2)

        self.cb7 = QCheckBox("Richtige Absaugssonde eingebaut?")
        self.centerLayout.addWidget(self.cb7)
        self.checks.append(self.cb7)
        self.cb7.stateChanged.connect(self.__checkReady)
        
        self.cb8 = QCheckBox("Gravimetrie: Messfilter eingebaut?")
        self.centerLayout.addWidget(self.cb8)
        self.checks.append(self.cb8)
        self.cb8.stateChanged.connect(self.__checkReady)
        
        self.groupRaum = QGroupBox()
        self.centerLayout.addWidget(self.groupRaum)
        self.groupRaum.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        self.layoutRaum = QHBoxLayout()
        self.layoutRaum.setContentsMargins(0,0,0,0)
        self.groupRaum.setLayout(self.layoutRaum)
        self.cbTemperatur = QCheckBox("Temperatur [°C]")
        self.layoutRaum.addWidget(self.cbTemperatur)
        self.checks.append(self.cbTemperatur)
        self.cbTemperatur.stateChanged.connect(self.__checkReady)
        self.leTemperatur = QLineEdit()
        self.layoutRaum.addWidget(self.leTemperatur)
        self.leTemperatur.setReadOnly(True)
        self.lFeuchte = QLabel("Feuchtigkeit [%]")
        self.layoutRaum.addWidget(self.lFeuchte)
        self.leFeuchte = QLineEdit()
        self.layoutRaum.addWidget(self.leFeuchte)
        self.leFeuchte.setReadOnly(True)

        self.groupKundeBericht = QGroupBox()
        self.centerLayout.addWidget(self.groupKundeBericht)
        self.groupKundeBericht.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        self.layoutKundeBericht = QHBoxLayout()
        self.layoutKundeBericht.setContentsMargins(0,0,0,0)
        self.groupKundeBericht.setLayout(self.layoutKundeBericht)
        self.cbKunde = QCheckBox("Kunde")
        self.layoutKundeBericht.addWidget(self.cbKunde)
        self.checks.append(self.cbKunde)
        self.cbKunde.stateChanged.connect(self.__checkReady)
        self.leKunde = QLineEdit()
        self.layoutKundeBericht.addWidget(self.leKunde)
        self.lBericht = QLabel("Berichtsnummer")
        self.layoutKundeBericht.addWidget(self.lBericht)
        self.leBericht = QLineEdit()
        self.layoutKundeBericht.addWidget(self.leBericht)
        
        self.groupHerstellerVol = QGroupBox()
        self.centerLayout.addWidget(self.groupHerstellerVol)
        self.groupHerstellerVol.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        self.layoutHerstellerVol = QHBoxLayout()
        self.layoutHerstellerVol.setContentsMargins(0,0,0,0)
        self.groupHerstellerVol.setLayout(self.layoutHerstellerVol)
        self.cbHerstellerVol = QCheckBox("Herstellerang. Volumenstrom [m/s]")
        self.layoutHerstellerVol.addWidget(self.cbHerstellerVol)
        self.checks.append(self.cbHerstellerVol)
        self.cbHerstellerVol.stateChanged.connect(self.__checkReady)
        self.sbHerstellerVol = QDoubleSpinBox()
        self.layoutHerstellerVol.addWidget(self.sbHerstellerVol)
        self.sbHerstellerVol.setDecimals(2)
        
        
        self.cb9 = QCheckBox("Messung starten?")
        self.centerLayout.addWidget(self.cb9)
        self.checks.append(self.cb9)
        self.cb9.stateChanged.connect(self.__checkReady)
        
        self.groupStartZuruck = QGroupBox()
        self.centerLayout.addWidget(self.groupStartZuruck)
        self.layoutStartZuruck = QHBoxLayout()
        self.groupStartZuruck.setLayout(self.layoutStartZuruck)
        self.pbZuruck = QPushButton("<< Zurück")
        self.pbZuruck.clicked.connect(self._sig_quit.emit)
        self.layoutStartZuruck.addWidget(self.pbZuruck)
        self.pbStart = QPushButton("Weiter >>")
        self.layoutStartZuruck.addWidget(self.pbStart)
        self.pbStart.setEnabled(False)
        self.pbStart.clicked.connect(self._sig_start.emit)

        self.centerLayout.addStretch(2)
        
        self.mainLayout.addStretch(1)
        
    
    
    def __checkReady(self):
        ready = True
        for cb in self.checks:
            if(not cb.isChecked()):
                ready = False
                break
        
        self.pbStart.setEnabled(ready)
        
        
    def on_setActive(self):
        #TODO: Set all not checked
        for cb in self.checks:
            cb.setChecked(True)
        

    def schlauchdurchmesserChanged(self):
        self.mainWindow.hwSetup.einstellungen[params.SCHLAUCHDURCHMESSER] = self.sbSchlauch.value()