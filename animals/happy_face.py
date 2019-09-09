from animals import Animal
from interfaces import Identifiable
from interfaces.terrestrial import ITerrestrial

class Hawaiian_Happy_Face_Spider(Animal, Identifiable, ITerrestrial):

    def __init__(self):
        Animal.__init__(self, "Spider")
        Identifiable.__init__(self)
        ITerrestrial.__init__(self)
        self.__prey = { "Insects" }