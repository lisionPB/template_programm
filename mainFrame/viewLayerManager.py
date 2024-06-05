
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
from mainFrame.screenCheckStaub import ScreenCheckStaub

from mainFrame.screenCheckBerst import ScreenCheckBerst

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
    VIEWID_PRUEF_STAUBTECH = 4
    VIEWID_CHECK_BERSTFEST = 5
    VIEWID_PRUEF_BERSTFEST = 6
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
        vMenu._sig_StartSchweis.connect(self.__checkSchweis)
        vMenu._sig_StartStaub.connect(self.__checkStaub)
        vMenu._sig_StartBerst.connect(self.__checkBerst)
        #vMenu._sig_quit.connect(self.__quit)
        
        #####
        # MESSPROGRAMME
        
        # Schweis 
        self.vCheckSchweis = ScreenCheckSchweis(self.mainWindow)
        self.__vc.add_view(self.VIEWID_CHECK_SCHWEIS, self.vCheckSchweis)
        self.vCheckSchweis._sig_quit.connect(self.__zumMenu)
        self.vCheckSchweis._sig_start.connect(self.__startSchweis)
        
        self.vPruefSchweis = ScreenPruefSchweis(self.mainWindow)
        self.__vc.add_view(self.VIEWID_PRUEF_SCHWEIS, self.vPruefSchweis)
        
        
        # Staub
        self.vCheckStaub = ScreenCheckStaub(self.mainWindow)
        self.__vc.add_view(self.VIEWID_CHECK_STAUBTECH, self.vCheckStaub)
        self.vCheckStaub._sig_quit.connect(self.__zumMenu)
        
        
        # Berst
        self.vCheckBerst = ScreenCheckBerst(self.mainWindow)
        self.__vc.add_view(self.VIEWID_CHECK_BERSTFEST, self.vCheckBerst)
        self.vCheckBerst._sig_quit.connect(self.__zumMenu)
        
        
        #####
        # CREDITS
        vCredits = ScreenCredits(self.mainWindow)
        self.__vc.add_view(self.VIEWID_CREDITS, vCredits)
        vCredits.process._sig_processEnded.connect(self.__close)

        

    ##########
    # Screen Switching

    def __initComplete(self):
        self.__vc.set_currentView(self.VIEWID_MENU)


    def __checkSchweis(self):
        self.__vc.set_currentView(self.VIEWID_CHECK_SCHWEIS)
        
        
    def __checkStaub(self):
        self.__vc.set_currentView(self.VIEWID_CHECK_STAUBTECH)
        
        
    def __checkBerst(self):
        self.__vc.set_currentView(self.VIEWID_CHECK_BERSTFEST)


    def __startSchweis(self):
        self.__vc.set_currentView(self.VIEWID_PRUEF_SCHWEIS)
        
        
    def __startStaub(self):
        self.__vc.set_currentView(self.VIEWID_PRUEF_STAUBTECH)
        
        
    def __startBerst(self):
        self.__vc.set_currentView(self.VIEWID_PRUEF_BERSTFEST)
        
    
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