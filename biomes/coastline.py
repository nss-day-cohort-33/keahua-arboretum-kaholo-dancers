from .biome import Biome
from interfaces import Identifiable


class Coastline(Biome, Identifiable):

    def __init__(self):
        Biome.__init__(self, 15, 3, self)
        Identifiable.__init__(self)
