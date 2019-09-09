from animals import Animal
from interfaces.saltwater import ISaltwater
from interfaces import Identifiable
from interfaces.swimming import ISwimming

class Kikakapu(Animal, ISaltwater, Identifiable, ISwimming):

    def __init__(self):
        Animal.__init__(self, "Fish")
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        ISwimming.__init__(self, 4, 20)
        self.__prey = { "Smaller Fish" }
