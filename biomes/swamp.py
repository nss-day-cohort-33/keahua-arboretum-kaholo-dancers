from .biome import Biome
from interfaces import Identifiable

# from environments.environment import Environment
# from interfaces.habitat import IStagnant
# from animals.

# from interfaces.habitats import IStagnant

class Swamp(Biome, Identifiable):

    def __init__(self):
        Biome.__init__(self, 8, 12, "Swamp")
        Identifiable.__init__(self)
        # self.name = name
        # self.inhabitants = []

        # def add_plant(self, plant):
        #     try:
        #         if plant.seeds == 0:
        #             self.plants.append(plant)
        #     except AttributeError:
        #         raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")


# blue_jade_vine1 = Blue_Jade()

# swamp1 = Swamp()

# swamp1.add_plant(blue_jade_vine1)



    # def animal_count(self):
    #     return "This place has a bunch of animals in it"

    # def addInhabitant(self, item):
    #     if not isinstance(item):
    #         raise TypeError(f"{item} is not of type IStagnant")
    #     self.inhabitants.append(item)

    # def __str__(self):
    #     return self.name
