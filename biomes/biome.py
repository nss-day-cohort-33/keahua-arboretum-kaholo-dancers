
class Biome:

    def __init__(self, max_animal, max_plant, name):
        self.max_animals = max_animal
        self.max_plants = max_plant
        self.name = name
        self.animals = []
        self.plants = []

        def add_animal(self, animal):
            try:
                if animal.IFreshwater and animal.ISwimming:
                  self.animals.append(animal)
            except AttributeError:
                raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")
