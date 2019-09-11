from .plant import Plant
from interfaces import Identifiable


class Silversword(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "shade", 22, "high", "Silversword")
        Identifiable.__init__(self)
