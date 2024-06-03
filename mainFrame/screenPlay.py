
import time

from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsScene, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from mainFrame.graphicsViewGame import WeltGraphicsViewWidget


from mainFrame.screen import Screen
from game.game import Game

class ScreenPlay(Screen):

    _sig_pause = pyqtSignal()

    def __init__(self, mainWindow):

        super().__init__(mainWindow)
        
        #####
        # Game
        
        self.game = None
        
        
        ##############
        # Left Menü
        
        self.menuGroup = QGroupBox()
        self.menuLayout = QVBoxLayout()
        self.menuGroup.setLayout(self.menuLayout)
        self.menuGroup.setFixedWidth(250)
        self.mainLayout.addWidget(self.menuGroup)
        
        # Pause Game
        self.pbPause = QPushButton("Pause")
        self.menuLayout.addWidget(self.pbPause)
        self.pbPause.clicked.connect(self.on_PauseClicked)


        ##############
        # Center (Welt)
        
        #qgs = QGraphicsScene()
        #qgs.addRect(100,100,100,100,QPen(),QBrush(QColor(0,0,0)))
        self.weltView = WeltGraphicsViewWidget()
        self.mainLayout.addWidget(self.weltView)

        ###############
        # Right Menu ?
        
        
    def on_PauseClicked(self):
        self._sig_pause.emit()
        
        
    
    def startGame(self):
        time.sleep(3)
        self.game = Game()
    
    
    def loadGame(self, sav):
        # TODO: Load Game
        pass
        
        
        
        
        
    def updateView (self):
        # WeltView
        self.weltView.update_graphicsView()
        # Status
        self.statusNameText.setText(self.m.getPlayer().name)
        self.statusEnergieText.setText(str(self.m.getPlayer().energie))



    def saveModel(self):
        # modelio.saveModelToFile(self.m, "sav/test.sav")
        pass
    
    def loadModel(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "sav/","All Files (*);; Save Files (*.sav)", options=options)
        if fileName:
            # self.m = modelio.loadModelFromFile(fileName)
            pass

    def setPlayerName(self, name):
        self.m.getPlayer().name = name


    def setPlayerEnergie(self, energie):
        self.m.getPlayer().energie = float(energie)
        
    