from animals import Animal
from interfaces.flying import IFlying
from interfaces import Identifiable

class Opeapea(Animal, IFlying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Hiary Bat")
        IFlying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Insects" }