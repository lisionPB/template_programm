from PyQt5.QtWidgets import QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QApplication, QProgressBar
import PyQt5.QtCore
from PyQt5.QtCore import pyqtSignal

from mainFrame.screen import Screen

from mainFrame.processInit import ProcessInit

class ScreenInit(Screen):

    sig_initDone = pyqtSignal()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400

    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        # background image
        self.setStyleSheet('background-image:url("symbols/start.png"); background-repeat: no-repeat')
        
        self.layout().setContentsMargins(0,0,0,0)
        self.setContentsMargins(0,0,0,0)
        
        # self.text = QLabel("Press Any Key to Enter!")
        # self.mainLayout.addWidget(self.text)

        # skip on key
        
        self.mainLayout.addStretch(1)
        
        self.lStatus = QLabel("")
        self.mainLayout.addWidget(self.lStatus)
        
        self.prbProgress = QProgressBar()
        self.mainLayout.addWidget(self.prbProgress)
        
        
        # Incldude Init-Process
        self.process = ProcessInit()
        
        self.process._sig_stateProgress.connect(self.updateProgress)

    
    def updateProgress(self, fortschritt):
        self.prbProgress.setValue(fortschritt * 100)
        self.lStatus.setText(self.process.statusText)
    
    
    def on_setActive(self):
        # größe
        displayWidth = QApplication.primaryScreen().size().width()
        displayHeight = QApplication.primaryScreen().size().height()
        self.mainWindow.setGeometry(int((displayWidth - self.SCREEN_WIDTH) / 2),  int((displayHeight - self.SCREEN_HEIGHT) / 2) ,self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        # self.mainWindow.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint)
        
        self.process.startProcess()
