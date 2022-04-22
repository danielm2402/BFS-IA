from Node import Node
from BreadthFirstSearch import  BreadthFirstSearch
from Puzzle import Puzzle

def main():
    initial = Node([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
    goal = "sum(list(map(sum, actual.state))) == 36"
    puzzle = Puzzle(initial, goal, False)
    bfs = BreadthFirstSearch(puzzle)
    solution = bfs.run()
    print(solution)


if __name__ == "__main__":
    main()