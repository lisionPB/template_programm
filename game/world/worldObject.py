class WorldObject():
    
    def __init__(self, pos):
        self.pos = pos
        
        
    def calcUpdateChanges(self):
        # TODO: Change to Changes -> dict
        
        self._updateObjectSpecificBehaviour()
        self.frc = self._calcResultingForces()
        self.__updatePhysics()
        
        
    def applyUpdateChanges(self):
        # TODO: Use Changes Dict and apply to values
        pass
        
        
        


#################
# To be overridden

    def _updateObjectSpecificBehaviour(self):
        pass
    

    def _calcResultingForces(self) -> list:
        return [0.0 for x in range(len(pos))]
        
        
        
###################
# Genuine Methods
        
    def __updatePhysics(self):
        # TODO: Calc Pos von Vel von Acc von Frc
        pass