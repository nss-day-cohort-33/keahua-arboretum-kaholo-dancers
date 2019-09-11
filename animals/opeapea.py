from animals import Animal
from interfaces import *

class Opeapea(Animal, IFlying, ICan_Inhabit_Forest, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Hiary Bat", "Ope'ape'a")
        IFlying.__init__(self, False)
        ICan_Inhabit_Forest.__init__(self)
        Identifiable.__init__(self)
        self.prey = ["Termites", "Moths", "Beetles", "Grass", "Weeds", "Berries"]