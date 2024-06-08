from mainFrame.process import Process

from datenerfassung.hwSetup import HWSetup
from datenerfassung.comBundle import ComBundle

from PyQt5.QtCore import pyqtSignal

import time

class ProcessInit(Process):
    
    _sig_stateProgress = pyqtSignal(float)
    
    def __init__(self):
        super().__init__()
        self.statusText = "Lade Hardwarekonfig ... " 
        self.result = None
        
            
    
    def runProcess(self):
        
        
        self.statusText = "Lade HW Setup ..."
        
        # Load HW-Setup
        #testHWSetup = HWSetup()
        #testBundle = ComBundle(configURL="config\config.json")
        #testHWSetup.addBundle("test", testBundle)
        #self.result = testHWSetup
        
        
        
        # Simulate loading
        self._sig_stateProgress.emit(0.5)
        time.sleep(0.1)
        
        self._sig_stateProgress.emit(0.7)
        self.statusText = "Gleich gehts los ..."
        time.sleep(0.2)
        
        self._sig_stateProgress.emit(0.9)
        time.sleep(0.2)
        
        self._sig_stateProgress.emit(1.0)
        time.sleep(0.1)