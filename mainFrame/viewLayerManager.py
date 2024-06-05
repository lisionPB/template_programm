
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsScene
from PyQt5.QtGui import QPen, QBrush, QColor

"""
author: Paul
version: v0.4
lastChange: 05.05.24

Koordination von Layern (Views) mit Widgets und Daten

Controller funktion


"""

from mainFrame.screenInit import ScreenInit
from mainFrame.screenMenu import ScreenMenu
from mainFrame.screenCheckSchweis import ScreenCheckSchweis
from mainFrame.screenPruefSchweis import ScreenPruefSchweis
from mainFrame.screenCredits import ScreenCredits

class ViewLayerManager():
    
    """
    Template für ViewManager
    """

    # VIEW_IDs
    VIEWID_INIT = -1
    VIEWID_MENU = 0
    VIEWID_CHECK_SCHWEIS = 1
    VIEWID_PRUEF_SCHWEIS = 2
    VIEWID_CHECK_STAUBTECH = 3
    VIEWID_STAUBTECH = 4
    VIEWID_CHECK_BERSTFEST = 5
    VIEWID_BERSTFEST = 6
    VIEWID_CREDITS = 7


    def __init__(self, mainWindow):

        self.mainWindow = mainWindow

        self.__vc = None  # ViewContainer
        
        

    def set_viewContainer(self, vc):
        self.__vc = vc
        
        # Initialisiere Views
        self.init_views()
        
        # Aktiviere aktuelle View
        self.__vc.set_currentView(self.VIEWID_INIT)
        
        
        
    def init_views(self):
        
        # INIT
        vInit = ScreenInit(self.mainWindow)
        self.__vc.add_view(self.VIEWID_INIT, vInit)
        vInit.process._sig_processEnded.connect(self.__initComplete)
        
        # MENU
        vMenu = ScreenMenu(self.mainWindow)
        self.__vc.add_view(self.VIEWID_MENU, vMenu)
        vMenu._sig_StartSchweis.connect(self.__startSchweis)
        #vMenu._sig_quit.connect(self.__quit)
        
        # MESSPROGRAMME
        self.vCheckSchweis = ScreenCheckSchweis(self.mainWindow)
        self.__vc.add_view(self.VIEWID_CHECK_SCHWEIS, self.vCheckSchweis)
        self.vCheckSchweis._sig_quit.connect(self.__zumMenu)
        
        self.vPruefSchweis = ScreenPruefSchweis(self.mainWindow)
        self.__vc.add_view(self.VIEWID_PRUEF_SCHWEIS, self.vPruefSchweis)
        
        
        # CREDITS
        vCredits = ScreenCredits(self.mainWindow)
        self.__vc.add_view(self.VIEWID_CREDITS, vCredits)
        vCredits.process._sig_processEnded.connect(self.__close)

        

    ##########
    # Screen Switching

    def __initComplete(self):
        self.__vc.set_currentView(self.VIEWID_MENU)


    def __startSchweis(self):
        self.__vc.set_currentView(self.VIEWID_CHECK_SCHWEIS)
        
    
    def __zumMenu(self):
        self.__vc.set_currentView(self.VIEWID_MENU)

        
    def __quit(self):
        self.__vc.set_currentView(self.VIEWID_CREDITS)
        


#######################
# Genuine Functions
        
    def __close(self):
        self.mainWindow.close()


    def update_vlm(self):
        self.vlPlay.updateView()


################
# EVENT Handler
#

    def handleKeyPress(self, e):
        pass
    

    def handleKeyRelease(self, e):
        # Auto steuern

        print(e.key())

        input = {}

        # self.m.handlePlayerIn