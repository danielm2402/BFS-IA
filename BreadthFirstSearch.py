

class BreadthFirstSearch:
  def __init__(self, problem):
    self.open=[]
    self.close=[]
    self.children=[]
    self.problem=problem

  def run(self):
    self.open.append(self.problem.initial)
    solution=[]
    if self.problem.isExplicit:
      while self.open:
        actual=self.open.pop(0)
        print('actual',actual)
        if(actual == self.problem.goal):
          while actual:
            action=actual.action
            actual=actual.parent
            solution.append(action)
          solution.reverse()
          return solution

        else:
          self.close.append(actual)
          self.children=self.problem.expand(actual)
          self.clean()
          self.open.extend(self.children)
      return solution
    else:
      while True:
        actual = self.open.pop(0)
        print('actual', actual)
        if eval(self.problem.goal):
          while actual:
            action = actual.action
            actual = actual.parent
            solution.append(action)
          solution.reverse()
          return solution

        else:
          self.close.append(actual)
          self.children = self.problem.expand(actual)
          self.clean()
          self.open.insert(0,self.children)

      return "test"

  def clean(self):
    for n in self.children[:]:
      for m in self.open:
        if(n==m):
          self.children.remove(n)
    for n in self.children[:]:
      for m in self.close:
        if(n==m):
          self.children.remove(n)
