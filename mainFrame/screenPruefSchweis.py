from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from mainFrame.screen import Screen

class ScreenPruefSchweis(Screen):

    _sig_start = pyqtSignal()
    _sig_quit = pyqtSignal()
    
    
    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.mainLayout.addStretch(1)

        self.groupCenter = QGroupBox()
        self.mainLayout.addWidget(self.groupCenter)
        self.centerLayout = QVBoxLayout()
        self.groupCenter.setLayout(self.centerLayout)
        self.groupCenter.setFixedWidth(400)

        self.centerLayout.addStretch(1)

        pbStart = QPushButton("START")
        self.centerLayout.addWidget(pbStart)
        pbStart.clicked.connect(self._sig_start.emit)

        pbQuit = QPushButton("ENDE")
        self.centerLayout.addWidget(pbQuit)
        pbQuit.clicked.connect(self._sig_quit.emit)
        
        self.centerLayout.addStretch(2)
        
        self.mainLayout.addStretch(1)