from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal


from mainFrame.screen import Screen

class ScreenPause(Screen):

    _sig_quit = pyqtSignal()
    _sig_continue = pyqtSignal()


    def __init__(self, mainWindow):
        super().__init__(mainWindow)    
        
        self.mainLayout.addStretch(1)

        self.groupCenter = QGroupBox()
        self.mainLayout.addWidget(self.groupCenter)
        self.centerLayout = QVBoxLayout()
        self.groupCenter.setLayout(self.centerLayout)
        self.groupCenter.setFixedWidth(400)
        # self.groupCenter.setFixedHeight(800)
        
        self.centerLayout.addStretch(1)      
    
        # Continue Game
        self.pbContinue = QPushButton("Continue")
        self.centerLayout.addWidget(self.pbContinue)
        self.pbContinue.clicked.connect(self.on_ContinueClicked)
    
        # Quit Game to Menu
        self.pbQuit = QPushButton("Quit Game")
        self.centerLayout.addWidget(self.pbQuit)
        self.pbQuit.clicked.connect(self.on_QuitClicked)
            
        self.centerLayout.addStretch(1)      
    
        
        
        
        self.mainLayout.addStretch(1)
        
        

    def on_QuitClicked(self):
        self._sig_quit.emit()


    def on_ContinueClicked(self):
        self._sig_continue.emit()

        
        