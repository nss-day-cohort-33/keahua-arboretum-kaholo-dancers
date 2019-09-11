from animals import RiverDolphin
from interfaces import *
from .biome import Biome

class River(Biome, IFreshwater, Identifiable):

    def __init__(self):
        Biome.__init__(self, 12, 6, "River")
        Identifiable.__init__(self)

    # def add_animal(self, animal):
    #     try:
    #         if animal.IFreshwater and animal.ISwimming:
    #             self.animals.append(animal)
    #     except AttributeError:
    #         raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

#     def add_plant(self, plant):
#         try:
#             if plant.freshwater and plant.requires_current:
#                 self.plants.append(plant)
#         except AttributeError:
#             raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
