

class BreadthFirstSearch:
  def __init__(self, problem):
    self.open=[]
    self.close=[]
    self.children=[]
    self.problem=problem

  def run(self):
    self.open.append(self.problem.initial)
    solution=[]
    while self.open:

      actual=self.open.pop(0)
      if self.problem.goal(actual):
        return actual
      else:
        self.close.append(actual)
        self.children = self.problem.expand(actual)
        self.clean()
        #self.open.extend(self.children)
        self.open = self.children + self.open

    return solution

  def clean(self):
    for n in self.children[:]:
      for m in self.open:
        if(n==m):
          self.children.remove(n)
    for n in self.children[:]:
      for m in self.close:
        if(n==m):
          self.children.remove(n)
