from animals import Animal
# from interfaces import IFlying
from interfaces import Identifiable

class Opeapea(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Hiary Bat")
        # IFlying.__init__(self)
        Identifiable.__init__(self)
        self.prey = ["Termites", "Moths", "Beetles", "Grass", "Weeds", "Berries"]