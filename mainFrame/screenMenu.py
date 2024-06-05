from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.Qt import QPixmap


from mainFrame.screen import Screen

class ScreenMenu(Screen):

    _sig_StartSchweis = pyqtSignal()
    _sig_StartStaub = pyqtSignal()
    _sig_StartBerst = pyqtSignal()
    _sig_Justage = pyqtSignal()
    _sig_Einrichtung = pyqtSignal()
    
    
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.mainLayout.addStretch(1)

        self.groupCenter = QGroupBox()
        self.mainLayout.addWidget(self.groupCenter)
        self.centerLayout = QVBoxLayout()
        self.groupCenter.setLayout(self.centerLayout)
        self.groupCenter.setFixedWidth(450)

        self.centerLayout.addStretch(1)


        # Messprogramme

        self.pbSchweis = QPushButton("Schweißrauchtechnische Prüfung")
        self.centerLayout.addWidget(self.pbSchweis)
        self.pbSchweis.clicked.connect(self._sig_StartSchweis.emit)

        self.pbStaub = QPushButton("Staubtechnische Prüfung")
        self.centerLayout.addWidget(self.pbStaub)
        self.pbStaub.clicked.connect(self._sig_StartStaub.emit)

        self.pbBerst = QPushButton("Berstfestigkeits Prüfung")
        self.centerLayout.addWidget(self.pbBerst)
        self.pbBerst.clicked.connect(self._sig_StartBerst.emit)
        
        self.centerLayout.addStretch(1)
        
        self.pbJustage = QPushButton("Justagedaten Sensoren")
        self.centerLayout.addWidget(self.pbJustage)
        self.pbJustage.clicked.connect(self._sig_Justage.emit)
        
        self.pbEinricht = QPushButton("Einrichtbetrieb")
        self.centerLayout.addWidget(self.pbEinricht)
        self.pbEinricht.clicked.connect(self._sig_Einrichtung.emit)
        
        
        self.centerLayout.addStretch(2)
        
        # Logo
        
        self.lLogo = QLabel()
        self.centerLayout.addWidget(self.lLogo)
        logo = QPixmap('symbols/lision.png')
        self.lLogo.setPixmap(logo.scaled(100, 200, Qt.KeepAspectRatio))
        #label.setScaledContents(True)
        #self.setCentralWidget(label)
        self.lLogo.setFixedWidth(400)
        
        self.mainLayout.addStretch(1)

        
        
    def on_setActive(self):
        # self.mainWindow.setWindowFlags(Qt.Hint)
        self.mainWindow.showMaximized()
        # self.mainWindow.showFullScreen()