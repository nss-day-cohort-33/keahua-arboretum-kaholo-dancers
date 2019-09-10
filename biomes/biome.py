
class Biome:

    def __init__(self, max_animal, max_plant, name):
        self.max_animals = max_animal
        self.max_plants = max_plant
        self.name = name
        self.animals = []
        self.plants = []

    def add_animal(self, animal):
        self.animals.append(animal)
