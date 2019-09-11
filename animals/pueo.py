from animals import Animal
from interfaces import *

class Pueo(Animal, IFlying, ICan_Inhabit_Grassland, ICan_Inhabit_Forest, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Short Eared Owl", "Pueo")
        IFlying.__init__(self, True)
        ICan_Inhabit_Grassland.__init__(self)
        ICan_Inhabit_Forest.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Rodents", "Mongoose"}