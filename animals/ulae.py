from animals import Animal
from interfaces import ISaltwater
from interfaces import Identifiable
from interfaces import ISwimming

class Ulae(Animal, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Lizardfish")
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.prey = ["Trout", "Mackarel", "Sardine"]