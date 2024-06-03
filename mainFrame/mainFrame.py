"""
author: Paul
version: v0.2
lastChange: 31.7.23
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QKeyEvent

from PyQt5.QtWidgets import QMainWindow

import mainFrame.viewLayerManager as vlm
import mainFrame.viewContainer as vc

class MainFrame(QMainWindow):

    def __init__(self):
        super().__init__()

        # Init Viel Layer Manager
        self.vlm = vlm.ViewLayerManager(self)
        

        # ViewContainer
        self.viewContainer = vc.ViewContainer()
        self.setCentralWidget(self.viewContainer)

        # Setze View in Controller 
        self.vlm.set_viewContainer(self.viewContainer)

        

    def set_viewLayerManager(self, vlm):
        self.vlm = vlm



    def set_viewLayout(self, layout, structure):
        """
        Übergibt die neue Struktur an die MainView
        """
        self.view.set_layout(layout, structure)



    #################
    # EVENT HANDLER
    #


    def keyPressEvent(self, a0: QKeyEvent) -> None:
        self.vlm.handleKeyPress(a0)
        return super().keyPressEvent(a0)
    
    
    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        self.vlm.handleKeyRelease(a0)
        return super().keyReleaseEvent(a0)
    


    ################
    # Close Event Handler
    # 

    def closeEvent(self, a0: QCloseEvent) -> None:
        return super().closeEvent(a0)
        print("closed")