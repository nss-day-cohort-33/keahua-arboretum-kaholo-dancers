from .plant import Plant
from interfaces import Identifiable

class Blue_Jade(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "partial", 0, "medium", "Blue Jade Vine")
        Identifiable.__init__(self)

