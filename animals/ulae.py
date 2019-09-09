from animals import Animal
from interfaces.saltwater import ISaltwater
from interfaces import Identifiable
from interfaces.swimming import ISwimming

class Ulae(Animal, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Lizardfish")
        ISwimming.__init__(self, 4, 10)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Smaller fish" }