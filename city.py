class City:
    def __init__(self, name, mayor, est):
        self.name = name
        self.mayor = mayor
        self.est = est
        self.buildings = list()

    def addBuilding(self, buildings):
        self.buildings.append(buildings)

    
        