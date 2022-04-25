from Node import Node


class Problem(object):
    def __init__(self, initial):
        if not isinstance(initial, Node):
            raise TypeError('node type is required for initial')

        self.initial = initial

    def expand(self, node):
        raise NotImplementedError

    def goal(self, node):
        raise NotImplementedError
