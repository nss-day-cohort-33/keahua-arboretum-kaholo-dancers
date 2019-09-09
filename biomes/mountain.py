from .biome import Biome
from interfaces import Identifiable


class Mountain(Biome, Identifiable):

    def __init__(self):
        Biome.__init__(self, 6, 4, self)
        Identifiable.__init__(self)
