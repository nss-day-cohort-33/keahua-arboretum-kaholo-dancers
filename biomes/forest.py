from .biome import Biome


class Forest(Biome):

    def __init__(self, name):
        Biome.__init__(self, 20, 32, "Forest")
