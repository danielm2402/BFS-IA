from Node import Node

class Problem(object):

    def __init__(self, initial, goal, isExplicit = True ):

        if not isinstance(initial, Node):
            raise TypeError('node type is required for initial')
        if isExplicit:
            if not isinstance(goal, Node):
                raise TypeError('node type is required for initial')

        self.initial = initial
        self.goal = goal
        self.isExplicit = isExplicit

    def expand(self, node):

        raise NotImplementedError