import copy
from Node import Node
from Problem import Problem
import random

class Puzzle(Problem):
    def __init__(self, initial, goal, isExplicit):
        Problem.__init__(self, initial, goal, isExplicit)

    def expand(self, node):
        children = []
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

    def putQueen(self, node):
        state = node.state
        newstate = copy.deepcopy(state)
        if len(newstate) < 8:
            nopuestos=[0,1,2,3,4,5,6,7,8]
            for x in newstate:
                for y in nopuestos:
                    if x == y:
                        nopuestos.remove(x)
            pos = random.choice(nopuestos)
            count = 0
            while self.verifyAttack(state, pos) or count < len(nopuestos):
                self.verifyAttack(pos)
                pos = random.choice(nopuestos)
                count=count+1

            if not self.verifyAttack(state, pos):
                newstate.append(pos)
                newnode = Node(newstate, node, 'add')
                return newnode
            return None

        return None



    def verifyAttack(self, state, pos):
        if (pos-1) == state[-1] or (pos+1) == state[-1]:
            return True
        return False
