
class Biome:

    def __init__(self, max_animal, max_plant, name):
        self.max_animals = max_animal
        self.max_plants = max_plant
        self.name = name
        self.animals = []
        self.plants = []


    def add_animal(self, animal, menu):
        length = len(self.animals)
        if length < self.max_animals:
            self.animals.append(animal)
        else:
            print(f'***That Biome is not large enough. Please choose Another***')
            print(f'              ***Please choose another one***')
            menu(animal)


    def add_plant(self, plant, menu):
        length = len(self.plants)
        if length < self.max_plants:
            self.plants.append(plant)
        else:
            print(f'That Biome Is Not Large Enough. Please Choose Another')
            menu(plant)


