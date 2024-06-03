
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
from mainFrame.screenLoading import ScreenLoading
from mainFrame.screenPlay import ScreenPlay
from mainFrame.screenPause import ScreenPause
from mainFrame.screenCredits import ScreenCredits

class ViewLayerManager():
    
    """
    Template für ViewManager
    """

    # VIEW_IDs
    VIEWID_INIT = -1
    VIEWID_MENU = 0
    VIEWID_LOADGAME = 1
    VIEWID_PLAY = 2
    VIEWID_PAUSE = 3
    VIEWID_CREDITS = 4


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
        vInit.process._sig_processEnded.connect(self.__initComplete)
        
        # MENU
        vMenu = ScreenMenu(self.mainWindow)
        vMenu._sig_start.connect(self.__start)
        vMenu._sig_quit.connect(self.__quit)
        
        # PLAY
        self.vPlay = ScreenPlay(self.mainWindow)
        self.vPlay._sig_pause.connect(self.__pause)
        
        # LOADING
        self.vLoading = ScreenLoading(self.mainWindow, self.vPlay)
        self.vLoading._sig_gameLoaded.connect(self.__play)
        self.vLoading._sig_loadfailed.connect(self.__failedLoad)
        
        # PAUSE
        vPause = ScreenPause(self.mainWindow)
        vPause._sig_continue.connect(self.__continue)
        vPause._sig_quit.connect(self.__quitGame)
        
        # CREDITS
        vCredits = ScreenCredits(self.mainWindow)
        vCredits.process._sig_processEnded.connect(self.__close)
        
        
        #
        # Add Views to View Container
        
        self.__vc.add_view(self.VIEWID_INIT, vInit)
        self.__vc.add_view(self.VIEWID_MENU, vMenu)
        self.__vc.add_view(self.VIEWID_LOADGAME, self.vLoading)
        self.__vc.add_view(self.VIEWID_PLAY, self.vPlay)
        self.__vc.add_view(self.VIEWID_PAUSE, vPause)
        self.__vc.add_view(self.VIEWID_CREDITS, vCredits)
        

    ##########
    # Screen Switching

    def __initComplete(self):
        self.__vc.set_currentView(self.VIEWID_MENU)
        
    def __start(self):
        self.vLoading.loadGame()
        self.__vc.set_currentView(self.VIEWID_LOADGAME)
        
    def __play(self):
        self.__vc.set_currentView(self.VIEWID_PLAY)
        
        
    def __failedLoad(self):
        # TODO: Show Error Dialog
        pass
    
        
    def __pause(self):
        self.__vc.set_currentView(self.VIEWID_PAUSE)
        
    def __continue(self):
        self.__vc.set_currentView(self.VIEWID_PLAY)
        
    def __quitGame(self):
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