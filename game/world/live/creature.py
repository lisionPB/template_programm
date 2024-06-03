from game.world.worldObject import WorldObject

class Creature(WorldObject):
    
    def __init__(self, pos):
        super().__init__(pos)
        
        self.lifeEnergy = 100.0
        self.health = 100.0
        
        
    def _updateObjectSpecificBehaviour(self):
        # TODO: Berechne Life von Health
        pass
    
    def _calcResultingForces(self):
        # TODO: Berechne Forces aus Verhalten
        pass