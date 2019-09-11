from .plant import Plant
from interfaces import Identifiable

class Mtn_Apple_Tree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "partial", 17, "high", "Mountain Apple Tree")
        Identifiable.__init__(self)
