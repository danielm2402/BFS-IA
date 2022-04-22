from Node import Node
from BreadthFirstSearch import  BreadthFirstSearch
from Puzzle import Puzzle

def main():
    initial = Node([[8, 1, 3], [2, 4, 5], [0, 7, 6]])
    goal = Node([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    puzzle = Puzzle(initial, goal)
    bfs = BreadthFirstSearch(puzzle)
    solution = bfs.run()
    print(solution)


if __name__ == "__main__":
    main()