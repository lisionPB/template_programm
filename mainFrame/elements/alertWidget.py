from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.Qt import QPixmap

class AlertWidget(QGroupBox):
    
    
    def __init__(self, name):
        super().__init__()
  
        self.bildIdle = QPixmap(("symbols/light_red_dark.png"))
        self.bildAlert = QPixmap("symbols/light_red.png")

        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        
        self.lImg = QLabel()
        self.mainLayout.addWidget(self.lImg)
        self.setAlert(False)
        
        self.lAlertText = QLabel(name)
        self.mainLayout.addWidget(self.lAlertText)
        
        self.mainLayout.addStretch(1)
        
        
    def setAlert(self, alert):
        if(alert):
            self.lImg.setPixmap(self.bildAlert)
        else:
            self.lImg.setPixmap(self.bildIdle)
        