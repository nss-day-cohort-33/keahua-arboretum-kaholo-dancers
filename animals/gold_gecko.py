from animals import Animal
from interfaces import ISaltwater
from interfaces import Identifiable

class Gold_Dust_Day_Gecko(Animal, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Lizard")
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = ["Termites", "Moths", "Beetles"]
