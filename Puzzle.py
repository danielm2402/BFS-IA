import copy
from Node import Node
from Problem import Problem

class Puzzle(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)

    def expand(self, node):
        children = []

        l = self.left(node)
        if l is not None:
            children.append(l)

        r = self.right(node)
        if r is not None:
            children.append(r)

        u = self.up(node)
        if u is not None:
            children.append(u)

        d = self.down(node)
        if d is not None:
            children.append(d)

        return children

    def left(self, node):
        state = node.state
        i, j = self.findgap(state)
        if (i > -1 and j > -1 and j < 2):
            newstate = copy.deepcopy(state)
            valor = newstate[i][j + 1]
            newstate[i][j + 1] = 0
            newstate[i][j] = valor
            newnode = Node(newstate, node, 'left')
            return newnode
        else:
            return None

    def right(self, node):
        state = node.state
        i, j = self.findgap(state)
        if (i > -1 and j > -1 and j > 0):
            newstate = copy.deepcopy(state)
            valor = newstate[i][j - 1]
            newstate[i][j - 1] = 0
            newstate[i][j] = valor
            newnode = Node(newstate, node, 'right')
            return newnode
        else:
            return None

    def up(self, node):
        state = node.state
        i, j = self.findgap(state)
        if (i > -1 and j > -1 and i < 2):
            newstate = copy.deepcopy(state)
            valor = newstate[i + 1][j]
            newstate[i + 1][j] = 0
            newstate[i][j] = valor
            newnode = Node(newstate, node, 'up')
            return newnode
        else:
            return None

    def down(self, node):
        state = node.state
        i, j = self.findgap(state)
        if (i > -1 and j > -1 and i > 0):
            newstate = copy.deepcopy(state)
            valor = newstate[i - 1][j]
            newstate[i - 1][j] = 0
            newstate[i][j] = valor
            newnode = Node(newstate, node, 'down')
            return newnode
        else:
            return None

    def findgap(self, state):
        for i, row in enumerate(state):
            for j, col in enumerate(row):
                if col == 0:
                    return i, j
        return -1, -1
