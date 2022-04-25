from Node import Node
from BreadthFirstSearch import  BreadthFirstSearch
from Queens import Queens

def main():
    #[0, 4, 7, 5, 2, 6, 1, 3])
    initial = Node([])
    queens = Queens(initial)
    bfs = BreadthFirstSearch(queens)
    solution = bfs.run()
    print("Solucion",solution)


if __name__ == "__main__":
    main()



