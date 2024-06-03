from process import Process

import time

class ProcessMenu(Process):
    
    def __init__(self):
        super().__init__()
    
    
    def _startProcess(self):
        pass
        
    
    def __load(self):
        time.sleep(10)
        self._endProcess()
        
        