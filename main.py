from Node import Node
from BreadthFirstSearch import  BreadthFirstSearch
from Queens import Puzzle

def main():
    initial = Node([])
    goal = ""
    puzzle = Puzzle(initial, goal, False)
    bfs = BreadthFirstSearch(puzzle)
    solution = bfs.run()
    print(solution)


if __name__ == "__main__":
    main()