from interfaces import Identifiable
from animals import RiverDolphin
# from interfaces import Identifiable
# from interfaces import IContainsAnimals
# from interfaces import IContainsPlants
# from animals import RiverDolphin
from .biome import Biome

class River(Biome, Identifiable):

    def __init__(self):
        Biome.__init__(self, 12, 6, self)
        Identifiable.__init__(self)

#     def add_animal(self, animal):
#         try:
#             if animal.aquatic and animal.cell_type == "hypertonic":
#                 self.animals.append(animal)
#         except AttributeError:
#             raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

#     def add_plant(self, plant):
#         try:
#             if plant.freshwater and plant.requires_current:
#                 self.plants.append(plant)
#         except AttributeError:
#             raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
