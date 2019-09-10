from animals import Animal
from interfaces import Identifiable

class Hawaiian_Happy_Face_Spider(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Spider")
        Identifiable.__init__(self)
        self.__prey = ["Termites", "Moths", "Beetles"]