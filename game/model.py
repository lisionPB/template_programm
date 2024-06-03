import time

from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage

import modelio

class Model():

    UPDATE_RELOAD_MODEL_ITEMS = 0
    
    def __init__(self):
        self.vlm = None
        self.initModel()

    
    def initModel(self, config=None):

        pass




    def handlePlayerInput(self, input):

        # TODO: To be filled

        pass
            
                

    def update_model(self):

        # TODO: To be filled

        pass



    def setViewManager(self, viewLayerManager):
        self.vlm = viewLayerManager





    def __getstate__(self):
        state = self.__dict__.copy()
        # Don't pickle baz
        del state["vlm"]
        return state
    


    def __setstate__(self, state):
        self.__dict__.update(state)