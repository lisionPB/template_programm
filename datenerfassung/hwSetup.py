class HWSetup():

    def __init__(self):
        self.bundles = {}
        self.einstellungen = {}
        
        
    def addBundle(self, name, bundle):
        self.bundles[name] = bundle