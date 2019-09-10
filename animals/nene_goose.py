from animals import Animal
# from interfaces import IFlying
from interfaces import *

class Nene_Goose(Animal, IFlying, ICan_Inhabit_Grassland, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Bird")
        IFlying.__init__(self)
        ICan_Inhabit_Forest.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Grass", "Weedy Plants", "Berries"}