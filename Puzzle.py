import copy
from Node import Node
from Problem import Problem

class Puzzle(Problem):
    def __init__(self, initial, goal, isExplicit):
        Problem.__init__(self, initial, goal, isExplicit)

    def expand(self, node):
        children = []
        print('HERE')
        pq = self.putQueen(node)
        if pq is not None:
            children.append(pq)
            return children

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

    def putQueen(self, node):
        print('1 VEZ')
        state = node.state
        j = self.lastQueen(state) + 1
        if j == 0 or j != 8:
            newstate = copy.deepcopy(state)
            newstate[0][j-1]=1
            newnode = Node(newstate, node, 'put')
            return newnode
        else:
            return None

    def lastQueen(self, state):
        for i, row in enumerate(state):
            for j, col in enumerate(row):
                if col == 1:
                    return j
        return -1

    def findgap(self, state):
        for i, row in enumerate(state):
            for j, col in enumerate(row):
                if col == 0:
                    return j
        return -1, -1
