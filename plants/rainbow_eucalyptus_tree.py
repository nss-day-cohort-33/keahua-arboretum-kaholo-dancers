from .plant import Plant
from interfaces import Identifiable


class Rainbow_Tree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "full", 8, "low", "Rainbow Eucalyptus Tree")
        Identifiable.__init__(self)
