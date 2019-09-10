from animals import Animal
from interfaces import *

class Kikakapu(Animal, Identifiable, ICan_Inhabit_Swamp, IFreshwater,ISwimming):

    def __init__(self):
        Animal.__init__(self, "Fish")
        Identifiable.__init__(self)
        ICan_Inhabit_Swamp.__init__(self)
        IFreshwater.__init__(self)
        ISwimming.__init__(self)
        self.__prey = { "Smaller Fish" }
