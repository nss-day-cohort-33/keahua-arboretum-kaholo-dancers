from animals import Animal
from interfaces import *
# from interfaces.terrestrial import ITerrestrial

class Hawaiian_Happy_Face_Spider(Animal, Identifiable, ICan_Inhabit_Swamp):

    def __init__(self):
        Animal.__init__(self, "Spider", "Hawaiin Happy Face Spider")
        Identifiable.__init__(self)
        ICan_Inhabit_Swamp.__init__(self)
        self.prey = ["Termites", "Moths", "Beetles"]
