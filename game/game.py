import time

from game.player import Player
from game.world.world import World
 
class Game ():

    def __init__(self):
        # Init Model Time  
        self.gameTimeStart = time.time()      
        
        self.world = self.loadWorld()
        self.players = self.loadPlayers()








#######################################################
# Template Methods -> Adopt to needs !


    def update_model(self):
        # TODO: To be filled
        pass
    
    def loadWorld(self) -> World:
        # TODO: To be filled
        pass    

        
    def loadPlayers(self):
        # TODO: To be filled
        pass


    def handlePlayerInput(self, input):
        # TODO: To be filled
        pass



########################################################
# Genuine Methods -> Dont touch !


    def get_gameTimeStamp(self):
        return time.time() - self.gameTimeStart


    def __getstate__(self):
        state = self.__dict__.copy()
        # Don't pickle vlm
        # del state["vlm"]
        return state
    

    def __setstate__(self, state):
        self.__dict__.update(state)

    