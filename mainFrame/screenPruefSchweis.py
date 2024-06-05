from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from mainFrame.screen import Screen

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
        
        # Vol
        self.groupVol = QGroupBox()
        self.layoutTop.addWidget(self.groupVol)
        self.layoutVol = QVBoxLayout()
        self.groupVol.setLayout(self.layoutVol)
        
        self.lTest = QLabel("Test")
        self.layoutVol.addWidget(self.lTest)
        

        ###############
        # BOTTOM
        
        self.groupBottom = QGroupBox()
        self.mainLayout.addWidget(self.groupBottom)
        self.layoutBottom = QHBoxLayout()
        self.groupBottom.setLayout(self.layoutBottom)
        
        