from game.world.worldObject import WorldObject

class World():
    
    def __init__(self, worldobjects):
        self.wos = worldobjects
        
    
    def update(self):
        # calc changes
        for w in self.wos:
            w.calcUpdateChanges()
            
        # apply changes
        for w in self.wos:    
            w.applyUpdateChanges()
            
        # delete dead objects
        for w in enumerate(reversed(self.wos)):
            if(w.isDead()):
                self.wos.remove(w)