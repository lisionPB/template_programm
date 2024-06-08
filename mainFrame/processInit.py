from mainFrame.process import Process

from PyQt5.QtCore import pyqtSignal

import time

class ProcessInit(Process):
    
    _sig_stateProgress = pyqtSignal(float)
    
    def __init__(self):
        super().__init__()
        self.statusText = "Lade Hardwarekonfig ... " 
        
            
    
    def runProcess(self):
        
        # Simulate loading
        self._sig_stateProgress.emit(0.1)
        time.sleep(0.1)
        
        self._sig_stateProgress.emit(0.2)
        self.statusText = "Begrüße Wolfgang ..."
        time.sleep(0.5)
        
        self._sig_stateProgress.emit(0.4)
        time.sleep(0.0)
        
        self._sig_stateProgress.emit(0.7)
        self.statusText = "Gleich gehts los ..."
        time.sleep(0.2)
        
        self._sig_stateProgress.emit(0.9)
        time.sleep(0.2)
        
        self._sig_stateProgress.emit(1.0)
        time.sleep(0.1)