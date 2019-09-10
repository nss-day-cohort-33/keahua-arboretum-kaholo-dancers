from .biome import Biome
from interfaces import Identifiable

class Grassland(Biome, Identifiable):

    def __init__(self):
        Biome.__init__(self, 22, 15, "Grassland")
        Identifiable.__init__(self)
