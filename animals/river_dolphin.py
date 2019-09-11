from animals import Animal
from interfaces import *

class RiverDolphin(Animal, IFreshwater, ISwimming, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Dolphin", "River Dolphin")
        IFreshwater.__init__(self)
        Identifiable.__init__(self)
        self.prey = ["Trout", "Mackarel", "Sardine"]



    # @property
    # def prey(self):
    #     return self.__prey

    # def feed(self, prey):
    #     if prey in self.__prey:
    #         print(f'The dolphin ate {prey} for a meal')
    #     else:
    #         print(f'The dolphin rejects the {prey}')


    # def __str__(self):
    #     return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
