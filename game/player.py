"""
    Allgemeine Klasse zur Kontrolle des Spielgeschehens (Welt und Spieleritems)
"""

from game.world.worldObject import WorldObject

class Player():

    def __init__(self, material):
        """

        Args:
            material (list of WorldObject)
        """
        self.material = material
    
    