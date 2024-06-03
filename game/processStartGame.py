from PyQt5.QtCore import Qt, pyqtSignal


from mainFrame.process import Process
from mainFrame.screenPlay import ScreenPlay
from game.game import Game



class ProcessStartGame(Process):
    
    _sig_StartFailed = pyqtSignal()
    _sig_gameStarted = pyqtSignal()
    
    def __init__(self, viewPlay: ScreenPlay):
        super().__init__()
        self.viewPlay = viewPlay
        self.startProcess()
        
        
    def runProcess(self):
        self.viewPlay.startGame()
        self._sig_gameStarted.emit()
        #TODO: Catch Start Failed