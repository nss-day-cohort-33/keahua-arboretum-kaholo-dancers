from .biome import Biome
from interfaces import Identifiable

class Forest(Biome, Identifiable):

    def __init__(self):
        Biome.__init__(self, 20, 32, self)
        Identifiable.__init__(self)
