from .biome import Biome


class Mountain(Biome):

    def __init__(self, name):
        Biome.__init__(self, 6, 4, "Mountain")
