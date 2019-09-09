from .biome import Biome


class Grassland(Biome):

    def __init__(self, name):
        Biome.__init__(self, 22, 15, "Grassland")
