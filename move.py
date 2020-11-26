

import utils
from future import standard_library

standard_library.install_aliases()
# ...
from builtins import bytes
from builtins import open
from future.utils import with_metaclass


class Move:
    """
    Move object including norm and direction
    """

    def __init__(self, direction, norm=1):
        self.dir = direction
        self.n = norm

    def norm(self):
        return self.n

    def direction(self):
        return self.dir

    def apply(self, point):
        return utils.add(point, self.direction(), mu=self.norm())

    def applyDirection(self, point, mu=1):
        return utils.add(point, self.direction(), mu=mu)

    def __repr__(self):
        return str(self.dir)
        #return "({}, {})".format(self.dir, self.norm)

