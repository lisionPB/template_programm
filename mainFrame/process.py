from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread

class Process(QObject):
    
    _sig_processStarted = pyqtSignal()
    _sig_processEnded = pyqtSignal()
    
    STATE_IDLE = 0
    STATE_RUNNING = 1
    STATE_FAILURE = 2
    STATE_FINISHED = 3
    
    def __init__(self):
        super().__init__()
        
        self._thread = QThread()
        self._worker = ProcessThread(self)
        self._worker.moveToThread(self._thread)
        
        self._thread.started.connect(self._worker.run)
        self._worker._sig_finished.connect(self._thread.quit)
        self._worker._sig_finished.connect(self._worker.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        
        self.__state = self.STATE_IDLE    
    
    
    def startProcess(self):
        self._thread.start()
        self.__state = self.STATE_RUNNING
        self._sig_processStarted.emit()
    
    
    def runProcess(self):
        pass
    
    
    def endProcess(self):
        self.__state = self.STATE_FINISHED
        self._sig_processEnded.emit()
        
        
    def getState(self):
        return self.__state
    
    
    
###############################################################################################    
    
class ProcessThread(QThread):
    
    _sig_finished = pyqtSignal()
    
    def __init__(self, process: Process):
        QThread.__init__(self)
        self.p = process
        
    def run(self):
        self.p.runProcess()
        self.p.endProcess()