"""
author: Paul
version: v0.2
lastChange: 31.7.23
"""
import ctypes

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QCloseEvent, QKeyEvent

from PyQt5.QtWidgets import QMainWindow, QAction

from mainFrame.helpDialog import HelpDialog

from datenerfassung.hwSetup import HWSetup

import mainFrame.viewLayerManager as vlm
import mainFrame.viewContainer as vc



class MainFrame(QMainWindow):

    
    TITEL = "Staubkammer Prüfsystem"
    VERSION = "0.0.1"
    YEAR = "2024"

    def __init__(self):
        super().__init__()

        # Setze Name und Symbol in Titelleiste 
        self.setWindowTitle(self.TITEL)
        self.setWindowIcon(QIcon("symbols/lision.ico"))

        # Setze Symbol in der Taskleiste
        myappid = u'lision.DaEf.Staubkammer.' + self.VERSION
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        
        ########
        # MENÜ	

        menuBar = self.menuBar()

        # Hilfe öffnen
        helpMenu = menuBar.addMenu('&Hilfe')
        helpAct = QAction('&Hilfe öffnen', self)
        helpAct.setStatusTip('Hilfe öffnen')
        helpAct.triggered.connect(self.open_help)
        helpMenu.addAction(helpAct)        
        
        
        
        
        
        # HW-Setup -> Wird in Init-Prozess initialisiert
        self.hwSetup = HWSetup()
        
        

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


    def set_hwSetup(self, hwSetup):
        self.hwSetup = hwSetup


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
        
        
    ##################
    # Dialoge
    # 
    
        
    def open_help(self):
        help = HelpDialog(self.TITEL, self.VERSION, self.YEAR)
        help.exec()