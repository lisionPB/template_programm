from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QLabel

from mainFrame.screen import Screen
from mainFrame.processCredits import ProcessCredits

class ScreenCredits(Screen):

    def __init__(self, mainWindow):
        super().__init__(mainWindow)

        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        
        lGoodBye = QLabel("Good Bye!")
        self.mainLayout.addWidget(lGoodBye)

        self.process = ProcessCredits()
        
        
        
    def on_setActive(self):
        self.process.startProcess()