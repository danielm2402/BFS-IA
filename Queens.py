import copy
from Node import Node
from Problem import Problem


class Queens(Problem):
    def __init__(self, initial):
        Problem.__init__(self, initial)

    def expand(self, node):
        children = []
        nopuestos = [0,1,2,3,4,5,6,7]

        for x in node.state:
            for y in nopuestos:
                if x == y:
                    nopuestos.remove(x)
        for n in nopuestos:
            pq = self.putQueen(node, n)
            if pq is not None:
                children.append(pq)
        return children

    def goal(self, node):

        if len(node.state) != 0 and len(node.state) == 8:
            return True
        else:
            return False

    def putQueen(self, node, pos):
        state = node.state
        newstate = copy.deepcopy(state)
        if len(newstate) < 8:
            if self.verifyAttack(state, pos):
                return None

            newstate.append(pos)
            return Node(newstate, node, 'add')
        return None

    def verifyAttack(self, state, pos):
        newpos = pos
        if len(state) == 0:
            return False
        count = len(state) - 1

        while count >= 0:
            if state[count] == (newpos - 1):
               return True
            count = count - 1
            newpos = newpos - 1

        count = len(state) - 1
        newpos = pos
        while count >= 0:
            if state[count] == (newpos + 1):
                return True
            count = count - 1
            newpos = newpos + 1
        return False

