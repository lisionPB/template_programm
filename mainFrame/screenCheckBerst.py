from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QLineEdit, QDoubleSpinBox, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from mainFrame.screen import Screen

class ScreenCheckBerst(Screen):

    _sig_start = pyqtSignal()
    _sig_quit = pyqtSignal()
    
    
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        self.mainLayout.addStretch(1)

        self.groupCenter = QGroupBox()
        self.mainLayout.addWidget(self.groupCenter)
        self.centerLayout = QVBoxLayout()
        self.groupCenter.setLayout(self.centerLayout)
        self.groupCenter.setFixedWidth(450)

        self.centerLayout.addStretch(1)
        
        self.lTitle = QLabel("Checkliste: Berstfestigkeits Prüfung")
        self.centerLayout.addWidget(self.lTitle)
        
        self.centerLayout.addStretch(1)

        self.cb1 = QCheckBox("Staubvorratsbehälter gefüllt?")
        self.centerLayout.addWidget(self.cb1)

        self.cb2 = QCheckBox("Körnungsanalyse durchgeführt?")
        self.centerLayout.addWidget(self.cb2)

        self.cb3 = QCheckBox("Abluftventilator auf Automatik?")
        self.centerLayout.addWidget(self.cb3)
        
        self.cb4 = QCheckBox("befindet sich der Umluft- / Abluftschalter in der richtigen Position?")
        self.centerLayout.addWidget(self.cb4)
        
        self.cb5 = QCheckBox("Prüfkammer geschlossen?")
        self.centerLayout.addWidget(self.cb5)
        
        self.cb6 = QCheckBox("Pumpen eingeschaltet?")
        self.centerLayout.addWidget(self.cb6)
        
        self.cb7 = QCheckBox("Richtige Absaugssonde eingebaut?")
        self.centerLayout.addWidget(self.cb7)
        
        self.cb8 = QCheckBox("Gravimetrie: Messfilter eingebaut?")
        self.centerLayout.addWidget(self.cb8)
        
        self.cb9 = QCheckBox("Staubzuführung gewährleistet?")
        self.centerLayout.addWidget(self.cb9)
        
        self.groupSchlauch = QGroupBox()
        self.centerLayout.addWidget(self.groupSchlauch)
        self.groupSchlauch.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        self.layoutSchlauch = QHBoxLayout()
        self.layoutSchlauch.setContentsMargins(0,0,0,0)
        self.groupSchlauch.setLayout(self.layoutSchlauch)
        self.cbSchlauch = QCheckBox("Schlauchdurchmesser")
        self.layoutSchlauch.addWidget(self.cbSchlauch)
        self.sbSchlauch = QDoubleSpinBox()
        self.layoutSchlauch.addWidget(self.sbSchlauch)
        self.sbSchlauch.setValue(10.0)
        self.sbSchlauch.setDecimals(2)

        
        self.groupRaum = QGroupBox()
        self.centerLayout.addWidget(self.groupRaum)
        self.groupRaum.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        self.layoutRaum = QHBoxLayout()
        self.layoutRaum.setContentsMargins(0,0,0,0)
        self.groupRaum.setLayout(self.layoutRaum)
        self.cbTemperatur = QCheckBox("Temperatur [°C]")
        self.layoutRaum.addWidget(self.cbTemperatur)
        self.sbTemperatur = QDoubleSpinBox()
        self.layoutRaum.addWidget(self.sbTemperatur)
        self.sbTemperatur.setValue(10.0)
        self.sbTemperatur.setDecimals(2)
        self.lFeuchte = QLabel("Feuchtigkeit [%]")
        self.layoutRaum.addWidget(self.lFeuchte)
        self.sbFeuchte = QDoubleSpinBox()
        self.layoutRaum.addWidget(self.sbFeuchte)
        self.sbFeuchte.setValue(50.0)
        self.sbFeuchte.setDecimals(2)

        self.groupKundeBericht = QGroupBox()
        self.centerLayout.addWidget(self.groupKundeBericht)
        self.groupKundeBericht.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        self.layoutKundeBericht = QHBoxLayout()
        self.layoutKundeBericht.setContentsMargins(0,0,0,0)
        self.groupKundeBericht.setLayout(self.layoutKundeBericht)
        self.cbKunde = QCheckBox("Kunde")
        self.layoutKundeBericht.addWidget(self.cbKunde)
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
        self.cbHerstellerVol = QCheckBox("Herstellerang. Volumenstrom")
        self.layoutHerstellerVol.addWidget(self.cbHerstellerVol)
        self.sbHerstellerVol = QDoubleSpinBox()
        self.layoutHerstellerVol.addWidget(self.sbHerstellerVol)
        self.sbHerstellerVol.setDecimals(2)
        
        self.groupGewicht = QGroupBox()
        self.centerLayout.addWidget(self.groupGewicht)
        self.groupGewicht.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        self.layoutGewicht = QHBoxLayout()
        self.layoutGewicht.setContentsMargins(0,0,0,0)
        self.groupGewicht.setLayout(self.layoutGewicht)
        self.cbGewichtGes = QCheckBox("akt. Gesamtgewicht Staub / Soll [kg]")
        self.layoutGewicht.addWidget(self.cbGewichtGes)
        self.leGesGewicht = QLineEdit()
        self.layoutGewicht.addWidget(self.leGesGewicht)
        self.lGewichtSoll = QLabel("/")
        self.layoutGewicht.addWidget(self.lGewichtSoll)
        self.leGewichtSoll = QLineEdit()
        self.layoutGewicht.addWidget(self.leGewichtSoll)
        
        
        self.cb9 = QCheckBox("Messung starten?")
        self.centerLayout.addWidget(self.cb9)
        
        self.groupStartZuruck = QGroupBox()
        self.centerLayout.addWidget(self.groupStartZuruck)
        self.layoutStartZuruck = QHBoxLayout()
        self.groupStartZuruck.setLayout(self.layoutStartZuruck)
        self.pbZuruck = QPushButton("<< Zurück")
        self.pbZuruck.clicked.connect(self._sig_quit.emit)
        self.layoutStartZuruck.addWidget(self.pbZuruck)
        self.pbStart = QPushButton("Weiter >>")
        self.layoutStartZuruck.addWidget(self.pbStart)
        self.pbStart.clicked.connect(self._sig_start.emit)

        self.centerLayout.addStretch(2)
        
        self.mainLayout.addStretch(1)