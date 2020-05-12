from . import RandomAgent, SimpleAgent
from pommerman.characters import Bomber

class Pacifist(Bomber):
    @property
    def ammo(self):
        return 0

    @ammo.setter
    def ammo(self, _):
        self._ammo = 0

class RandomPacifist(RandomAgent):
    """A RandomAgent that never uses bombs."""
    def __init__(self):
        super(RandomPacifist, self).__init__(character=Pacifist)


class SimplePacifist(SimpleAgent):
    """A SimpleAgent that never uses bombs."""
    def __init__(self):
        super(SimplePacifist, self).__init__(character=Pacifist)
