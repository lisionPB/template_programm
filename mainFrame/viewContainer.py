"""
author: Paul Benz
lastChange: 31.07.23
version: v0.2

Concept:
* Layout von QWidget und dessen Organisation
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from mainFrame.screen import Screen

class ViewContainer(QWidget):
    
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.viewStructure = {}
        self.currentView = None

        # Remove Margins and Border 
        self.layout().setContentsMargins(0,0,0,0)
        # self.setStyleSheet("border: 0px;")


    def add_view(self, viewID, view: Screen):
        self.viewStructure[viewID]  = view
        self.mainLayout.addWidget(view)


    def set_currentView(self, viewID):
        for v in self.viewStructure:
            visible = (v == viewID)
            self.viewStructure[v].setVisible(visible)
            if(visible):
                self.viewStructure[v].on_setActive()
            else:
                self.viewStructure[v].on_setInactive()