from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from mainFrame.screen import Screen

class ScreenMenu(Screen):

    _sig_start = pyqtSignal()
    _sig_load = pyqtSignal()
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
        pbStart.clicked.connect(self.on_StartClicked)

        pbLoad = QPushButton("LOAD")
        self.centerLayout.addWidget(pbLoad)
        pbLoad.setEnabled(False)
        pbLoad.clicked.connect(self.on_LoadClicked)

        pbQuit = QPushButton("QUIT")
        self.centerLayout.addWidget(pbQuit)
        pbQuit.clicked.connect(self.on_QuitClicked)
        
        self.centerLayout.addStretch(2)
        
        self.mainLayout.addStretch(1)


    def on_StartClicked(self):
        self._sig_start.emit()    
    
    def on_LoadClicked(self):
        self._sig_load.emit()
    
    def on_QuitClicked(self):
        self._sig_quit.emit()
        
        
    def on_setActive(self):
        # self.mainWindow.setWindowState(Qt.WindowMaximized)
        self.mainWindow.showFullScreen()