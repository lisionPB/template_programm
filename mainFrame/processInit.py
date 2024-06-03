from mainFrame.process import Process

import time

class ProcessInit(Process):
    
    def __init__(self):
        super().__init__()
    
    
    def runProcess(self):
        time.sleep(1)