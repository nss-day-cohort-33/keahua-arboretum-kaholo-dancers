from animals import Animal
from interfaces import *

class Gold_Dust_Day_Gecko(Animal, ICan_Inhabit_Forest, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Lizard", "Gold Dust Day Gecko")
        ICan_Inhabit_Forest.__init__(self)
        Identifiable.__init__(self)
        self.prey = ["Termites", "Moths", "Beetles"]
