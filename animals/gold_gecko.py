from animals import Animal
from interfaces.saltwater import ISaltwater
from interfaces import Identifiable
from interfaces.terrestrial import ITerrestrial

class Gold_Dust_Day_Gecko(Animal, ISaltwater, Identifiable, ITerrestrial):

    def __init__(self):
        Animal.__init__(self, "Lizard")
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        ITerrestrial.__init__(self)
        self.__prey = { "Insects" }