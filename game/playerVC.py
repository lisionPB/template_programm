from game.player import Player
from game.world.live.human import Human


class PlayerVC(Player):
    
    def __init__(self):
        self.me = Human(pos = [0,0,0])
        
        
        
    