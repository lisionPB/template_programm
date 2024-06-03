from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel
from PyQt5.QtCore import pyqtSignal

from mainFrame.screen import Screen
from mainFrame.screenPlay import ScreenPlay
from game.processLoadGame import ProcessLoadGame
from game.processStartGame import ProcessStartGame
from game.game import Game

class ScreenLoading(Screen):

    _sig_gameLoaded = pyqtSignal()
    _sig_loadfailed = pyqtSignal()

    def __init__(self, mainWindow, viewPlay: ScreenPlay):
        super().__init__(mainWindow)
        self.viewPlay = viewPlay
        
        self.mainLayout.addWidget(QLabel("Loading ..."))
    
    
    def loadGame(self, src=None):
        
        if(src):
            # TODO: Spiel laden
            pass
        else:
            # Neues Spiel
            self.process = ProcessStartGame(self.viewPlay)
            self.process._sig_gameStarted.connect(self.game_loaded)
            self.process._sig_StartFailed.connect(self.load_failed)
            
            
    def game_loaded(self):
        self._sig_gameLoaded.emit()
        
        
    def load_failed(self):
        # TODO: Show Error Message
        self._sig_loadfailed.emit()
            