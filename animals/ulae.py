from animals import Animal
from interfaces import *

class Ulae(Animal, ISaltwater, ISwimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Lizardfish", "Ulae")
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.prey = ["Trout", "Mackarel", "Sardine"]