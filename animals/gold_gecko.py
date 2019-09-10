from animals import Animal
from interfaces import Identifiable

class Gold_Dust_Day_Gecko(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Lizard")
        Identifiable.__init__(self)
        self.__prey = { "Insects" }