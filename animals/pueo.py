from animals import Animal
from interfaces import IFlying
from interfaces import Identifiable

class Pueo(Animal, IFlying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Short Eared Owl")
        IFlying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Rodents", "Mongoose"}