class Animal:

    def __init__(self, species, prey):
        self.species = species
        self.prey = prey
        
    def feed(self, species, prey):
        print(f"{self.species} ate {self.prey}")

    # def move(self, propulsion, speed):
    #     return f"{self. species} moves at {speed} meters/sec by {propulsion}"
