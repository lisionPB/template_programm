from PyQt5.QtWidgets import QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel

from PyQt5.QtCore import pyqtSignal

class Screen(QGroupBox):

    def __init__(self, mainWindow):
        super().__init__()

        self.mainWindow = mainWindow
    
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)  


    def on_setActive(self):
        pass

    def on_setInactive(self):
        pass
