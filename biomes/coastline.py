from .biome import Biome


class Coastline(Biome):

    def __init__(self, name):
        Biome.__init__(self, 15, 3, "Coastline")
